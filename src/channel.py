import json
import os
from googleapiclient.discovery import build



class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YOU_TUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)   # объект для работы с api ютуба

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.describtion = self.channel_info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + channel_id
        self.subscriber_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале в удобном формате, с отступами"""
        print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, file_name) -> None:
        """Сохраняет в файл json значения атрибутов экземпляра в виде словаря"""
        with open(file_name, 'w', encoding='utf8') as file:
            data = {'channel_id': self.channel_id, 'title': self.title, 'describtion': self.describtion,
                    'url': self.url, 'subscriber_count': self.subscriber_count, 'video_count': self.video_count,
                    'view_count': self.view_count}
            json.dump(data, file, indent=2, ensure_ascii=False)
