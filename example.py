from GetLatestVideo import API

# Add your Youtube Data API V3 Key here
API_KEY = ''

# Add the Channel IDs here
# When you only know the channel name you can get the ID from here https://commentpicker.com/youtube-channel-id.php
CHANNEL_ID = [
    'ID1',
    'ID2'
]

videos = []

yt = API(API_KEY)

for channel in CHANNEL_ID:
    videos.append(yt.get_latest_video(channel))

print(videos)
