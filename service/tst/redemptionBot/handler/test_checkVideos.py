import unittest
from unittest.mock import patch
from datetime import datetime, timezone
import redemptionBot.handler.checkVideos as underTest


class TestCheckVideos(unittest.TestCase):
    @patch("redemptionBot.handler.checkVideos.videosComponent.collectNewVideos")
    def test_process_success(self, mock_collect_new_videos):
        mock_collect_new_videos.return_value = [{"id": "video1"}]
        event = {"time": "2024-11-21T10:00:00Z"}

        result = underTest.process(event, None)

        mock_collect_new_videos.assert_called_once_with("2024-11-21T10:00:00Z")
        self.assertEqual(result, {"new_videos": [{"id": "video1"}]})

    @patch("redemptionBot.handler.checkVideos.videosComponent.collectNewVideos")
    def test_process_emptyInputTimestamp_success(self, mock_collect_new_videos):
        mock_collect_new_videos.return_value = [{"id": "video1"}]

        result = underTest.process({}, None)
        expectedTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        mock_collect_new_videos.assert_called_once_with(expectedTime)
        self.assertEqual(result, {"new_videos": [{"id": "video1"}]})

    @patch("redemptionBot.handler.checkVideos.videosComponent.collectNewVideos")
    def test_process_emptyVideoList_success(self, mock_collect_new_videos):
        mock_collect_new_videos.return_value = []

        result = underTest.process({}, None)
        expectedTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        mock_collect_new_videos.assert_called_once_with(expectedTime)
        self.assertEqual(result, {"new_videos": []})

    @patch("redemptionBot.handler.checkVideos.videosComponent.collectNewVideos")
    def test_process_nullInput_success(self, mock_collect_new_videos):
        mock_collect_new_videos.return_value = [{"id": "video1"}]

        result = underTest.process(None, None)
        expectedTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        mock_collect_new_videos.assert_called_once_with(expectedTime)
        self.assertEqual(result, {"new_videos": [{"id": "video1"}]})


if __name__ == "__main__":
    unittest.main()
