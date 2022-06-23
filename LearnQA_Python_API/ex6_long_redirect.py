import requests

url = "https://playground.learnqa.ru/api/long_redirect"

response = requests.get(url)
final_response = response

print(len(response.history))
print(final_response.url)
