from api_framework.framework.models import ResponseModel
from api_framework.framework.constants import Configuration
from api_framework.framework.requests import ShellRequestAPI


class BaseRequest:
    URL = Configuration.URL

    def __init__(self):
        self.url = self.URL
        self.request_api = ShellRequestAPI()

    @staticmethod
    def get_response_model(response):
        return ResponseModel(status=response.status_code, response=response.json(), url=response.url)
