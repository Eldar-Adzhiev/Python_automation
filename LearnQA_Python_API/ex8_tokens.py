import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1. создавал задачу
create_job = requests.get(url)
pars_response = create_job.json()
token = pars_response["token"]
sec = pars_response["seconds"]

# 2. делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
response_2 = requests.get(url, params={"token": token})
print(response_2.text)

# 3. ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
print(sec)
time.sleep(sec)

# 4. делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
response_3 = requests.get(url, params={"token": token})
print(response_3.text)


