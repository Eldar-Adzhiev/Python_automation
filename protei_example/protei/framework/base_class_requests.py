from .models import ResponseModel
from ..tests.config.config import Config
from .requests import ShellRequestAPI


class BaseRequest:
    URL = Config.BASE_URL

    def __init__(self):
        self.url = self.URL
        self.request_api = ShellRequestAPI()

    @staticmethod
    def get_response_model(response):
        return ResponseModel(status=response.status_code, response=response.json(), url=response.url)
