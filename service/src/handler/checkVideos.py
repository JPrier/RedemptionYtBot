from googleapiclient.discovery import build

API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_IDS = os.getenv('YOUTUBE_CHANNEL_IDS')

def process(event, context):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    for channel in CHANNEL_IDS:
        request = youtube.search().list(
            part='snippet',
            channelId=CHANNEL_ID,
            maxResults=5,  # Fetch up to 5 latest videos
            order='date'
        )
        print(request.execute())
