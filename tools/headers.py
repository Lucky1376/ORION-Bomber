from fake_useragent import UserAgent

ua = UserAgent()
ua = ua.random

headers = {"apteka.ru":
		{
			"Accept": "*/*",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
			"Access-Control-Request-Headers": "authorization,content-type",
			"Access-Control-Request-Method": "POST",
			"Connection": "keep-alive",
			"Host": "api.apteka.ru",
			"Origin": "https://apteka.ru",
			"Referer": "https://apteka.ru/",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-site",
			"User-Agent": ua
		},
		   "magnit": {"User-Agent": ua}}