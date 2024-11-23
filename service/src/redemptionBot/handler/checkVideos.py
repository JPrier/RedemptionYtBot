from redemptionBot.logic import videosComponent
from redemptionBot.util import timeUtil


def process(event, context):
    print(f"Received CheckVideo Event {event}")
    time = timeUtil.getCurrentTimestamp()
    if event:
        time = event.get("time", timeUtil.getCurrentTimestamp())
    videos = videosComponent.collectNewVideos(time)
    print(f"Collected {len(videos)} for timestamp {time} -- videos: {videos}")
    return {"new_videos": videos}
