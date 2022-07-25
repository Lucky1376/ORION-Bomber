import json
import time
import requests
from fake_useragent import UserAgent


class Send:
    def __init__(self, service):
        self.service = service
        self.service_data = None
        self.services = None
        self.time_out_ = {'apteka.ru': 0, 'magnit': 0, 'telegram': 0}
        self.time_out_config = {'apteka.ru': 120, 'magnit': 120, 'telegram': 120}

    def checktimeout(self, service):
        # now_time = time.time()
        time_out_ = self.time_out_
        time_out_config = self.time_out_config
        if time_out_[service] == 0:
            time_out_[service] = time.time()
            return True
        else:
            old_time = time_out_[service]
            now_time = time.time()
            try:
                if now_time - old_time >= time_out_config[service]:
                    time_out_[service] = time.time()
                    return True
                else:
                    return False
            except:
                print('error: что-то пошло не так (возможно в конфиге нету нужного сервиса)')
                return False


    # Обработка json для последующего спама
    def json_processing(self, phone):
        # Проверка страны
        if phone[1][:1] == '3':
            country = "by"
        else:
            country = "ru"

        # Загрузка json
        with open('tools/services.json') as f:
            services = json.load(f)
        # Получение сервисов по стране
        self.services = services[country][0]
        try:
            service = self.services[self.service]
        except: # Если нужного сервиса не оказалось в json
            return False
        self.service_data = service

        if "json" in service: # Если данные для запроса json
            payload = service["json"]
            datatype = 'json'
        elif "data" in service: # Если данные для запроса data
            payload = service["data"]
            datatype = 'data'
        else:
            payload = service["url"] # Если данные для запроса в url
            datatype = 'url'

        # Форматирование для России
        if country == 'ru':
            for old, new in {
                "#+phone#": phone[0],
                "#phone#": phone[1],
                "#phone8#": phone[2],
                "#phone()#": phone[3]
            }.items():
                if old in payload:
                    payload = payload.replace(old, new)
            return datatype, payload
        # Форматирование для беларуси
        elif country == 'by':
            for old, new in {
                "#+phone#": phone[0],
                "#phone#": phone[1],
                "#-phone#": phone[2]
            }.items():
                if old in payload:
                    payload = payload.replace(old, new)
            return datatype, payload

    # Функция для спама
    def spam(self, phone, proxy=None):
        if self.json_processing(phone) != False:
            datatype, payload = self.json_processing(phone)
        else: # Если сервиса нет в json
            return False

        # Дата сервиса
        service = self.service_data
        url = service["url"]

        # Генерируем headers
        ua = UserAgent().random
        try:
            service["headers"]["User-Agent"] = ua
            headers = service["headers"]
        except:
            headers = {"User-Agent": ua}

        session = requests.Session()
        request = requests.Request("POST", url)
        request.headers = headers

        # В зависимости от типа входных данных, добавляем их в запрос
        if datatype == "json":
            request.json = eval(payload)
        elif datatype == "data":
            request.data = eval(payload)
        elif datatype == "url":
            request.url = payload["url"]

        # Отправляем запрос
        try:
            request = request.prepare()
            r = session.send(request, timeout=10, proxies=proxy)
            return r.status_code
        except:
            return False
