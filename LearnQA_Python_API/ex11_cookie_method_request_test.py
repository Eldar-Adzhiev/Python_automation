import requests

# python -m pytest -s LearnQA_Python_API\ex11_cookie_method_request_test.py


def test_homework_cookie():
    url = "https://playground.learnqa.ru/api/homework_cookie"

    response1 = requests.get(url)

    cookie = response1.cookies
    print(cookie)

    response2 = response1
    assert response2.cookies == cookie, "Cookie is invalid"
