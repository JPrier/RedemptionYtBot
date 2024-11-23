from redemptionBot.logic import videosComponent
from redemptionBot.util import timeUtil


def process(event, context):
    print(f"Received CheckVideo Event {event}")
    videos = videosComponent.collectNewVideos(
        event.get("time", timeUtil.getCurrentTimestamp())
    )
    print(f"Collected {len(videos)} videos")
    return {"new_videos": videos}
