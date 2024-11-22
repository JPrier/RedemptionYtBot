from logic import videoComponent


def process(event, context):
    print(f"Received CheckVideo Event {event}")
    videos = videoComponent.collectNewVideos(event.get("time", ""))
    print(f"Collected {len(videos)} videos")
    return {"new_videos": videos}
