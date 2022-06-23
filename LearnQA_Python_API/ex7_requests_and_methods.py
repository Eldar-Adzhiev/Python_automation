import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"



# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response_1 = requests.get(url)
print("Запрос без параметра method =", response_1.text)

# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response_2 = requests.head(url)
print("запрос не из списк =", response_2.text)

# Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response_3 = requests.post(url, data={"method": "POST"})
print("Запрос с правильным значением method =", response_3.text)

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
methods = ["GET", "POST", "PUT", "DELETE"]

for method in methods:
    for i in methods:
        # print(method, i)
        if method == "GET":
            response = requests.get(url, params={"method": i})
            if i == "GET" and response.text == "Wrong method provided":
                print(f"Сообщение при методе {method} и параметре {i} неверное {response.text}")
            elif i != "GET" and response.text == '{"success":"!"}':
                print(f"Сообщение при методе {method} и параметре {i} неверное {response.text}")
        elif method == "POST":
            response = requests.post(url, data={"method": i})
            if i == "POST" and response.text == "Wrong method provided":
                print(f"Сообщение при методе {method} и параметре {i} неверное {response.text}")
            elif i != "POST" and response.text == '{"success":"!"}':
                print(f"Сообщение при методе {method} и параметре {i} неверное {response.text}")
        elif method == "PUT":
            response = requests.put(url, data={"method": i})
            if i == "PUT" and response.text == "Wrong method provided":
                print(f"Сообщение при методе {method} и параметре {i} неверное {response.text}")
            elif i != "PUT" and response.text == '{"success":"!"}':
                print(f"Сообщение при методе {method} и параметре {i} неверное {response.text}")
        else:
            response = requests.delete(url, data={"method": i})
            if i == "DELETE" and response.text == "Wrong method provided":
                print(f"Сообщение при методе {method} и параметре {i} неверное {response.text}")
            elif i != "DELETE" and response.text == '{"success":"!"}':
                print(f"Сообщение при методе {method} и параметре {i} неверное {response.text}")

# ====================================================================================================
# Более короткий способ
print('================================================================================================')

for request_method in methods:
    for params_method in methods:
        if request_method == "GET":
            response = requests.request(method=request_method, url=url, params={"method": params_method})
        else:
            response = requests.request(method=request_method, url=url, data={"method": params_method})

        if request_method == params_method and response.text != '{"success":"!"}':
            print(f"При методе {request_method} и параметре {params_method}")
            print('Ожидается такое: {"success":"!"}')
            print('А получается вот так: Wrong method provided' )
        elif request_method != params_method and response.text == '{"success":"!"}':
            print(f"При методе {request_method} и параметре {params_method}")
            print('Ожидается такое: Wrong method provided' )
            print('А получается вот так: {"success":"!"}')






