import os
import json
from redemptionBot.data import videoDataBuilder


def collectNewVideos(timestamp):
    CHANNEL_IDS = json.loads(os.getenv("YOUTUBE_CHANNEL_IDS", "[]"))
    return [
        video
        for channelId in CHANNEL_IDS
        for video in videoDataBuilder.getVideosFromChannelId(channelId, timestamp)
    ]
