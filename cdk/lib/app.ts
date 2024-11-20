#!/usr/bin/env node
import { App } from 'aws-cdk-lib';
import { YoutubeBotStack } from './stacks/youtubeBotStack';
import { STAGES } from './config/stages';

const app = new App();

STAGES.forEach((stage) => {
  new YoutubeBotStack(app, `YoutubeBotStack-${stage.name}`, {
    env: stage.env,
    stage: stage
  });
});
