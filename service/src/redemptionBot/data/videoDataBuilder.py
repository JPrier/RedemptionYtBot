import os
from redemptionBot.dependency import youtubeAccessor
from redemptionBot.util import timeUtil
from redemptionBot.types.videoInfo import VideoInfo


def getVideosFromChannelId(channelId, timestamp):
    TIME_DIFF = int(os.getenv("TIME_DELTA"))
    beforeTimestamp = timeUtil.addMinutesToTimestamp(timestamp, TIME_DIFF)
    ytVideos = youtubeAccessor.getVideosFromChannelIdBetweenTimestamps(
        channelId, beforeTimestamp, timestamp
    )

    return [convertVideoToVideoInfo(ytVideo) for ytVideo in ytVideos]


def convertVideoToVideoInfo(ytVideo) -> VideoInfo:
    return {
        "channelName": ytVideo["snippet"]["channelTitle"],
        "videoTitle": ytVideo["snippet"]["title"],
        "videoId": ytVideo["id"]["videoId"],
    }
