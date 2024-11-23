import os
from googleapiclient.discovery import build


def getVideosFromChannelId(channelId, maxNumberOfVideos=5):
    API_KEY = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        part="snippet", channelId=channelId, maxResults=maxNumberOfVideos
    )
    response = request.execute()
    print(
        f'Successfully completed request for channel {channelId} and got {len(response['items'])}'
    )
    return response["items"]


def getVideosFromChannelIdBetweenTimestamps(
    channelId, beforeTimestamp, afterTimestamp, maxNumberOfVideos=5
):
    API_KEY = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        part="snippet",
        channelId=channelId,
        publishedAfter=afterTimestamp,
        publishedBefore=beforeTimestamp,
        maxResults=maxNumberOfVideos,
    )
    response = request.execute()
    print(
        f'Successfully completed retrieved videos for channel {channelId} between {afterTimestamp} and {beforeTimestamp}, and received {len(response['items'])}'
    )
    print(f"Response: {response}")
    print(f'Items: {response['items']}')
    return response["items"]
