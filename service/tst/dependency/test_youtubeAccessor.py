import unittest
from unittest.mock import patch, MagicMock
from dependency import youtubeAccessor as underTest


class TestYoutubeAccessor(unittest.TestCase):
    @patch("dependency.youtubeAccessor.build")
    @patch("os.getenv")
    def test_getVideosFromChannelId(self, mock_getenv, mock_build):
        mock_getenv.return_value = "TEST_KEY"

        # Mock YouTube API client and its response
        mock_youtube = MagicMock()
        mock_build.return_value = mock_youtube
        mock_request = mock_youtube.search().list.return_value
        mock_request.execute.return_value = {
            "items": [{"id": "video1"}, {"id": "video2"}]
        }

        # Call the function under test
        channel_id = "test_channel"
        result = underTest.getVideosFromChannelId(channel_id)

        # Assertions
        mock_build.assert_called_once_with("youtube", "v3", developerKey="TEST_KEY")
        mock_youtube.search().list.assert_called_once_with(
            part="snippet", channelId=channel_id, maxResults=5
        )
        self.assertEqual(result, [{"id": "video1"}, {"id": "video2"}])

    @patch("dependency.youtubeAccessor.build")
    @patch("os.getenv")
    def test_getVideosFromChannelIdBetweenTimestamps(self, mock_getenv, mock_build):
        mock_getenv.return_value = "TEST_KEY"

        # Mock YouTube API client and its response
        mock_youtube = MagicMock()
        mock_build.return_value = mock_youtube
        mock_request = mock_youtube.search().list.return_value
        mock_request.execute.return_value = {
            "items": [{"id": "video3"}, {"id": "video4"}]
        }

        # Call the function under test
        channel_id = "test_channel"
        before_timestamp = "2024-11-21T09:00:00Z"
        after_timestamp = "2024-11-21T08:00:00Z"
        result = underTest.getVideosFromChannelIdBetweenTimestamps(
            channel_id, before_timestamp, after_timestamp
        )

        # Assertions
        mock_build.assert_called_once_with("youtube", "v3", developerKey="TEST_KEY")
        mock_youtube.search().list.assert_called_once_with(
            part="snippet",
            channelId=channel_id,
            publishedAfter=after_timestamp,
            publishedBefore=before_timestamp,
            maxResults=5,
        )
        self.assertEqual(result, [{"id": "video3"}, {"id": "video4"}])


if __name__ == "__main__":
    unittest.main()
