import os
import uuid

import pytest

from requests import HTTPError

from api.client import ApiClient, AuthFailureException
from api.suite.base import BaseAPISuiteTest
from utils.builder import LocationBuilder
from utils.datamanager import DataManager
from utils.decorators import wait


class TestChat(BaseAPISuiteTest):

    def test_get_chat_list(self):
        teachers_list = ["DevDivision", "Илья Кириллов", "Александр Краснов"]
        for teacher in teachers_list:
            assert self.get_chat_teacher(teacher), f'{teacher} not found in teachers'

    def test_empty_teacher_dialogue(self):
        teacher = "Александр Краснов"
        messages = self.get_teacher_dialogue(teacher)['messages']
        assert not messages

    def test_no_such_teacher_dialogue(self):
        with pytest.raises(HTTPError) as exc:
            self.api_client.get_chat_dialogue(66666666666666666666666666666666)

        assert exc.value.response.status_code == 400
        assert exc.value.response.json() == {'RECIPIENT_NOT_FOUND': 'Собеседник не найден'}

    def test_get_teacher_dialogue(self):
        teacher = "Илья Кириллов"
        dialogue = self.get_teacher_dialogue(teacher)
        assert dialogue['messages']

    def test_send_message(self):
        teacher = "Илья Кириллов"
        message = str(uuid.uuid4())

        chat_id = self.get_teacher_dialogue(teacher)['id']
        self.api_client.post_chat_send_message(chat_id, message)

        assert self.check_message(teacher, message)

    @pytest.mark.parametrize('c', (1, 10), ids=lambda x: f'count={x}')
    def test_delete_message(self, c):
        teacher = "Илья Кириллов"
        chat_id = self.get_teacher_dialogue(teacher)['id']

        messages = []
        message_ids = []

        for i in range(c):
            message = str(uuid.uuid4())
            messages.append(message)
            message_id = self.api_client.post_chat_send_message(chat_id, message)['id']
            message_ids.append(message_id)

        self.api_client.post_chat_delete_message(message_ids)
        for m in messages:
            assert not self.check_message(teacher, m)

    def test_send_generated_image(self):
        self.teacher = "Илья Кириллов"
        image, path = self.data_manager.image(width=500, height=1000)

        chat_id = self.get_teacher_dialogue(self.teacher)['id']
        self.api_client.post_chat_send_message(chat_id, filepath=path)


class TestUploadFile(BaseAPISuiteTest):
    detect_filetype = True

    def _check_message(self):
        message = self.get_teacher_dialogue(self.teacher)['messages'][0]
        assert message
        assert message['files'][0]['file']['name'] == self.file
        self._check_filetype(message)

    def _check_filetype(self, message):
        assert message['fileType'] == self.filetype

    @pytest.mark.parametrize('file, filetype', [('image.png', 'image'), ('file.txt', 'file')])
    def test_send_file(self, repo_root, file, filetype):
        filepath = os.path.join(repo_root, 'resources', file)

        self.teacher = "Илья Кириллов"
        self.file = file
        self.filetype = filetype

        chat_id = self.get_teacher_dialogue(self.teacher)['id']
        self.api_client.post_chat_send_message(chat_id, filepath=filepath, detect_filetype=self.detect_filetype)

        wait(self._check_message, timeout=10, interval=1)


class TestUploadFileWithoutFileDetection(TestUploadFile):
    detect_filetype = False

    def _check_filetype(self, message):
        pass

    def _check_message(self):
        super(TestUploadFileWithoutFileDetection, self)._check_message()

        message = self.get_teacher_dialogue(self.teacher)['messages'][0]
        assert message['fileType'] == 'file'



class TestData(BaseAPISuiteTest):

    def test_data_inside(self):
        user = self.data_manager.user()
        print(user)


    @pytest.fixture
    def user_test(self):
        user = self.data_manager.user()
        # some code to create user in APP
        yield user
        # some code to delete user in APP

    def test_data_outside(self, user_test):
        print(user_test)


    @pytest.mark.parametrize('u', [
        DataManager.user(email=''),
        DataManager.user(email='123'),
        DataManager.user(email='123@'),
        DataManager.user(email='123@123'),
        DataManager.user(email='@123'),
    ])
    def test_data_driven_invalid(self, u):
        print(u.email)
        # some action with user data

    def test_builder_data(self):
        location = LocationBuilder().with_city('Moscow').with_zipcode(11111).with_country('Russia').with_building(123)
        location.with_zipcode(22222)
        user = self.data_manager.user(bio=location.build())
        print(user.bio)
        print(location.zipcode)


class TestSoup(BaseAPISuiteTest):

    def test_raw_data(self):
        content = self.api_client._request('GET', self.base_url, check_status=False, jsonify=False).text

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        print(soup.title)
        print(soup.img)
        print(soup.img['src'])
        print(soup.find_all('div'))
        print(soup.div.img)



class TestNegativeRequest(BaseAPISuiteTest):

    def test_negative(self):
        client = ApiClient(self.base_url)
        with pytest.raises(AuthFailureException) as exc:
            client.post_user_auth('66666666666666666666666666666666', '123187637812637812637821678312')

        assert exc.value.response.status_code == 400
        assert exc.value.response.json() == {"INVALID_EMAIL": "INVALID_EMAIL"}

    def test_negative2(self):
        client = ApiClient(self.base_url)
        client.post_user_auth('66666666666666666666666666666666', '123187637812637812637821678312')