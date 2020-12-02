# youtube_newest_video_from_channel
Small Python script to get the latest video from a specific Youtube channel and returns it's title and url

* You need to get an API Key for the [Youtube Data API V3](https://console.developers.google.com/) -> Create a project, then add a key to it
* The Channel ID -> May be Part of the URL if you go to the channel (after 'https://www.youtube.com/channel/' and before the first '?&'

**Hint:** 

Nowadays the channel url not always shows the channel id, but sometimes the channel name.
However the script needs the channel id. You can get the id from here when you only have the channel name: https://commentpicker.com/youtube-channel-id.php



Requires '_requests_' to work.

## Usage example
````python
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
````