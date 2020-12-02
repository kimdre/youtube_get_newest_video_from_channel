import requests


class API:
    def __init__(self, youtube_api_key):
        self.api_key = youtube_api_key

    def get_video_items(self, channel_id):
        try:
            request = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=' + \
                      channel_id + '&maxResults=10&order=date&type=video&key=' + \
                      self.api_key

            return requests.get(request).json()

        except Exception as error:
            print(error)

    @staticmethod
    def get_newest_video(items_json):
        return items_json['items'][0]

    @staticmethod
    def get_url(video_json):
        return video_json['id']['videoId']

    @staticmethod
    def get_title(video_json):
        return video_json['snippet']['title']

    def get_latest_video(self, channel_id):
        video_items_json = self.get_video_items(channel_id)
        new_video_json = self.get_newest_video(video_items_json)

        video_url_snippet = self.get_url(new_video_json)
        video_url = 'https://www.youtube.com/watch?v=' + video_url_snippet

        video_title = self.get_title(new_video_json)

        return video_title, video_url
