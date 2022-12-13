import json
import logging
import os
from json import JSONDecodeError
from urllib.parse import urljoin

import allure
import requests
from jsonschema import validate
from requests import HTTPError

from api import schemas

logger = logging.getLogger("test")


class AuthFailureException(HTTPError, AssertionError):
    pass


class RequestFailureException(HTTPError, AssertionError):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    @staticmethod
    def _logging_pre(url, headers, data, files, expected_status):
        text = f'Performing request:\n' \
               f'URL: {url}\n' \
               f'HEADERS: {headers}\n' \
               f'DATA: {data}\n\n' \
               f'FILES: {files}\n\n' \
               f'expected status: {expected_status}\n\n'

        allure.attach(text, 'request', attachment_type=allure.attachment_type.TEXT)
        logger.info(text)

    @staticmethod
    def _logging_post(response):
        try:
            data = json.dumps(response.json(), indent=4)
        except JSONDecodeError:
            data = response.text

        text = 'Got response:\n' \
              f'RESPONSE STATUS: {response.status_code}\n' \
              f'RESPONSE CONTENT: {data}\n\n'

        allure.attach(text, 'response', attachment_type=allure.attachment_type.TEXT)
        logger.info(text)

    def _request(self, method, location, headers=None, params=None, data=None, json_data=None, files=None,
                 check_schema=None, check_status=True, expect_status=200, jsonify=True):
        url = urljoin(self.base_url, location)
        logger.info('-' * 100 + '\n')

        self._logging_pre(url, headers, data or json_data, files, expect_status)
        response = self.session.request(method, url, headers=headers, params=params, data=data, json=json_data,
                                        files=files)

        self._logging_post(response)
        # check 4xx and 5xx
        if check_status:
            response.raise_for_status()

        # check expected status
        if expect_status and response.status_code != expect_status:
            raise RequestFailureException(f'Request {url} failed with [{response.status_code}]: {response.text}',
                                          response=response)

        # check schema
        if check_schema is not None:
            validate(instance=response.json(), schema=check_schema)

        if jsonify:
            return response.json()

        return response


    def post_user_auth(self, email, password):
        location = 'api/user/auth'
        data = {'email': email, 'password': password}

        response = self._request('POST', location, data=data, check_status=False, expect_status=0, jsonify=False,
                                 check_schema=schemas.LOGIN_SCHEMA)
        if response.status_code != 200:
            raise AuthFailureException(f'Authorization failed with [{response.status_code}]: {response.text}',
                                       response=response)

        return response.json()

    def get_chat_list(self):
        location = 'api/student/chat/list'
        return self._request('GET', location)

    def get_chat_dialogue(self, user_id):
        location = 'api/student/chat/dialogue'
        params = {'userId': user_id}

        return self._request('GET', location, params=params)

    def post_chat_send_message(self, chat_id, message='', filepath=None, detect_filetype=True):
        location = 'api/student/chat/send-message'

        files = {}
        filetype = ''

        if filepath is not None and os.path.exists(filepath):
            if detect_filetype and filepath.endswith('.png'):
                filetype = 'image'
                content_type = 'image/png'
            else:
                filetype = 'file'
                content_type = 'application/octet-stream'

            files['files[0]'] = (filepath, open(filepath, 'rb'), content_type)

        data = {'chatId': chat_id, 'message': message, 'fileType': filetype}

        return self._request('POST', location, data=data, files=files)

    def post_chat_delete_message(self, message_ids):
        location = 'api/student/chat/delete-messages'

        if not isinstance(message_ids, list):
            message_ids = [message_ids]

        data = {f'messageIds[{i}]': message for i, message in enumerate(message_ids)}
        return self._request('POST', location, data=data)
