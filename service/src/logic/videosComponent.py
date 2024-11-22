import os
import json
from data import videoDataBuilder


def collectNewVideos(timestamp):
    CHANNEL_IDS = json.loads(os.getenv("YOUTUBE_CHANNEL_IDS", "[]"))
    return [
        videoDataBuilder.getVideosFromChannelId(channelId, timestamp)
        for channelId in CHANNEL_IDS
    ]
