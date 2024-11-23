import os
from redemptionBot.dependency import youtubeAccessor
from redemptionBot.util import timeUtil


def getVideosFromChannelId(channelId, timestamp):
    TIME_DIFF = int(os.getenv("TIME_DELTA"))
    # TODO: Figure out what data is required from the youtube response and condense it into an internal type
    beforeTimestamp = timeUtil.addMinutesToTimestamp(timestamp, TIME_DIFF)
    return youtubeAccessor.getVideosFromChannelIdBetweenTimestamps(
        channelId, beforeTimestamp, timestamp
    )
