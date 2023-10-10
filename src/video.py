# from src.channel import Channel
from src.apimixin import APIMixin


class Video(APIMixin):
    def __init__(self, video_id):
        try:
            self.id = video_id
            self.video_info = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                           id=self.video_id).execute()
            self.title = self.video_info['items'][0]['snippet']['title']
            self.url = 'https://www.youtube.com/watch?v=' + video_id
            self.view_count = self.video_info['items'][0]['statistics']['viewCount']
            self.like_count = self.video_info['items'][0]['statistics']['likeCount']
        except:
            self.id = video_id
            self.video_info = None
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id, pl_video_id):
        super().__init__(video_id)
        self.pl_video_id = pl_video_id

    def __str__(self):
        return f'{self.title}'
