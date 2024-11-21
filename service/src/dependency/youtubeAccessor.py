import os
from googleapiclient.discovery import build

API_KEY = os.getenv('YOUTUBE_API_KEY')

def getVideosFromChannelId(channelId, maxNumberOfVideos=5):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
            part='snippet',
            channelId=channel,
            maxResults=maxNumberOfVideos
        )
    response = request.execute()
    print(f'Successfully completed request for channel {channel} and got {len(response['items'])}')
    return response['items']

def getVideosFromChannelIdBetweenTimestamps(channelId, beforeTimestamp, afterTimestamp, maxNumberOfVideos=5):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
            part='snippet',
            channelId=channel,
            publishedAfter=afterTimestamp,
            publishedBefore=beforeTimestamp,
            maxResults=maxNumberOfVideos
        )
    response = request.execute()
    print(f'Successfully completed retrieved videos for channel {channel} between {afterTimestamp} and {beforeTimestamp}, and received {len(response['items'])}')
    return response['items']
