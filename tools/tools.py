# -*- coding: utf-8 -*-

# Tools for different processing

from termcolor import colored
from datetime import datetime
import requests as r, os, time, random, shutil, zipfile, webbrowser, traceback
from sys import platform
from tools import proxy
from progress.bar import ChargingBar
from tools import sender as send

def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # For Russia
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_11 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_11 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_5 = numb[:2] + " " + numb[2:5] + " " + numb[5:8] + " " + numb[8:10] + " " + numb[10:]
			numb_6 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " - " + numb[8:10] + " - " + numb[10:]
			numb_7 = numb[:2] + " ("+numb[2:]
			numb_8 = numb[2:]
			numb_9 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + " " + numb[8:10] + numb[10:]
			numb_10 = numb[:2] + ' ' + numb[2:5] + ' ' + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
			numb_11 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:]
	elif country == "by": # For Belarus
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
			numb_4 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] + '-' + numb[9:11] + '-' + numb[11:13]
			numb_5 = numb[:4] + ' (' + numb[4:6] + ") " + numb[6:9] +numb[9:11] +numb[11:13]
			numb_6 = numb[:4] + ' ' + numb[4:6] + " " + numb[6:9] + ' ' + numb[9:11] + ' ' + numb[11:13]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]
			numb_4 = '+' + numb[:3] + ' (' + numb[3:5] + ") " + numb[5:8] + '-' + numb[8:10] + '-' + numb[10:12]
			numb_5 = numb_1[:4] + ' (' + numb_1[4:6] + ") " + numb_1[6:9] +numb_1[9:11] +numb_1[11:13]
			numb_6 = numb_1[:4] + ' ' + numb_1[4:6] + " " + numb_1[6:9] + ' ' + numb_1[9:11] + ' ' + numb_1[11:13]
	if country == "by":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6, numb_7, numb_8, numb_9, numb_10, numb_11

def clear():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		print(colored("\nИзвините наша программа не поддерживает вашу операционную систему ;(\n", "red"))
		exit()

def anim_text(text, speed, color="green"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def RCT(text):
	last_color = None
	colors = ["green", "yellow", "red", "magenta", "blue"]
	new_text = ""
	for i in str(text):
		new_color = random.choice(colors)
		while new_color == last_color:
			new_color = random.choice(colors)
		new_text += colored(i, new_color)
	return new_text

def banner():
	a = open("tools/version.txt", "r")
	ver = a.read().split("\n")[0]
	a.close()

	ru_s = str(len(send.services_list))
	by_s = str(len(send.services_list_by))

	banner = colored("""

	 ▒█████   ██▀███   ██▓ ▒█████   ███▄    █ 
	▒██▒  ██▒▓██ ▒ ██▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
	▒██░  ██▒▓██ ░▄█ ▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
	▒██   ██░▒██▀▀█▄  ░██░▒██   ██░▓██▒  ▐▌██▒
	░ ████▓▒░░██▓ ▒██▒░██░░ ████▓▒░▒██░   ▓██░
	░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
	  ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
	░ ░ ░ ▒    ░░   ░  ▒ ░░ ░ ░ ▒     ░   ░ ░ 
	    ░ ░     ░      ░      ░ ░           ░ """, "red")

	pred_info = " "*24+colored("Сервисы", "green")+"\n"
	pred_info_ru = " "*17+colored("Россия ", "blue")+colored(ru_s, "green")+"   "
	pred_info_by = colored("Беларусь ", "cyan")+colored(by_s, "green")+"\n"
	pred_info = pred_info+pred_info_ru+pred_info_by

	info = " "*13+colored("[", "blue")+"Developers :"+colored("rizza", "green")+" and "+colored("LostIk", "red")
	info_2 = " "*13+colored("[", "blue")+"Version    :"+colored(ver, "red")
	info_3 = " "*13+colored("[", "blue")+"Telegram   :"+colored("@orionbomber", "cyan")+colored("   <--", "green")
	info_4 = "\n"+" "*12+colored("Программа больше не поддерживается!", "red")+"\n"

	print(banner)
	print(pred_info)
	print(info)
	print(info_2)
	print(info_3)
	print(info_4)

def banner_tools():
	print(colored("[1]", "red"), colored("Начать спам", "green"))
	print(colored("[2]", "red"), colored("Поддержать разработчиков!    <---", "green"))
	print(colored("[3]", "red"), colored("Android приложение", "magenta"))
	#print(colored("[3]", "red"), colored("Инструкция по отправке логов", "yellow"))
	#print(colored("[4]", "red"), colored("Попробуй", "green"), colored("в", "yellow"), colored("Telegram", "cyan")+colored("!", "yellow"), colored("   <---", "cyan"))
	print(colored("\n[99]", "red"), colored("Информация", "cyan"))
	print(colored("\n[0] Выход", "red"))

def donate():
	print("")
	print(colored("Спасибо за использование программы :D", "green"))
	print("")
	print(colored("QIWI", "yellow"))
	print("├"+colored("https://qiwi.com/n/LUCKY1376", "cyan"), colored("Перевод по никнейму", "green"))
	print("└"+colored("2200 7302 4344 6206", "cyan"), colored("MIR", "green"))
	#print("└"+colored("4890 4947 5754 5546", "cyan"), colored("VISA", "blue"))
	print("")
	print(colored("Сбербанк", "green"))
	print("└"+colored("2202 2024 3331 7181", "cyan"), colored("MIR", "green"))
	#print("└"+colored("5469 4500 1265 2996", "cyan"), colored("MasterCard", "red"))
	#print("")
	##print(colored("Юмани", "blue"))
	#print("├"+colored("4100 1174 8743 5875", "cyan"), "Номер счета")
	#print("└"+colored("2202 1201 0852 7850", "cyan"), colored("MIR", "green"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Файлы", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("были сохранены в папку Download на вашем устройстве", "green"))
			print(colored("Пожалуйста отправьте поочередно эти 2 файла в наш чат телеграм", "green"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"))
			print("")
			print("\nНажмите Enter чтобы вернуться назад")
			input()
		elif platform == "win32" or platform == "darwin":
			print("")
			print(colored("Пожалуйста отправьте в наш чат телеграм", "green"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"), colored("поочередно файлы", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("из папки", "green"), colored("tools", "cyan"))
			print("")
			print("\nНажмите Enter чтобы вернуться назад")
			input()
	except:
		print("")
		print(colored("Мы не смогли переместить файлы в нужную директорию", "yellow"))
		print(colored("Возможно у вас для Термукса в настройках разрешения приложению не доступны Файлы и медиаконтент", "yellow"))
		print(colored("Пожалуйста разрешите Термуксу в настройках все нужные разрешения и повторите попытку"))
		print(colored("За помощью по данному вопросу пишите в наш чат телеграм"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"))
		print("")
		print("\nНажмите Enter чтобы вернуться назад")
		input()

def clear_logs():
	with open("tools/logs.txt", "w"):
		pass
	with open("tools/error_logs.txt", "w"):
		pass
	print("")
	print(colored("Логи успешно были очищены", "green"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def banner_info():
	print(colored("\nТелеграм", "cyan"))
	print("├"+colored("rizza", "green")+":", colored("https://t.me/rlzza", "cyan"))
	print("├"+colored("LostIk", "red")+":", colored("https://t.me/lolzby", "cyan"))
	print("├"+colored("Android APK", "magenta")+":", colored("https://t.me/orion_cloud_bot", "cyan"))
	print("└"+colored("Канал", "cyan")+":", colored("https://t.me/orionbomber", "cyan"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def number_ckeck(numb):
	if len(numb) == 9 or len(numb) == 10:
		sp_numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		for i in str(numb):
			try:
				int(i)
			except:
				return False
		return True
	else:
		return False

def start_input():
	country_code = {"1": "+375",
					"2": "+7"}
	country_code_2 = {"1": "by",
					  "2": "ru"}
	clear()
	while True:
		print(colored("[99] Отмена", "red"))
		print("")
		print(colored("[1]", "red"), colored("Беларусь +375", "blue"))
		print(colored("[2]", "red"), colored("Россия +7", "cyan"))
		print("")
		ct = input(colored("Выберите страну: ", "green"))
		if ct == "2":
			break
		elif ct == "1":
			break
		elif ct == "99":
			return 0, 0, 0
		else:
			clear()
			print(colored("Новая страна", "magenta"), colored(ct, "cyan")+colored("!", "magenta"))
			print()
	clear()
	while True:
		print(colored("[99] Отмена", "red"))
		print()
		numb = input(colored("Введите номер без кода страны "+country_code[ct]+" ", "green"))
		if number_ckeck(numb):
			break
		else:
			clear()
			print(colored("Не очень похоже на номер телефона...", "magenta"))
			print()
		if numb == "99":
			return 0, 0, 0
	clear()
	while True:
		print(colored("[99] Отмена", "red"))
		print()
		print(colored("[1]", "red"), colored("Да", "green"))
		print(colored("[2]", "red"), colored("Нет", "red"))
		print()
		pr = input(colored("Использовать прокси?: ", "green"))
		if pr in ["1", "2"]:
			if pr == "1":
				pr = country_code_2[ct]
			else:
				pr = None
			break
		elif pr == "99":
			return 0, 0, 0
		else:
			clear()
			print(colored("Выбери один из вариантов...", "magenta"))
			print()
	clear()
	if pr != None:
		while True:
			print(colored("[99] Отмена", "red"))
			print()
			print(colored("[1]", "red"), colored("Общедоступный прокси", "yellow"))
			print("└"+colored("Общедоступный прокси используют все пользователи ORION-Bomber", "cyan"))
			print()
			print(colored("[2]", "red"), colored("Свой прокси", "green"))
			print("└"+colored("Ваш прокси обязательно должен иметь протокол HTTP или HTTPS с поддержкой ipv4 и страну вашего номера", "cyan"))
			print()
			who_pr = input("Вариант: ")
			if who_pr in ["1", "2"]:
				if who_pr == "2":
					print()
					print(colored("[99] Отмена", "red"))
					print()
					print(colored("Введите Ip и Port и логин и пароль если прокси частный", "green"))
					print("└"+colored("Пример:\n├123.45.678.910:8080\n└123.45.678.910:8080:LOGIN:PASSWORD", "cyan"))
					print()
					new_pr = input(colored("~# ", "red"))
					
					if new_pr == "99":
						return 0, 0, 0
					elif len(new_pr.split(":")) < 3:
						# Shared Proxy Check
						result = proxy.SPC(new_pr.split(":")[0], new_pr.split(":")[1])
						if result == False:
							print(colored("Ваш прокси не работает!", "red"))
						else:
							pr = {"ip": new_pr.split(":")[0],
								  "port": new_pr.split(":")[1],
								  "format": result}
							print(colored("Прокси работает!", "green"))
							time.sleep(2)
							break
					elif len(new_pr.split(":")) > 2:
						# Private Proxy Check
						result = proxy.SPC(new_pr.split(":")[0], new_pr.split(":")[1], login=new_pr.split(":")[2], password=new_pr.split(":")[3])
						if result == False:
							print(colored("Ваш прокси не работает!", "red"))
						else:
							pr = {"ip": new_pr.split(":")[0],
								  "port": new_pr.split(":")[1],
								  "login": new_pr.split(":")[2],
								  "password": new_pr.split(":")[3],
								  "format": result}
							print(colored("Прокси работает!", "green"))
							time.sleep(2)
							break

				else:
					break
			elif who_pr == "99":
				return 0, 0, 0
			else:
				clear()
				print(colored("К сожалению придется выбрать а не писать", "magenta"), colored(who_pr, "cyan"))
				print()

	return country_code[ct]+numb, country_code_2[ct], pr

def ICC():
	try:
		anim_text("Проверка интернет соединения...", speed=0.02, color="green")
		r.get("https://google.com", timeout=5)
	except Exception as es:
		clear()
		print(colored("[!]", "red"), colored("Ваше устройство не подключено к интернету или интернет слишком слабый!", "magenta"))
		exit()

def app():
	if platform in ["darwin", "win32"]:
		print(colored("Открываю ссылку!", "green"))
		webbrowser.open("https://t.me/orion_cloud_bot", new=0, autoraise=True)
		print("\nНажмите Enter чтобы вернуть назад")
		input()
	else:
		print()
		print(colored(" Попробуй данный Sms Bomber в новом", "yellow"), colored("Android", "green"), colored("приложении", "yellow"), colored("ORION app", "green"))
		print(colored("\n                 ---> ", "magenta"), colored("@orion_cloud_bot", "cyan"), colored(" <---", "magenta"))
		print("\n\nНажмите Enter чтобы вернуть назад")
		input()

def check_moderator():
	clear()
	anim_text("!WARNING!", speed=0.085, color="red")
	time.sleep(1.5)
	clear()
	anim_text("Эта функция предназначена только разработчикам...", speed=0.030, color="magenta")
	time.sleep(1)
	print()
	anim_text("Для продолжения введите код пароль если вы знаете что вы делаете...", speed=0.022, color="cyan")
	time.sleep(1)
	while True:
		print("\n")
		print(colored("[0] Выход", "red"))
		print()
		try:
			password = input(colored("~# ", "magenta"))
		except KeyboardInterrupt:
			return "return"
		if password == "868535514":
			return True
		elif password == "0":
			return "return"
		else:
			anim_text("Пароль неверный...", speed=0.030, color="red")
			time.sleep(1)

def force_update():
	result_m = check_moderator()
	if result_m == "return":
		return
	elif result_m == True:
		result = r.get("https://raw.githubusercontent.com/Lucky1376/ORION-Bomber/master/tools/version.txt")
		last_ver = result.content.decode("utf-8")

		update_list = r.get("https://raw.githubusercontent.com/Lucky1376/ORION-Bomber/master/tools/update_list.txt")
		update_list = update_list.content.decode("utf-8").split("\n")

		clear()
		print(colored("[!]", "magenta"), colored("Найдено новое обновление V", "green")+colored(last_ver, "cyan")+colored("!", "green"))
		print("")
		k = 0
		print(colored("Что нового?", "green"))
		for par in update_list:
			if len(update_list)-1 == k:
				print("└"+colored(par, "cyan"))
			else:
				print("├"+colored(par, "cyan"))
			k+=1
		print("")
		print(colored("Желаете ли вы обновиться до актуальной версии?", "yellow"))
		print("")
		print(colored("[1]", "red"), colored("Да", "green"))
		print(colored("[2]", "red"), colored("Нет", "red"))
		print("")
		while True:
			how = input(colored("~# ", "red"))
			if how == "1":
				clear()
				if platform == "linux" or platform == "linux2":
					print(colored("Устанавливаю архив...", "green"))
					os.chdir("/data/data/com.termux/files/home")
					os.system("rm -rf ORION-Bomber")
					
					result = r.get("https://github.com/Lucky1376/ORION-Bomber/archive/refs/heads/master.zip")
					
					a = open("ORION-Bomber.zip", "wb")
					a.write(result.content)
					a.close()
					
					print(colored("Распаковка архива...", "green"))

					fantasy_zip = zipfile.ZipFile("ORION-Bomber.zip")
					fantasy_zip.extractall("ORION-Bomber")
					fantasy_zip.close()
					os.system("rm -rf ORION-Bomber.zip")

					os.chdir("ORION-Bomber")
					os.chdir("ORION-Bomber-master")
					 
					get_files = os.listdir(os.getcwd())
					 
					for g in get_files:
						shutil.move(g, "/data/data/com.termux/files/home/ORION-Bomber")
					os.chdir("/data/data/com.termux/files/home/ORION-Bomber")
					os.system("rm -rf ORION-Bomber-master")

					print(colored("Обновление прошло успешно, запускаю ORION-Bomber...", "green"))
					time.sleep(1.5)

					os.system("pip install -r requirements.txt")
					os.system("python main.py")
					exit()
				elif platform == "win32":
					clear()
					os.startfile(os.getcwd()+"/updaters/windows.exe")
					exit()
				else:
					print(colored("[!]", "red"), colored("Наша программа пока не может установить обновление на вашу операционную ситему, вам придется скачать обновление вручную. В будущем мы постораемся сделать автообновление под вашу ОС!", "magenta"))
					print("\nНажмите Enter чтобы запустить программу на старой версии или введите 1 чтобы я открыл ссылку на репозиторий с актуальной версией")
					if input() == "1":
						result_open = webbrowser.open("https://github.com/Lucky1376/ORION-Bomber", new=0, autoraise=True)
						if not(result_open):
							clear()
							print(colored("Мне не удалось открыть ссылку на актуальную версию на вашем устройстве ;(", "red"))
							print("\n"+"Попробуйте открыть ее сами! "+colored("https://github.com/Lucky1376/ORION-Bomber", "green"))
							print("\nНажмите Enter чтобы запустить программу на старой версии или введите 1 чтобы выйти")
							if input() == "1":
								exit()
							else:
								return
						else:
							clear()
							print(colored("Скачивайте обновление!", "green"))
							exit()
					else:
						return
			elif how == "2":
				clear()
				break



def CFU():
	in_d = False
	# Checking the Internet
	try:
		r.get("https://google.com", timeout=5)
		in_d = True
	except:
		clear()
		print(colored("[!]", "red"), colored("Ваше устройство не подключено к интернету или интернет слишком слабый!", "magenta"))
		exit()
	clear()
	if in_d:
		anim_text("Проверяем обновление...", speed=0.02, color="green")
		# ├ └

		result = r.get("https://raw.githubusercontent.com/Lucky1376/ORION-Bomber/master/tools/version.txt")
		last_ver = result.content.decode("utf-8")

		update_list = r.get("https://raw.githubusercontent.com/Lucky1376/ORION-Bomber/master/tools/update_list.txt")
		update_list = update_list.content.decode("utf-8").split("\n")

		a = open("tools/version.txt", "r")
		current_ver = a.read()
		a.close()
		if last_ver != current_ver:
			clear()
			print(colored("[!]", "magenta"), colored("Найдено новое обновление V", "green")+colored(last_ver, "cyan")+colored("!", "green"))
			print("")
			k = 0
			print(colored("Что нового?", "green"))
			for par in update_list:
				if len(update_list)-1 == k:
					print("└"+colored(par, "cyan"))
				else:
					print("├"+colored(par, "cyan"))
				k+=1
			print("")
			print(colored("Желаете ли вы обновиться до актуальной версии?", "yellow"))
			print("")
			print(colored("[1]", "red"), colored("Да", "green"))
			print(colored("[2]", "red"), colored("Нет", "red"))
			print("")
			while True:
				how = input(colored("~# ", "red"))
				if how == "1":
					clear()
					if platform == "linux" or platform == "linux2":
						print(colored("Устанавливаю архив...", "green"))
						os.chdir("/data/data/com.termux/files/home")
						os.system("rm -rf ORION-Bomber")
						
						result = r.get("https://github.com/Lucky1376/ORION-Bomber/archive/refs/heads/master.zip")
						
						a = open("ORION-Bomber.zip", "wb")
						a.write(result.content)
						a.close()
						
						print(colored("Распаковка архива...", "green"))

						fantasy_zip = zipfile.ZipFile("ORION-Bomber.zip")
						fantasy_zip.extractall("ORION-Bomber")
						fantasy_zip.close()
						os.system("rm -rf ORION-Bomber.zip")

						os.chdir("ORION-Bomber")
						os.chdir("ORION-Bomber-master")
						 
						get_files = os.listdir(os.getcwd())
						 
						for g in get_files:
							shutil.move(g, "/data/data/com.termux/files/home/ORION-Bomber")
						os.chdir("/data/data/com.termux/files/home/ORION-Bomber")
						os.system("rm -rf ORION-Bomber-master")

						print(colored("Обновление прошло успешно, запускаю ORION-Bomber...", "green"))
						time.sleep(1.5)

						os.system("pip install -r requirements.txt")
						os.system("python main.py")
						exit()
					elif platform == "win32":
						clear()
						os.startfile(os.getcwd()+"/updaters/windows.exe")
						exit()
					else:
						print(colored("[!]", "red"), colored("Наша программа пока не может установить обновление на вашу операционную ситему, вам придется скачать обновление вручную. В будущем мы постораемся сделать автообновление под вашу ОС!", "magenta"))
						print("\nНажмите Enter чтобы запустить программу на старой версии или введите 1 чтобы я открыл ссылку на репозиторий с актуальной версией")
						if input() == "1":
							result_open = webbrowser.open("https://github.com/Lucky1376/ORION-Bomber", new=0, autoraise=True)
							if not(result_open):
								clear()
								print(colored("Мне не удалось открыть ссылку на актуальную версию на вашем устройстве ;(", "red"))
								print("\n"+"Попробуйте открыть ее сами! "+colored("https://github.com/Lucky1376/ORION-Bomber", "green"))
								print("\nНажмите Enter чтобы запустить программу на старой версии или введите 1 чтобы выйти")
								if input() == "1":
									exit()
								else:
									return
							else:
								clear()
								print(colored("Скачивайте обновление!", "green"))
								exit()
						else:
							return
				elif how == "2":
					clear()
					break
		else:
			clear()

class Logs:
	def __init__(self):
		pass

	def save_logs(self, service, status_code, error="There is not"):
		date = datetime.now()
		if status_code in [666, False]:
			status_code = "Unknown"
		with open("tools/logs.txt", "a", encoding="utf-8") as f:
			f.write(f"DATE - {date}\nService - {service}\nStatus_code - {status_code}\nERROR:\n{error}\n\n\n")

	def error_logs(self, error):
		date = datetime.now()
		with open("tools/error_logs.txt", "a", encoding="utf-8") as f:
			f.write(f"DATE - {date}\nERROR:\n{error}\n")

def check_files_fn(dir_, files):
	if dir_ != "":
		last_dir = os.getcwd()
		os.chdir(dir_)
	list_ = os.listdir()
	for f in files:
		if f not in list_:
			return False
	if dir_ != "":
		os.chdir(last_dir)
	return True

def check_files():
	anim_text("Проверка файлов...", speed=0.02, color="green")
	files = os.listdir()
	list_ = ["main.py", "LICENSE", "README.md", "tools"]
	list_2 = ["proxy.py", "sender.py", "services.json", "tools.py", "version.txt", "logs.txt", "error_logs.txt"]
	list_3 = ["windows.exe"]

	def ward():
		clear()
		print(colored("Наша программа не нашла некоторые наши файлы", "red"))
		print(colored("Пожалуйста установите программу заново предварительно удалив папку с этой!\n", "green"))
		exit()

	if not(check_files_fn("", list_)):
		ward()
	elif not(check_files_fn("tools", list_2)):
		ward()
	elif not(check_files_fn("updaters", list_3)):
		ward()

def CTF():
	try:
		with open("tools/timeout.txt", "r") as f:
			# Checking all services in the file
			if len(f.read().split()) < len(send.services_list + send.services_list_by):
				1/0
	except:
		with open("tools/timeout.txt", "w") as f:
			for serv in send.services_list:
				f.write(f"{serv}:0\n")
			for serv in send.services_list_by:
				f.write(f"{serv}:0\n")

def FormattingResponse(status_code, service):
	date = datetime.now()
	# Hour
	if date.hour <= 9:
		hour = f"0{date.hour}"
	else:
		hour = date.hour
	# Minute
	if date.minute <= 9:
		minute = f"0{date.minute}"
	else:
		minute = date.minute
	# Second
	if date.second <= 9:
		second = f"0{date.second}"
	else:
		second = date.second
	date = colored(f"{hour}:{minute}:{second}", "magenta")

	status_codes = {200: colored("SUCCESS", "green"),
					201: colored("SUCCESS", "green"),
					429: colored("TIME-OUT", "yellow"),
					400: colored("TIME_OUT", "yellow"),
					404: colored("NOT FOUND", "red"),
					500: colored("TIME-OUT", "yellow"),
					400: colored("TIME_OUT", "yellow")}
	service = colored(service, "yellow")
	if status_code not in status_codes:
		status_code = colored("UNKNOWN ANSWER", "red")
		info = f"{date} | {service} | {status_code}"
		print(info)
	else:
		info = f"{date} | {service} | {status_codes[status_code]}"
		print(info)

def start(number, country, proxy_=None):
	# Proxy preparation
	if proxy_ == None:
		proxy_ = None
	elif proxy_ in ["ru", "by"]:
		starting = True
		while starting:
			print(colored("\nПодготовка прокси... (Не дольше 1 минуты)", "yellow"))
			if proxy_ == "by":
				proxy_class = proxy.Proxy(country=["ru", "by"])
			else:
				proxy_class = proxy.Proxy(country=[country])
			proxy_class.get()
			print("")
			print(colored("Проверка найденного списка прокси... (Не дольше 2х минут)", "yellow"))
			proxy_class.verify()
			if proxy_class.mix() == False:
				print(colored("\n\nУПС!", "yellow"), colored("К сожалению наша программа не смогла найти ни одного рабочего прокси ;(", "green"))
				print("")
				print(colored("[1]", "red"), colored("Без прокси", "green"))
				print(colored("[2]", "red"), colored("Попробуем еще раз", "yellow"))
				print(colored("[3]", "red"), colored("Выход", "red"))
				print("")
				print(colored("Начать спам без прокси или попробуем еще раз?", "yellow"))
				while True:
					how = input(colored("~# ", "red"))
					if how in ["3", "0", "99"]:
						return
					elif how == "1":
						proxy_ = None
						starting = False
						break
					elif how == "2":
						break
			else:
				print(colored("\n\nПытаемся найти подходящий! (Не дольше 1 минуты)", "cyan"))
				all_list = proxy_class.mix()
				bar = ChargingBar('Ищем подходящий', max = len(all_list["all"]))
				# proxy_class.list[proxy_]
				for pr in all_list["all"]:
					ch = proxy.SPC(pr["ip"], pr["port"])
					bar.next()
					if ch != False:
						proxy_ = {"ip": pr["ip"],
								  "port": pr["port"],
								  "format": ch}
						starting = False
						break
					else:
						all_list["all"].remove(pr)
				if proxy_ in ["ru", "by"]:
					print(colored("\n\nК сожалению наша программа не нашла рабочий прокси ;(", "yellow"))
					print("")
					print(colored("[1]", "red"), colored("Да", "green"))
					print(colored("[2]", "red"), colored("Нет", "red"))
					print("")
					while True:
						how = input(colored("Начать спам без прокси? ", "green"))
						if how == "2":
							return
						elif how == "1":
							proxy_ = None
							starting = False
							break
				else:
					print("")
					print(colored("Прокси найден!", "green"))
					time.sleep(2)
					starting = False
	else:
		proxy_ = proxy_



	print()
	an=["3", "2", "1"]
	for i in an:
		print(colored("Спам начнется через ", "red")+colored(i, "green")+" ",sep=' ',end='\r')
		time.sleep(1)
	clear()
	print(colored("Остановка спама", "yellow"))
	print("├"+colored("Termux", "magenta")+":", colored("На встроенной клавиатуре от Termux выбрать CTRL затем C", "cyan"))
	print("└"+colored("Windows", "blue")+":", colored("Комбинация клавишь Ctrl+C или Ctrl+Z", "cyan"))
	print()


	if platform in ["darwin", "win32"]:
		if random.randint(1, 2) == 2:
			print(colored("Подпишитесь на наш", "green"), colored("Телеграм!", "cyan"))
			print(colored("Открываю ссылку...\n", "yellow"))
			webbrowser.open("https://t.me/orionbomber", new=0, autoraise=True)
	else:
		print(colored("Подпишитесь на наш", "green"), colored("Телеграм!", "cyan"), colored("t.me/orionbomber", "red"))
		print()
		
	# Number formats
	number = FormattingNumber(number, country)

	# Bomber launch
	sender_class = send.Send(country)
	logs = Logs()
	if country == "ru":
		services_list = send.services_list
	else:
		services_list = send.services_list_by
	starting_spam = True
	circles = 0
	circles_2 = 1
	while starting_spam:
		try:
			if circles == len(services_list):
				print(colored("Круг ", "green")+colored(str(circles_2), "yellow"), colored("Пройден!", "green"))
				circles -= len(services_list)
				circles_2 += 1
			time.sleep(1)
			for serv in services_list:
				if sender_class.checktimeout(serv) == True:
					if proxy_ != None:
						result = sender_class.spam(serv, number, proxy=proxy_["format"])
						if result[1] == "keyboard":
							raise KeyboardInterrupt

						if result[0] == False:
							logs.save_logs(serv, result[0], error=str(result[1]))
						else:
							logs.save_logs(serv, result[0])
						if result[0] == False:
							# Checking the proxy before the next spam attempt
							print(colored("Проверка прокси...", "yellow"))
							if "login" in proxy_:
								test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"], login=proxy_["login"], password=proxy_["password"])
								if test_proxy == False:
									print(colored("Ваш прокси больше не работает!", "red"))
									print("")
									print(colored("[1]", "red"), colored("Да", "green"))
									print(colored("[2]", "red"), colored("Нет", "red"))
									while True:
										print("")
										print(colored("Продолжить спам без прокси?", "yellow"))
										print("")
										how = input(colored("~# ", "red"))
										if how == "2":
											starting_spam = False
											return
										elif how == "1":
											proxy_ = None
											break
								else:
									proxy_ = {"ip": proxy_["ip"],
										     "port": proxy_["port"],
										     "login": proxy_["login"],
										     "password": proxy_["password"],
										     "format": test_proxy}
									print(colored("Прокси работает!", "green"))
									print(colored("Продолжаю спам!", "green"))

							else:
								try:
									a = all_list
									general = True
								except:
									general = False
								if general == False:
									test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"])
									if test_proxy == False:
										print(colored("Ваш прокси больше не работает!", "red"))
										print("")
										print(colored("[1]", "red"), colored("Да", "green"))
										print(colored("[2]", "red"), colored("Нет", "red"))
										while True:
											print("")
											print(colored("Продолжить спам без прокси?", "yellow"))
											print("")
											how = input(colored("~# ", "red"))
											if how == "2":
												starting_spam = False
												return
											elif how == "1":
												proxy_ = None
												break
									else:
										print(colored("Ваш прокси работает, продолжаю спам", "green"))
								else:
									test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"])
									if test_proxy == False:
										if len(all_list["all"]) < 1:
											print(colored("Увы но прокси закончились ;(", "yellow"))
											print("")
											print(colored("[1]", "red"), colored("Да", "green"))
											print(colored("[2]", "red"), colored("Нет", "red"))
											while True:
												print("")
												print(colored("Продолжить спам без прокси?", "yellow"))
												print("")
												how = input(colored("~# ", "red"))
												if how == "2":
													starting_spam = False
													return
												elif how == "1":
													proxy_ = None
													break
										else:
											print(colored("Берем следующий прокси...", "green"))
											last_pr = proxy_
											all_list["all"].remove(proxy_)
											for pr in all_list["all"]:
												ch = proxy.SPC(pr["ip"], pr["port"])
												if ch != False:
													proxy_ = {"ip": pr["ip"],
														      "port": pr["port"],
														      "format": ch}
													starting = False
													break
												else:
													all_list["all"].remove(pr)
											if proxy_ == last_pr:
												print(colored("Увы но прокси закончились ;(", "yellow"))
												print("")
												print(colored("[1]", "red"), colored("Да", "green"))
												print(colored("[2]", "red"), colored("Нет", "red"))
												while True:
													print("")
													print(colored("Продолжить спам без прокси?", "yellow"))
													print("")
													how = input(colored("~# ", "red"))
													if how == "2":
														starting_spam = False
														return
													elif how == "1":
														proxy_ = None
														break
									else:
										print(colored("Прокси работает, продолжаю спам!", "green"))
						else:
							circles += 1
							if result[0] != False:
								if serv == "magnit":
									if type(result[1]) == dict:
										if result[1]["status_code"] == 200:
											FormattingResponse(200, serv)
										elif result[1]["status_code"] == 422:
											FormattingResponse(429, serv)
									else:
										FormattingResponse(result[0], serv)
								else:
									FormattingResponse(result[0], serv)
							else:
								FormattingResponse(666, serv)
					else:
						result = sender_class.spam(serv, number)
						if result[1] == "keyboard":
							raise KeyboardInterrupt

						if result[0] == False:
							logs.save_logs(serv, result[0], error=str(result[1]))
						else:
							logs.save_logs(serv, result[0])
						circles += 1
						if result[0] != False:
							if serv == "magnit":
								if type(result[1]) == dict:
									if result[1]["status_code"] == 200:
										FormattingResponse(200, serv)
									elif result[1]["status_code"] == 422:
										FormattingResponse(429, serv)
								else:
									FormattingResponse(result[0], serv)
							else:
								FormattingResponse(result[0], serv)
						else:
							FormattingResponse(666, serv)
		except KeyboardInterrupt:
			starting_spam = False
			print("\n")
			print(colored("Спам был принудительно оставлен\n", "green"))
			print("Нажмите Enter чтобы вернуть назад")
			try:
				input()
			except KeyboardInterrupt:
				return
			return
		except Exception as e:
			starting_spam = False
			print("\n")
			print(colored("Из-за неизвестной ошибки наша программа выдала ошибку при спаме\n", "yellow"))
			logs.error_logs(traceback.format_exc())
			print(colored("Данная ошибка была сохранена в логи", "green"))
			print(colored("Пожалуйста отправьте нам файл с логами по инструкции в главном меню чтобы мы могли улучшать наш проект с вашей помощью", "green"))
			print("\nНажмите Enter чтобы вернуть назад")
			try:
				input()
			except KeyboardInterrupt:
				return
			return