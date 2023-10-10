import os
from googleapiclient.discovery import build


class APIMixin:
    """Класс-миксин для предоставления доступа к API."""

    api_key: str = os.getenv('YOU_TUBE_API_KEY')

    @classmethod
    def get_service(cls) -> build:
        """Возвращает объект для работы с API youtube."""
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube
