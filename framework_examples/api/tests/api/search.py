from framework_examples.api.framework.base_request import BaseRequest
from framework_examples.api.tests.utils.set_params import Params


class Search(BaseRequest):
    SEARCH = "search"

    def __init__(self):
        super().__init__()

    def get_response_search(self, data):
        response = self.request_api.make_a_custom_request(
            "GET",
            f"{self.url}{self.SEARCH}",
            params=Params().get_params_for_request_search(data)
        )
        return self.get_response_model(response)
