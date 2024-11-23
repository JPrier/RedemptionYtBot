from redemptionBot.dependency import youtubeAccessor
from redemptionBot.util import timeUtil

# TODO: Move this to a env variable to support dynamic period changes
TIME_DIFF = 60  # Number of Minutes for video checks


def getVideosFromChannelId(channelId, timestamp):
    # TODO: Figure out what data is required from the youtube response and condense it into an internal type
    beforeTimestamp = timeUtil.addMinutesToTimestamp(timestamp, TIME_DIFF)
    return youtubeAccessor.getVideosFromChannelIdBetweenTimestamps(
        channelId, beforeTimestamp, timestamp
    )
