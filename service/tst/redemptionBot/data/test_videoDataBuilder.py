import unittest
from unittest.mock import patch
import redemptionBot.data.videoDataBuilder as underTest


class TestVideoDataBuilder(unittest.TestCase):
    @patch(
        "redemptionBot.data.videoDataBuilder.youtubeAccessor.getVideosFromChannelIdBetweenTimestamps"
    )
    @patch("redemptionBot.data.videoDataBuilder.timeUtil.addMinutesToTimestamp")
    @patch("os.getenv")
    def test_getVideosFromChannelId(
        self, mock_getenv, mock_add_minutes, mock_get_videos
    ):
        mock_getenv.return_value = "10"

        channel_id = "test_channel"
        timestamp = "2024-11-21T10:00:00Z"
        mock_add_minutes.return_value = "2024-11-21T09:00:00Z"
        mock_get_videos.return_value = [{"id": "video1"}, {"id": "video2"}]

        result = underTest.getVideosFromChannelId(channel_id, timestamp)

        mock_add_minutes.assert_called_once_with(timestamp, 10)
        mock_get_videos.assert_called_once_with(
            channel_id, "2024-11-21T09:00:00Z", timestamp
        )
        self.assertEqual(result, [{"id": "video1"}, {"id": "video2"}])


if __name__ == "__main__":
    unittest.main()
