from ..framework.base_class_requests import BaseRequest
from .config.test_data import DataSearch, DataReverse


class SpecializedUtility:
    def __init__(self):
        self.params_search = DataSearch.PARAMETERS
        self.params_reverse = DataReverse.PARAMETERS

    def get_params_for_request_search(self, data: str):
        data_req = {"q": data}
        data_req.update(self.params_search)
        return data_req

    def get_params_for_request_reverse(self, data: dict):
        data.update(self.params_reverse)
        return data


class Search(BaseRequest):
    SEARCH = "search"

    def __init__(self):
        super().__init__()

    def get_response_search(self, data):
        response = self.request_api.make_a_custom_request(
            "GET",
            f"{self.url}{self.SEARCH}",
            params=SpecializedUtility().get_params_for_request_search(data)
        )
        return self.get_response_model(response)


class Reverse(BaseRequest):
    REVERSE = "reverse"

    def __init__(self):
        super().__init__()

    def get_response_reverse(self, data):
        response = self.request_api.make_a_custom_request(
            "GET",
            f"{self.url}{self.REVERSE}",
            params=SpecializedUtility().get_params_for_request_reverse(data)
        )
        return self.get_response_model(response)
