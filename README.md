# youtube_get_newest_video_from_channel
Small Python script to get the latest video from a specific Youtube channel and returns it's title and url

[![Build Status](https://drone.pyas.de/api/badges/Kim/youtube_get_newest_video_from_channel/status.svg)](https://drone.pyas.de/Kim/youtube_get_newest_video_from_channel)

* You need to get an API Key for the [Youtube Data API V3](https://console.developers.google.com/) -> Create a project, then add a key to it
* The Channel ID -> May be Part of the URL if you go to the channel (after 'https://www.youtube.com/channel/' and before the first '?&'

**Hint:** 

Nowadays the channel url doesn't always show the channel id, but sometimes the channel name.
However the script needs the channel id. You can get the id from here when you only have the channel name: https://commentpicker.com/youtube-channel-id.php
A channel id looks like this `UCmpilcSVu1T-AsAiiHbfpcA`


Requires python module '_requests_' to work.

## Usage example
````python
from GetLatestVideo import API

# Add your Youtube Data API V3 Key here
API_KEY = ''

# Add the Channel ID(s) here,
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

## Credits
Repo Icon made by [Freepik](https://www.freepik.com "Freepik") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon")