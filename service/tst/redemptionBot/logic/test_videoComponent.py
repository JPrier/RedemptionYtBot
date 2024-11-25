import unittest
from unittest.mock import patch
import redemptionBot.logic.videosComponent as underTest


class TestVideosComponent(unittest.TestCase):
    @patch(
        "redemptionBot.logic.videosComponent.videoDataBuilder.getVideosFromChannelId"
    )
    @patch("os.getenv")
    def test_collectNewVideos(self, mock_getenv, mock_get_videos):
        mock_getenv.return_value = '["channel1", "channel2"]'
        mock_get_videos.side_effect = [[{"id": "video1"}], [{"id": "video2"}]]
        timestamp = "2024-11-21T10:00:00Z"

        result = underTest.collectNewVideos(timestamp)

        mock_get_videos.assert_any_call("channel1", timestamp)
        mock_get_videos.assert_any_call("channel2", timestamp)
        self.assertEqual(result, [{"id": "video1"}, {"id": "video2"}])

    @patch(
        "redemptionBot.logic.videosComponent.videoDataBuilder.getVideosFromChannelId"
    )
    @patch("os.getenv")
    def test_collectNewVideos_noVideos(self, mock_getenv, mock_get_videos):
        mock_getenv.return_value = '["channel1", "channel2"]'
        mock_get_videos.side_effect = [[], []]
        timestamp = "2024-11-21T10:00:00Z"

        result = underTest.collectNewVideos(timestamp)

        mock_get_videos.assert_any_call("channel1", timestamp)
        mock_get_videos.assert_any_call("channel2", timestamp)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
