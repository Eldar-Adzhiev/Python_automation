from api_framework.framework.base_request import BaseRequest
from api_framework.tests.utils.set_params import Params


class Reverse(BaseRequest):
    REVERSE = "reverse"

    def __init__(self):
        super().__init__()

    def get_response_reverse(self, data):
        response = self.request_api.make_a_custom_request(
            "GET",
            f"{self.url}{self.REVERSE}",
            params=Params().get_params_for_request_reverse(data)
        )
        return self.get_response_model(response)

