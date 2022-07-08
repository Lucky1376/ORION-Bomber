import requests, tools, headers
from fake_useragent import UserAgent

ua = UserAgent()
ua = ua.random

number = tools.FormattingNumber("", "ru")[3]
headers = headers.headers["apteka.ru"]
result = requests.post("https://api.apteka.ru/Auth/Auth_Code?cityUrl=moskva", json={"phone":number, "u": "U"}, headers=headers, proxies=None)
print(result.status_code)
print(result.json())