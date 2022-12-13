import logging

import allure
import pytest

from api.client import ApiClient
from utils.datamanager import DataManager


class BaseAPISuiteTest:

    base_url: str
    logger: logging.Logger
    api_client: ApiClient

    @pytest.fixture(autouse=True)
    def prepare(self, base_url, api_client, logger, test_dir):
        self.base_url: str = base_url
        self.logger: logging.Logger = logger

        self.data_manager = DataManager(test_dir)
        self.api_client: ApiClient = api_client

        self.logger.info('PREPARE DONE')

    @allure.step
    def get_chat_teacher(self, teacher_name):
        chat_list = self.api_client.get_chat_list()

        for teacher in chat_list['teachers']:
            if teacher['name'] == teacher_name:
                return teacher
        return {}

    @allure.step
    def get_teacher_dialogue(self, teacher_name):
        teacher = self.get_chat_teacher(teacher_name)
        if not teacher:
            pytest.fail(f'No such teacher {teacher_name}')

        return self.api_client.get_chat_dialogue(teacher['id'])

    @allure.step
    def check_message(self, teacher_name, message_text):
        messages = self.get_teacher_dialogue(teacher_name)['messages']
        return any(m for m in messages if m['text'] == message_text)
