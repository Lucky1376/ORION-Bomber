# Инструменты для разных обработок

from termcolor import colored


def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # Для России
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
	elif country == "by": # Для Балуруси
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]

	if country == "by":
		return numb_1, numb_2, numb_3
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4

def FormattingResponse(response):
	try:
		code = (response.status_code)
	except:
		code = int(response)

	SUCCESS = {200: ("OK", "good", "green"),
			   204: ("OK", "no content", "green"),}

	FAIL_USER = {404: ("FAIL_USER", "not found", "red"),
				 423: ("FAIL_USER", "locked ip", "red"),
				 400: ("FAIL_USER", "bad requests", "red"),
				 429: ("FAIL_USER", "too many requests", "red"),
				 403: ("FAIL_USER", "forbidden", "red")}

	FAIL_SERVER = {500: ("FAIL_SERVER", "internal server error", "red"),
				   503: ("FAIL_SERVER", "service unavailable", "red"),
				   504: ("FAIL_SERVER", "timeout", "red")}

	if code in SUCCESS:
		return SUCCESS[code]
	elif code in FAIL_USER:
		return FAIL_USER[code]
	elif code in FAIL_SERVER:
		return FAIL_SERVER[code]
	else:
		return None