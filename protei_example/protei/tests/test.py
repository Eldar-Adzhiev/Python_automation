# coding=utf-8
from ..framework.utils.logger import Logger
from .models.schemas import ResponseModel
from .models.schema_of_response_reverse import Schema
from pydantic import BaseModel, ValidationError, Field

import pytest

from ..framework.constants import StatusCode
from .config.test_data import DataSearch, DataReverse

from .api import Search, Reverse


class TestTask3:

    @pytest.mark.skip
    @pytest.mark.parametrize("data", DataSearch.DATA)
    def test_request_to_get_list_of_search_and_check_on_model(self, data):
        response = Search().get_response_search(data)
        assert response.status == StatusCode.STATUS_200, \
            f"Server response is {response.status}, expected result is {StatusCode.STATUS_200}"
        Logger.info(f"url = {response.url}")
        Logger.info(f"{type(response.response)}")
        Logger.info(f"JSON = {response.response}")

        try:
            q = ResponseModel(response_model=response.response)
            Logger.info(f"Model = {q.json()}")
        except ValidationError as e:
            print(e)
            # print(e.json())

    @pytest.mark.need_review
    @pytest.mark.parametrize("data", DataReverse.DATA)
    def test_request_to_get_reverse(self, data):
        response = Reverse().get_response_reverse(data)
        assert response.status == StatusCode.STATUS_200, \
            f"Server response is {response.status}, expected result is {StatusCode.STATUS_200}"
        Logger.info(f"url = {response.url}")
        Logger.info(f"{type(response.response)}")
        Logger.info(f"JSON = {response.response}")

        try:
            q = Schema(**response.response)
            Logger.info(f"Model = {q.json()}")
        except ValidationError as e:
            print(e)
            # print(e.json())
