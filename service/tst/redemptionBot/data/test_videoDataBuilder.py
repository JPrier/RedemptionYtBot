from unittest.mock import patch
import redemptionBot.data.videoDataBuilder as underTest


@patch(
    "redemptionBot.data.videoDataBuilder.youtubeAccessor.getVideosFromChannelIdBetweenTimestamps"
)
@patch("redemptionBot.data.videoDataBuilder.timeUtil.addMinutesToTimestamp")
@patch("os.getenv")
def test_getVideosFromChannelId(
    mock_getenv, mock_add_minutes, mock_get_videos, testYoutubeVideoData, testVideoInfo
):
    mock_getenv.return_value = "10"

    channel_id = "test_channel"
    timestamp = "2024-11-21T10:00:00Z"
    mock_add_minutes.return_value = "2024-11-21T09:00:00Z"
    mock_get_videos.return_value = [testYoutubeVideoData, testYoutubeVideoData]

    result = underTest.getVideosFromChannelId(channel_id, timestamp)

    mock_add_minutes.assert_called_once_with(timestamp, 10)
    mock_get_videos.assert_called_once_with(
        channel_id, "2024-11-21T09:00:00Z", timestamp
    )
    assert result == [testVideoInfo, testVideoInfo]


@patch(
    "redemptionBot.data.videoDataBuilder.youtubeAccessor.getVideosFromChannelIdBetweenTimestamps"
)
@patch("redemptionBot.data.videoDataBuilder.timeUtil.addMinutesToTimestamp")
@patch("os.getenv")
def test_getVideosFromChannelId_withEmptyVideoLists(
    mock_getenv, mock_add_minutes, mock_get_videos
):
    mock_getenv.return_value = "10"

    channel_id = "test_channel"
    timestamp = "2024-11-21T10:00:00Z"
    mock_add_minutes.return_value = "2024-11-21T09:00:00Z"
    mock_get_videos.return_value = []

    result = underTest.getVideosFromChannelId(channel_id, timestamp)

    mock_add_minutes.assert_called_once_with(timestamp, 10)
    mock_get_videos.assert_called_once_with(
        channel_id, "2024-11-21T09:00:00Z", timestamp
    )
    assert result == []
