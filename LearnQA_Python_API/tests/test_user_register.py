from LearnQA_Python_API.lib.my_requests import MyRequests
from LearnQA_Python_API.lib.base_case import BaseCase
from LearnQA_Python_API.lib.assertions import Assertions

class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"

        data = self.prepare_registration_data(email)

        response = MyRequests.post("/api/user/", data=data)

        print(response.status_code)
        print(response.content)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email 'vinkotov@example.com' already exists"


