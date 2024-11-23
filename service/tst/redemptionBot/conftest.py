import pytest
from redemptionBot.types.videoInfo import VideoInfo


@pytest.fixture
def testChannelId():
    return "TEST_CHANNEL_ID"


@pytest.fixture
def testChannelTitle():
    return "TEST_CHANNEL_TITLE"


@pytest.fixture
def testVideoId():
    return "TEST_VIDEO_ID"


@pytest.fixture
def testVideoTitle():
    return "TEST_VIDEO_TITLE"


@pytest.fixture
def testVideoInfo(testVideoId, testVideoTitle, testChannelTitle) -> VideoInfo:
    return {
        "videoId": testVideoId,
        "videoTitle": testVideoTitle,
        "channelName": testChannelTitle,
    }


@pytest.fixture
def testYoutubeVideoData(testVideoId, testChannelId, testVideoTitle, testChannelTitle):
    return {
        "kind": "youtube#searchResult",
        "etag": "TEST_ETAG",
        "id": {"kind": "youtube#video", "videoId": testVideoId},
        "snippet": {
            "publishedAt": "2024-11-21T22:19:41Z",
            "channelId": testChannelId,
            "title": testVideoTitle,
            "description": "",
            "thumbnails": {
                "default": {
                    "url": "https://i.ytimg.com/vi/URL/default.jpg",
                    "width": 120,
                    "height": 90,
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/URL/mqdefault.jpg",
                    "width": 320,
                    "height": 180,
                },
                "high": {
                    "url": "https://i.ytimg.com/vi/URL/hqdefault.jpg",
                    "width": 480,
                    "height": 360,
                },
            },
            "channelTitle": testChannelTitle,
            "liveBroadcastContent": "none",
            "publishTime": "2024-11-21T22:19:41Z",
        },
    }
