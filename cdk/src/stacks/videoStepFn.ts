import { Duration, RemovalPolicy } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { Choice, Condition, Map, Pass, StateMachine } from 'aws-cdk-lib/aws-stepfunctions';
import { LambdaInvoke } from 'aws-cdk-lib/aws-stepfunctions-tasks';
import { Rule, Schedule } from 'aws-cdk-lib/aws-events';
import { SfnStateMachine } from 'aws-cdk-lib/aws-events-targets';

export class YoutubeBotStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 bucket for storing video files
    const videoBucket = new Bucket(this, 'VideoBucket', {
      removalPolicy: RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // Lambda function to check for new videos
    const checkForVideosLambda = new Function(this, 'CheckForVideos', {
      runtime: Runtime.PYTHON_3_9,
      handler: 'checkVideos.process',
      code: Code.fromAsset('service/src/handler/checkVideos'),
      environment: {
        VIDEO_BUCKET_NAME: videoBucket.bucketName,
      },
    });

    // Lambda function to download videos
    const downloadVideoLambda = new Function(this, 'DownloadVideo', {
      runtime: Runtime.PYTHON_3_9,
      handler: 'downloadVideo.process',
      code: Code.fromAsset('service/src/handler/downloadVideo'),
      environment: {
        VIDEO_BUCKET_NAME: videoBucket.bucketName,
      },
    });

    // Lambda function to edit videos
    const editVideoLambda = new Function(this, 'EditVideo', {
      runtime: Runtime.PYTHON_3_9,
      handler: 'editVideo.process',
      code: Code.fromAsset('service/src/handler/editVideo'),
      environment: {
        VIDEO_BUCKET_NAME: videoBucket.bucketName,
      },
    });

    // Lambda function to upload videos
    const uploadVideoLambda = new Function(this, 'UploadVideo', {
      runtime: Runtime.PYTHON_3_9,
      handler: 'uploadVideo.process',
      code: Code.fromAsset('service/src/handler/uploadVideo'),
    });

    // Grant permissions to Lambdas
    videoBucket.grantReadWrite(checkForVideosLambda);
    videoBucket.grantReadWrite(downloadVideoLambda);
    videoBucket.grantReadWrite(editVideoLambda);

    // Step Functions definition
    const downloadVideoTask = new LambdaInvoke(this, 'DownloadVideoTask', {
      lambdaFunction: downloadVideoLambda,
    });

    const editVideoTask = new LambdaInvoke(this, 'EditVideoTask', {
      lambdaFunction: editVideoLambda,
    });

    const uploadVideoTask = new LambdaInvoke(this, 'UploadVideoTask', {
      lambdaFunction: uploadVideoLambda,
    });

    const checkForVideosTask = new LambdaInvoke(this, 'CheckForVideosTask', {
      lambdaFunction: checkForVideosLambda,
      outputPath: '$.Payload', // Pass Lambda response to the next state
    });

    // Map state to process multiple videos concurrently
    const mapState = new Map(this, 'ProcessVideos', {
      inputPath: '$.new_videos',
      itemsPath: '$',
      resultPath: '$.results', // Collect results of all iterations
      maxConcurrency: 5, // Limit concurrency if needed
    });

    mapState.iterator(
      downloadVideoTask
        .next(editVideoTask)
        .next(uploadVideoTask)
    );

    // Choice state to check if there are any new videos
    const isVideoListEmpty = new Choice(this, 'AreVideosAvailable');

    isVideoListEmpty
      .when(
        Condition.isPresent('$.new_videos[0]'),
        mapState // Proceed with Map state if new videos exist
      )
      .otherwise(
        new Pass(this, 'NoNewVideos', {
          result: { value: 'No new videos found' },
        })
      );

    // Define the overall workflow
    const definition = checkForVideosTask
      .next(isVideoListEmpty);

    const stateMachine = new StateMachine(this, 'StateMachine', {
      definition,
    });

    // EventBridge rule to trigger Step Functions every hour
    new Rule(this, 'ScheduleRule', {
      schedule: Schedule.rate(Duration.hours(1)),
      targets: [new SfnStateMachine(stateMachine)],
    });
  }
}
