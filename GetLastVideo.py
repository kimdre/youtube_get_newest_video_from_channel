import requests


class API:
    def __init__(self, youtube_api_key, channel_id):
        self.api_key = youtube_api_key
        self.channel_id = channel_id

    def is_not_used(self):
        pass

    def get_video_items(self):
        request = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=' + \
                  self.channel_id + '&maxResults=10&order=date&type=video&key=' + \
                  self.api_key

        return requests.get(request).json()

    def get_newest_video(self, items_json):
        self.is_not_used()
        return items_json['items'][0]

    def get_url(self, video_json):
        self.is_not_used()
        return video_json['id']['videoId']

    def get_title(self, video_json):
        self.is_not_used()
        return video_json['snippet']['title']

    def start_find_video_process(self):
        self.is_not_used()
        video_items_json = var.get_video_items()
        new_video_json = var.get_newest_video(video_items_json)

        video_url_snippet = var.get_url(new_video_json)
        video_url = 'https://www.youtube.com/watch?v=' + video_url_snippet

        video_title = var.get_title(new_video_json)

        return video_title, video_url


# Add your Youtube Data API V3 Key here
API_KEY = ''

# Add the Channel IDs here
# When you only know the channel name you can get the ID from here https://commentpicker.com/youtube-channel-id.php
CHANNEL_ID = [
    'ID1',
    'ID2'
]

videos = []

for item in CHANNEL_ID:
    var = API(API_KEY, item)
    videos.append(var.start_find_video_process())

print(videos)
