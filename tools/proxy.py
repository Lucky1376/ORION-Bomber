import requests as r
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import os
#os.system("cls")

def GetProxyList(country="all", type_="all"):
	url_type = ""
	if country == "all":
		country = ["ru", "ca", "by", "kz", "de", "es", "uk"]
		country_list_service_2_3 = ['ru', 'ca', 'by', 'kz', 'de', 'es', 'uk', 'gb', 'us', 'nl', 'jp', 'unk', 'sg', 'hk', 'co', 'br', 'dk', 'do', 'uz', 'fr', 'ec', 'se', 'it', 'tw', 'hn', 'at', 'mx', 'in', 'kr', 'fi', 'cn', 'eg', 'ro', 'si', 'rs', 'sa', 'ps', 'pl', 'sr', 'ua']
	else:
		country_list_service_2_3 = country
	if type_ == "all":
		type_ = ["http", "https"]
		url_type = "hs"
	elif type_ == "http":
		url_type = "h"
	elif type_ == "https":
		url_type = "s"

	ua = UserAgent()
	ua = ua.random

	itog = {}

	# Service 1
	country_url = {"ru": "https://hidemy.name/ru/proxy-list/?country=RU&type="+url_type+"#list", # Россия
				   "ca": "https://hidemy.name/ru/proxy-list/?country=CA&type="+url_type+"#list", # Канада
				   "by": "https://hidemy.name/ru/proxy-list/?country=BY&type="+url_type+"#list", # Беларусь
				   "kz": "https://hidemy.name/ru/proxy-list/?country=KZ&type="+url_type+"#list", # Казахстан
				   "de": "https://hidemy.name/ru/proxy-list/?country=DE&type="+url_type+"#list", # Германия
				   "es": "https://hidemy.name/ru/proxy-list/?country=ES&type="+url_type+"#list", # Испания
				   "uk": "https://hidemy.name/ru/proxy-list/?country=UA&type="+url_type+"#list"} # Украина
	for ct in country:
		if ct not in country_url:
			continue
		itog[ct] = []
		result = r.get(country_url[ct], headers={'User-Agent': ua})
		html = bs(result.content, "lxml")

		all_proxy = html.find("div", class_="table_block").find("tbody")

		pred_itog = []
		for tr in all_proxy:
			for td in tr:
				try:
					pred_itog.append(td.text.replace(" ", ""))
				except:
					continue
			if len(pred_itog) > 0:
				itog[ct].append({"ip": pred_itog[0],
								 "port": pred_itog[1],
								 "type": pred_itog[4]})
			pred_itog = []

	# Service 2
	format_ = "json"
	if type_ == ['http', 'https']:
		type_s = "http,https"
	else:
		type_s = type_
	limit = "20"

	result = r.get(f"https://www.proxyscan.io/api/proxy?&format=json&format={format_}&type={type_s}&limit={limit}")
	for i in result.json():
		ip = i["Ip"]
		port = i["Port"]
		country_s = i["Location"]["countryCode"]
		if len(country_s) < 1:
			country_s = "us"
		if country_s.lower() not in country_list_service_2_3:
			continue
		type_ss = i["Type"]
		
		if len(type_) == 1:
			type_ss = type_ss[0]
		else:
			try:
				type_ss = type_ss[0]+","+type_ss[1]
			except:
				pass

		if country_s.lower() not in itog:
			itog[country_s.lower()] = []

		itog[country_s.lower()].append({"ip": ip,
									  "port": port,
									  "type": type_ss})

	# Service 3
	type_slovar = {"hs": "HTTP,HTTPS",
				   "h": "HTTP",
				   "s": "HTTPS"}

	result = r.get("https://www.sslproxies.org", headers={"User-Agent": ua})
	html = bs(result.content, "lxml")
	table = html.find_all("tbody")[0]

	for i in table:
		proxy_sp = []
		for j in i:
			proxy_sp.append(j.text.replace(" ", ""))
		if proxy_sp[2].lower() not in country_list_service_2_3:
			proxy_sp = []
			continue
		if proxy_sp[2].lower() in itog:
			itog[proxy_sp[2].lower()].append({"ip": proxy_sp[0],
											  "port": proxy_sp[1],
											  "type": type_slovar[url_type]})
		else:
			itog[proxy_sp[2].lower()] = []
			itog[proxy_sp[2].lower()].append({"ip": proxy_sp[0],
											  "port": proxy_sp[1],
											  "type": type_slovar[url_type]})
		proxy_sp = []

	# Обработка итогового словаря на повторы
	itog_2 = {}
	for key in itog:
		itog_2[key] = []
		for pr in itog[key]:
			if pr in itog_2[key]:
				continue
			else:
				itog_2[key].append(pr)

	return itog_2

def CheckingTheProxyList(proxys): # BETA TEST
	itog = {}

	for ct in proxys:
		if len(proxys[ct]) < 1:
			continue
		else:
			itog[ct] = []

			proxy_sp = proxys[ct]
			for proxy in proxy_sp:
				ua = UserAgent()
				ua = ua.random

				ip = proxy["ip"]
				port = proxy["port"]
				type_ = proxy["type"]

				if type_ == "HTTP,HTTPS":
					proxy_get = {"http://": ip+":"+port,
								 "https://": ip+":"+port}
				else:
					proxy_get = {type_.lower()+"://": ip+":"+port,}

				result = r.get("https://google.com", proxies=proxy_get, headers={'User-Agent': ua})
				if result.status_code == r.codes["ok"]:
					itog[ct].append({"ip": ip,
									 "port": port,
									 "type": type_})
				else:
					continue
	return itog

def CheckingTheProxy(dict): # BETA TEST
	ua = UserAgent()
	ua = ua.random

	result = r.get("https://google.com", proxies=dict, headers={'User-Agent': ua})

	if result.status_code == r.codes["ok"]:
		return True # Прокси работает
	else:
		return False # Прокси не работает

def FormattingProxy(dict=None, ip=None, port=None, type_=None): # BETA TEST
	if dict != None:
		try:
			ip = dict["ip"]
			port = dict["port"]
			type_ = dict["type"]
		except:
			return False, "ERROR in specifying dictionary elements" # При ошибке указания элементов словаря
	elif ip != None and port != None and type_ != None:
		pass
	else:
		return False, "NO parameters are specified"

	proxy_get = {"http://": ip+":"+port,
				 "https://": ip+":"+port}
	
	return True, proxy_get