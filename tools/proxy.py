import requests, random, threading as th
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent as UA
from progress.bar import ChargingBar

def SPC(ip, port, login=None, password=None):
    ua = UA().random
    ipp = ip + ':' + port
    #proxy_https = {'http': 'http://' + ipp,
    #               'https': 'http://' + ipp}
    proxy_http = {'http': 'http://' + ipp}

    ip_user = requests.get("http://icanhazip.com/", headers={'User-Agent': ua}).text
    if login == None and password == None: # проверка публичных прокси
        #try:
        #    ip_proxy = requests.get("http://icanhazip.com/", headers={'User-Agent': ua}, proxies=proxy_https, timeout=5)
        #    if ip_user not in ip_proxy.text and ip_proxy.status_code == 200:
        #        return proxy_https
        #    else:
        #        return False                                                            #кирилл лох
        #except:
        try:
            ip_proxy = requests.get("http://icanhazip.com/", headers={'User-Agent': ua}, proxies=proxy_http, timeout=5)
            if ip_user not in ip_proxy.text and ip_proxy.status_code == 200:
                return proxy_http
            else:
                return False
        except:
            return False
    else: #checking private proxies
        proxy_private_https = {'http': 'http://' + login + ':' + password + '@' + ip + ':' + port,
                               'https': 'http://' + login + ':' + password + '@' + ip + ':' + port}
        proxy_private_http = {'http': 'http://' + login + ':' + password + '@' + ip + ':' + port}
        try:
            ip_proxy = requests.get("http://icanhazip.com/", headers={'User-Agent': ua}, proxies=proxy_private_https,
                             timeout=5)
            if ip_user not in ip_proxy.text and ip_proxy.status_code == 200:
                return proxy_private_https
            else:
                return False
        except:
            try:
                ip_proxy = requests.get("http://icanhazip.com/", headers={'User-Agent': ua}, proxies=proxy_private_http,
                                 timeout=5)
                if ip_user not in ip_proxy.text and ip_proxy.status_code == 200:
                    return proxy_private_http
                else:
                    return False
            except:
                return False

class Proxy:
	def __init__(self, country=["ru", "by", "ua", "us"], unknown=False, timeout=15):
		# Checking for Errors in Parameters
		# -----------------------------------------------
		if len(country) < 1:
			print("Не указаны страны")
			exit()
		else:
			for ct in country:
				if ct not in ["ru", "by", "ua", "us"]:
					print(f"{ct} - неизвестная страна")
					exit()
		if unknown not in [False, True]:
			print("Неизвестный параметр для unknown")
			exit()
		try:
			timeout = int(timeout)
		except:
			print("Параметр timeout возможно указан как строка")
			exit()
		if timeout < 10 or timeout > 15:
			print("timeout не может быть меньше 10 или больше 15 секунд")
			exit()
		# -----------------------------------------------
		self.unknown = unknown
		self.country = country
		self.timeout = timeout
		self.list = {}
		self.list_2 = {}
		self.list_3 = {}
		self.list_4 = {}

	def mix(self):
		if self.list == {}:
			return False
		else:
			new_itog = {"all": []}
			for ct in self.list:
				for pr in self.list[ct]:
					new_itog["all"].append(pr)
			return new_itog


	def random(self, country=False, delete_el=False, sp=None):
		if country != False and country not in self.country:
			return False
		if self.list == {}:
			return False
		if country == False:
			key = random.choice(self.country)
			pr = random.choice(self.list[key])
		else:
			key = country
			pr = random.choice(self.list[country])

		if delete_el == True:
			self.list[key].remove(pr)

		return pr

	def verify(self):
		if self.list == {}:
			print("Список прокси пустой")
			return
		else:
			# Progress bar
			pr_b = []
			for key in self.list:
				for i in range(len(self.list[key])):
					pr_b.append(i)
			bar = ChargingBar('Проверка', max = len(pr_b))

		new_list = {}

		def vrf_th(key, ip, port):
			a = SPC(ip, port)
			bar.next()
			if a != False:
				if key not in new_list:
					new_list[key] = []
				new_list[key].append({"ip": ip,
									  "port": port,
									  "format": a})

		threads = []

		for key in self.list:
			for pr in self.list[key]:
				t = th.Thread(target=vrf_th, args=(key, pr["ip"], pr["port"],))
				threads.append(t)

		for i in range(len(threads)):
			threads[i].start()

		for i in range(len(threads)):
			threads[i].join()

		self.list = new_list


	def get(self):
		# Progress bar
		pr_b = [1, 2, 3, 4]
		bar = ChargingBar('Парсинг', max = len(pr_b))

		# User-Agent
		ua = UA()

		# Summary sheet with proxy
		itog = {}

		# https://hidemy.name
		# -----------------------------------------------
		"""Composing url Addresses for 1 service"""
		url_list = {}
		for ct in self.country:
			url_list[ct] = f"https://hidemy.name/ru/proxy-list/?country={ct.upper()}&type=hs#list"
		"""Parsing"""
		for ct in url_list:
			can = False
			try:
				response = requests.get(url_list[ct], headers={"User-Agent": ua.random}, timeout=self.timeout)
				can = True
			except:
				pass
			if response.status_code == 200 or can == True:
				itog[ct] = []

				html = BS(response.content, "html.parser")

				all_list_bs = html.find("div", class_="table_block").find("tbody")

				pred_itog = []
				for tr in all_list_bs:
					for td in tr:
						try:
							pred_itog.append(td.text.replace(" ", ""))
						except:
							continue
					if len(pred_itog) > 0:
						itog[ct].append({"ip": pred_itog[0],
										 "port": pred_itog[1]})
					pred_itog = []
		self.list = itog
		bar.next()
		# -----------------------------------------------

		itog_2 = {}

		# https://free-proxy-list.net
		# -----------------------------------------------
		can = False
		try:
			response = requests.get("https://www.sslproxies.org", headers={"User-Agent": ua.random}, timeout=self.timeout)
			can = True
		except:
			pass
		if response.status_code == 200 or can == True:
			"""Парсинг"""
			html = BS(response.content, "html.parser")

			all_list_bs = html.find("div", "table-responsive fpl-list").find("tbody")

			pred_itog = []
			for tr in all_list_bs:
				for td in tr:
					pred_itog.append(td.text.strip())
				#print(pred_itog[2].lower())
				if pred_itog[2].lower() not in self.country:
					pred_itog = []
					continue
				if pred_itog[2].lower() in itog_2:
					itog_2[pred_itog[2].lower()].append({"ip": pred_itog[0],
														 "port": pred_itog[1]})
				else:
					itog_2[pred_itog[2].lower()] = []
					itog_2[pred_itog[2].lower()].append({"ip": pred_itog[0],
														 "port": pred_itog[1]})
				pred_itog = []
		self.list_2 = itog_2
		bar.next()
		# -----------------------------------------------

		itog_3 = {"unk":[]}

		# https://proxyscrape.com
		# -----------------------------------------------
		if self.unknown == True:
			can = False
			try:
				response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all", headers={"User-Agent": ua.random}, timeout=self.timeout)
				can = True
			except:
				pass
			if response.status_code == 200 or can == True:
				a = response.text.split("\n")
				a.remove("")
				for i in a:
					ip = i.replace("\r", "").split(":")[0]
					port = i.replace("\r", "").split(":")[1]
					itog_3["unk"].append({"ip": ip,
										  "port": port})
			self.list_3 = itog_3
		bar.next()
		# -----------------------------------------------

		itog_4 = {}

		# https://proxylist.geonode.com
		# -----------------------------------------------
		"""Counting the number of pages on the service"""
		col_page = 1
		can = False
		try:
			result = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&speed=medium&protocols=http%2Chttps", headers={"User-Agent": ua.random}, timeout=self.timeout)
			can = True
		except:
			pass
		if can == True:
			if result.json()["total"] / 50 > result.json()["total"] // 50:
				col_page += result.json()["total"] // 50 + 1
			else:
				col_page += result.json()["total"] // 50
		
		"""Парсинг"""
		if can == True:
			i = 1
			while i < col_page:
				try:
					response = requests.get(f"https://proxylist.geonode.com/api/proxy-list?limit=50&page={i}&sort_by=lastChecked&sort_type=desc&speed=medium&protocols=http%2Chttps", headers={"User-Agent": ua.random}, timeout=15)
					if response.status_code == 200:
						for pr in response.json()["data"]:
							ip = pr["ip"]
							port = pr["port"]
							ct = pr["country"].lower()
							if ct in self.country:
								if ct in itog_4:
									itog_4[ct].append({"ip": ip,
													   "port": port})
								else:
									itog_4[ct] = []
									itog_4[ct].append({"ip": ip,
													   "port": port})
					i+=1
				except:
					i+=1
			try:
				self.list_4 = itog_4
				bar.next()
				bar.finish()
			except:
				bar.next()
				bar.finish()
		# -----------------------------------------------


		# -----------------------------------------------
		"""Formation into one dictionary"""
		l1 = self.list

		def formation(dict):
			for key in dict:
				if len(dict[key]) < 1:
					continue
				else:
					for pr in dict[key]:
						if key not in l1:
							l1[key] = []
						if pr not in l1[key]:
							l1[key].append(pr)

		if self.list_2 != {}:
			formation(self.list_2)
		if self.list_3 != {}:
			formation(self.list_3)
		if self.list_4 != {}:
			formation(self.list_4)

		self.list = l1
		# -----------------------------------------------