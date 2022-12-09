from framework_examples.api.configurations.config import SearchParams, ReverseParams


class Params:
    def __init__(self):
        self.params_search = SearchParams.PARAMETERS
        self.params_reverse = ReverseParams.PARAMETERS

    def get_params_for_request_search(self, data: str):
        data_dict = {"q": data}
        data_dict.update(self.params_search)
        return data_dict

    def get_params_for_request_reverse(self, data: dict):
        data.update(self.params_reverse)
        return data
