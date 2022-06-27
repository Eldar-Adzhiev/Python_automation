import requests

#  python -m pytest -s LearnQA_Python_API\ex12_header_method_test.py


def test_homework_headers():
    url = "https://playground.learnqa.ru/api/homework_header"

    response = requests.get(url)

    header_resp = response.headers
    print(header_resp)

    assert header_resp is not None, "Header is None"


