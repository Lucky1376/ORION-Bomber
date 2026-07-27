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
		print(colored("\nSorry, our program does not support your operating system ;(\n", "red"))
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

	pred_info = " "*24+colored("Services", "green")+"\n"
	pred_info_ru = " "*17+colored("Russia ", "blue")+colored(ru_s, "green")+"   "
	pred_info_by = colored("Belarus ", "cyan")+colored(by_s, "green")+"\n"
	pred_info = pred_info+pred_info_ru+pred_info_by

	info = " "*13+colored("[", "blue")+"Developers :"+colored("rizza", "green")+" and "+colored("LostIk", "red")
	info_2 = " "*13+colored("[", "blue")+"Version    :"+colored(ver, "red")
	info_3 = " "*13+colored("[", "blue")+"Telegram   :"+colored("@orionbomber", "cyan")+colored("   <--", "green")
	info_4 = "\n"+" "*12+colored("This program is no longer supported!", "red")+"\n"

	print(banner)
	print(pred_info)
	print(info)
	print(info_2)
	print(info_3)
	print(info_4)

def banner_tools():
	print(colored("[1]", "red"), colored("Start spam", "green"))
	print(colored("[2]", "red"), colored("Support developers!    <---", "green"))
	print(colored("[3]", "red"), colored("Android app", "magenta"))
	#print(colored("[3]", "red"), colored("How to send logs", "yellow"))
	#print(colored("[4]", "red"), colored("Try", "green"), colored("in", "yellow"), colored("Telegram", "cyan")+colored("!", "yellow"), colored("   <---", "cyan"))
	print(colored("\n[99]", "red"), colored("Information", "cyan"))
	print(colored("\n[0] Exit", "red"))

def donate():
	print("")
	print(colored("Thanks for using the program :D", "green"))
	print("")
	print(colored("QIWI", "yellow"))
	print("├"+colored("https://qiwi.com/n/LUCKY1376", "cyan"), colored("Transfer by nickname", "green"))
	print("└"+colored("2200 7302 4344 6206", "cyan"), colored("MIR", "green"))
	#print("└"+colored("4890 4947 5754 5546", "cyan"), colored("VISA", "blue"))
	print("")
	print(colored("Sberbank", "green"))
	print("└"+colored("2202 2024 3331 7181", "cyan"), colored("MIR", "green"))
	#print("└"+colored("5469 4500 1265 2996", "cyan"), colored("MasterCard", "red"))
	#print("")
	##print(colored("YooMoney", "blue"))
	#print("├"+colored("4100 1174 8743 5875", "cyan"), "Account number")
	#print("└"+colored("2202 1201 0852 7850", "cyan"), colored("MIR", "green"))
	print("\nPress Enter to go back")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Files", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("were saved to the Download folder on your device", "green"))
			print(colored("Please send these 2 files one by one to our Telegram chat", "green"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"))
			print("")
			print("\nPress Enter to go back")
			input()
		elif platform == "win32" or platform == "darwin":
			print("")
			print(colored("Please send to our Telegram chat", "green"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"), colored("the files", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("one by one from the", "green"), colored("tools", "cyan"), colored("folder", "green"))
			print("")
			print("\nPress Enter to go back")
			input()
	except:
		print("")
		print(colored("We could not move files to the required directory", "yellow"))
		print(colored("Termux may not have access to Files and Media in app permissions", "yellow"))
		print(colored("Please grant all required permissions to Termux and try again"))
		print(colored("For help with this issue, contact our Telegram chat"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"))
		print("")
		print("\nPress Enter to go back")
		input()

def clear_logs():
	with open("tools/logs.txt", "w"):
		pass
	with open("tools/error_logs.txt", "w"):
		pass
	print("")
	print(colored("Logs were cleared successfully", "green"))
	print("\nPress Enter to go back")
	input()

def banner_info():
	print(colored("\nTelegram", "cyan"))
	print("├"+colored("rizza", "green")+":", colored("https://t.me/rlzza", "cyan"))
	print("├"+colored("LostIk", "red")+":", colored("https://t.me/lolzby", "cyan"))
	print("├"+colored("Android APK", "magenta")+":", colored("https://t.me/orion_cloud_bot", "cyan"))
	print("└"+colored("Channel", "cyan")+":", colored("https://t.me/orionbomber", "cyan"))
	print("\nPress Enter to go back")
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
		print(colored("[99] Cancel", "red"))
		print("")
		print(colored("[1]", "red"), colored("Belarus +375", "blue"))
		print(colored("[2]", "red"), colored("Russia +7", "cyan"))
		print("")
		ct = input(colored("Select country: ", "green"))
		if ct == "2":
			break
		elif ct == "1":
			break
		elif ct == "99":
			return 0, 0, 0
		else:
			clear()
			print(colored("New country", "magenta"), colored(ct, "cyan")+colored("!", "magenta"))
			print()
	clear()
	while True:
		print(colored("[99] Cancel", "red"))
		print()
		numb = input(colored("Enter number without country code "+country_code[ct]+" ", "green"))
		if number_ckeck(numb):
			break
		else:
			clear()
			print(colored("This does not look like a phone number...", "magenta"))
			print()
		if numb == "99":
			return 0, 0, 0
	clear()
	while True:
		print(colored("[99] Cancel", "red"))
		print()
		print(colored("[1]", "red"), colored("Yes", "green"))
		print(colored("[2]", "red"), colored("No", "red"))
		print()
		pr = input(colored("Use proxy?: ", "green"))
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
			print(colored("Pick one of the options...", "magenta"))
			print()
	clear()
	if pr != None:
		while True:
			print(colored("[99] Cancel", "red"))
			print()
			print(colored("[1]", "red"), colored("Public proxy", "yellow"))
			print("└"+colored("Public proxies are shared by all ORION-Bomber users", "cyan"))
			print()
			print(colored("[2]", "red"), colored("Your own proxy", "green"))
			print("└"+colored("Your proxy must support HTTP or HTTPS over IPv4 and match your phone-number country", "cyan"))
			print()
			who_pr = input("Option: ")
			if who_pr in ["1", "2"]:
				if who_pr == "2":
					print()
					print(colored("[99] Cancel", "red"))
					print()
					print(colored("Enter IP and Port, and login/password if the proxy is private", "green"))
					print("└"+colored("Example:\n├123.45.678.910:8080\n└123.45.678.910:8080:LOGIN:PASSWORD", "cyan"))
					print()
					new_pr = input(colored("~# ", "red"))
					
					if new_pr == "99":
						return 0, 0, 0
					elif len(new_pr.split(":")) < 3:
						# Shared Proxy Check
						result = proxy.SPC(new_pr.split(":")[0], new_pr.split(":")[1])
						if result == False:
							print(colored("Your proxy is not working!", "red"))
						else:
							pr = {"ip": new_pr.split(":")[0],
								  "port": new_pr.split(":")[1],
								  "format": result}
							print(colored("Proxy is working!", "green"))
							time.sleep(2)
							break
					elif len(new_pr.split(":")) > 2:
						# Private Proxy Check
						result = proxy.SPC(new_pr.split(":")[0], new_pr.split(":")[1], login=new_pr.split(":")[2], password=new_pr.split(":")[3])
						if result == False:
							print(colored("Your proxy is not working!", "red"))
						else:
							pr = {"ip": new_pr.split(":")[0],
								  "port": new_pr.split(":")[1],
								  "login": new_pr.split(":")[2],
								  "password": new_pr.split(":")[3],
								  "format": result}
							print(colored("Proxy is working!", "green"))
							time.sleep(2)
							break

				else:
					break
			elif who_pr == "99":
				return 0, 0, 0
			else:
				clear()
				print(colored("Please choose one of the options instead of typing custom text", "magenta"), colored(who_pr, "cyan"))
				print()

	return country_code[ct]+numb, country_code_2[ct], pr

def ICC():
	try:
		anim_text("Checking internet connection...", speed=0.02, color="green")
		r.get("https://google.com", timeout=5)
	except Exception as es:
		clear()
		print(colored("[!]", "red"), colored("Your device is not connected to the internet or the connection is too weak!", "magenta"))
		exit()

def app():
	if platform in ["darwin", "win32"]:
		print(colored("Opening link!", "green"))
		webbrowser.open("https://t.me/orion_cloud_bot", new=0, autoraise=True)
		print("\nPress Enter to go back")
		input()
	else:
		print()
		print(colored(" Try this SMS Bomber in the new", "yellow"), colored("Android", "green"), colored("app", "yellow"), colored("ORION app", "green"))
		print(colored("\n                 ---> ", "magenta"), colored("orion-cloud.ru", "cyan"), colored(" <---", "magenta"))
		print("\n\nPress Enter to go back")
		input()

def check_moderator():
	clear()
	anim_text("!WARNING!", speed=0.085, color="red")
	time.sleep(1.5)
	clear()
	anim_text("This feature is for developers only...", speed=0.030, color="magenta")
	time.sleep(1)
	print()
	anim_text("To continue, enter the password code only if you know what you are doing...", speed=0.022, color="cyan")
	time.sleep(1)
	while True:
		print("\n")
		print(colored("[0] Exit", "red"))
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
			anim_text("Wrong password...", speed=0.030, color="red")
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
		print(colored("[!]", "magenta"), colored("New update found V", "green")+colored(last_ver, "cyan")+colored("!", "green"))
		print("")
		k = 0
		print(colored("What's new?", "green"))
		for par in update_list:
			if len(update_list)-1 == k:
				print("└"+colored(par, "cyan"))
			else:
				print("├"+colored(par, "cyan"))
			k+=1
		print("")
		print(colored("Do you want to update to the latest version?", "yellow"))
		print("")
		print(colored("[1]", "red"), colored("Yes", "green"))
		print(colored("[2]", "red"), colored("No", "red"))
		print("")
		while True:
			how = input(colored("~# ", "red"))
			if how == "1":
				clear()
				if platform == "linux" or platform == "linux2":
					print(colored("Installing archive...", "green"))
					os.chdir("/data/data/com.termux/files/home")
					os.system("rm -rf ORION-Bomber")
					
					result = r.get("https://github.com/Lucky1376/ORION-Bomber/archive/refs/heads/master.zip")
					
					a = open("ORION-Bomber.zip", "wb")
					a.write(result.content)
					a.close()
					
					print(colored("Extracting archive...", "green"))

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

					print(colored("Update completed successfully, launching ORION-Bomber...", "green"))
					time.sleep(1.5)

					os.system("pip install -r requirements.txt")
					os.system("python main.py")
					exit()
				elif platform == "win32":
					clear()
					os.startfile(os.getcwd()+"/updaters/windows.exe")
					exit()
				else:
					print(colored("[!]", "red"), colored("Our program cannot install updates on your operating system yet. You will need to download the update manually. We will try to add auto-update support for your OS in the future!", "magenta"))
					print("\nPress Enter to run the old version, or type 1 to open the repository link with the latest version")
					if input() == "1":
						result_open = webbrowser.open("https://github.com/Lucky1376/ORION-Bomber", new=0, autoraise=True)
						if not(result_open):
							clear()
							print(colored("I could not open the link to the latest version on your device ;(", "red"))
							print("\n"+"Try opening it manually: "+colored("https://github.com/Lucky1376/ORION-Bomber", "green"))
							print("\nPress Enter to run the old version, or type 1 to exit")
							if input() == "1":
								exit()
							else:
								return
						else:
							clear()
							print(colored("Download the update!", "green"))
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
		print(colored("[!]", "red"), colored("Your device is not connected to the internet or the connection is too weak!", "magenta"))
		exit()
	clear()
	if in_d:
		anim_text("Checking for updates...", speed=0.02, color="green")
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
			print(colored("[!]", "magenta"), colored("New update found V", "green")+colored(last_ver, "cyan")+colored("!", "green"))
			print("")
			k = 0
			print(colored("What's new?", "green"))
			for par in update_list:
				if len(update_list)-1 == k:
					print("└"+colored(par, "cyan"))
				else:
					print("├"+colored(par, "cyan"))
				k+=1
			print("")
			print(colored("Do you want to update to the latest version?", "yellow"))
			print("")
			print(colored("[1]", "red"), colored("Yes", "green"))
			print(colored("[2]", "red"), colored("No", "red"))
			print("")
			while True:
				how = input(colored("~# ", "red"))
				if how == "1":
					clear()
					if platform == "linux" or platform == "linux2":
						print(colored("Installing archive...", "green"))
						os.chdir("/data/data/com.termux/files/home")
						os.system("rm -rf ORION-Bomber")
						
						result = r.get("https://github.com/Lucky1376/ORION-Bomber/archive/refs/heads/master.zip")
						
						a = open("ORION-Bomber.zip", "wb")
						a.write(result.content)
						a.close()
						
						print(colored("Extracting archive...", "green"))

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

						print(colored("Update completed successfully, launching ORION-Bomber...", "green"))
						time.sleep(1.5)

						os.system("pip install -r requirements.txt")
						os.system("python main.py")
						exit()
					elif platform == "win32":
						clear()
						os.startfile(os.getcwd()+"/updaters/windows.exe")
						exit()
					else:
						print(colored("[!]", "red"), colored("Our program cannot install updates on your operating system yet. You will need to download the update manually. We will try to add auto-update support for your OS in the future!", "magenta"))
						print("\nPress Enter to run the old version, or type 1 to open the repository link with the latest version")
						if input() == "1":
							result_open = webbrowser.open("https://github.com/Lucky1376/ORION-Bomber", new=0, autoraise=True)
							if not(result_open):
								clear()
								print(colored("I could not open the link to the latest version on your device ;(", "red"))
								print("\n"+"Try opening it manually: "+colored("https://github.com/Lucky1376/ORION-Bomber", "green"))
								print("\nPress Enter to run the old version, or type 1 to exit")
								if input() == "1":
									exit()
								else:
									return
							else:
								clear()
								print(colored("Download the update!", "green"))
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
	anim_text("Checking files...", speed=0.02, color="green")
	files = os.listdir()
	list_ = ["main.py", "LICENSE", "README.md", "tools"]
	list_2 = ["proxy.py", "sender.py", "services.json", "tools.py", "version.txt", "logs.txt", "error_logs.txt"]
	list_3 = ["windows.exe"]

	def ward():
		clear()
		print(colored("Our program did not find some required files", "red"))
		print(colored("Please reinstall the program after deleting this folder first!\n", "green"))
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
			print(colored("\nPreparing proxies... (No longer than 1 minute)", "yellow"))
			if proxy_ == "by":
				proxy_class = proxy.Proxy(country=["ru", "by"])
			else:
				proxy_class = proxy.Proxy(country=[country])
			proxy_class.get()
			print("")
			print(colored("Checking found proxy list... (No longer than 2 minutes)", "yellow"))
			proxy_class.verify()
			if proxy_class.mix() == False:
				print(colored("\n\nOOPS!", "yellow"), colored("Unfortunately, our program could not find any working proxy ;(", "green"))
				print("")
				print(colored("[1]", "red"), colored("Without proxy", "green"))
				print(colored("[2]", "red"), colored("Try again", "yellow"))
				print(colored("[3]", "red"), colored("Exit", "red"))
				print("")
				print(colored("Start spam without proxy or try again?", "yellow"))
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
				print(colored("\n\nTrying to find a suitable one! (No longer than 1 minute)", "cyan"))
				all_list = proxy_class.mix()
				bar = ChargingBar('Searching for a match', max = len(all_list["all"]))
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
					print(colored("\n\nUnfortunately, our program did not find a working proxy ;(", "yellow"))
					print("")
					print(colored("[1]", "red"), colored("Yes", "green"))
					print(colored("[2]", "red"), colored("No", "red"))
					print("")
					while True:
						how = input(colored("Start spam without proxy? ", "green"))
						if how == "2":
							return
						elif how == "1":
							proxy_ = None
							starting = False
							break
				else:
					print("")
					print(colored("Proxy found!", "green"))
					time.sleep(2)
					starting = False
	else:
		proxy_ = proxy_



	print()
	an=["3", "2", "1"]
	for i in an:
		print(colored("Spam will start in ", "red")+colored(i, "green")+" ",sep=' ',end='\r')
		time.sleep(1)
	clear()
	print(colored("Stopping spam", "yellow"))
	print("├"+colored("Termux", "magenta")+":", colored("On the built-in Termux keyboard, press CTRL then C", "cyan"))
	print("└"+colored("Windows", "blue")+":", colored("Use Ctrl+C or Ctrl+Z", "cyan"))
	print()


	if platform in ["darwin", "win32"]:
		if random.randint(1, 2) == 2:
			print(colored("Subscribe to our", "green"), colored("Telegram!", "cyan"))
			print(colored("Opening link...\n", "yellow"))
			webbrowser.open("https://t.me/orionbomber", new=0, autoraise=True)
	else:
		print(colored("Subscribe to our", "green"), colored("Telegram!", "cyan"), colored("t.me/orionbomber", "red"))
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
				print(colored("Round ", "green")+colored(str(circles_2), "yellow"), colored("Completed!", "green"))
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
							print(colored("Checking proxy...", "yellow"))
							if "login" in proxy_:
								test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"], login=proxy_["login"], password=proxy_["password"])
								if test_proxy == False:
									print(colored("Your proxy is no longer working!", "red"))
									print("")
									print(colored("[1]", "red"), colored("Yes", "green"))
									print(colored("[2]", "red"), colored("No", "red"))
									while True:
										print("")
										print(colored("Continue spam without proxy?", "yellow"))
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
									print(colored("Proxy is working!", "green"))
									print(colored("Continuing spam!", "green"))

							else:
								try:
									a = all_list
									general = True
								except:
									general = False
								if general == False:
									test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"])
									if test_proxy == False:
										print(colored("Your proxy is no longer working!", "red"))
										print("")
										print(colored("[1]", "red"), colored("Yes", "green"))
										print(colored("[2]", "red"), colored("No", "red"))
										while True:
											print("")
											print(colored("Continue spam without proxy?", "yellow"))
											print("")
											how = input(colored("~# ", "red"))
											if how == "2":
												starting_spam = False
												return
											elif how == "1":
												proxy_ = None
												break
									else:
										print(colored("Your proxy works, continuing spam", "green"))
								else:
									test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"])
									if test_proxy == False:
										if len(all_list["all"]) < 1:
											print(colored("Unfortunately, proxies are exhausted ;(", "yellow"))
											print("")
											print(colored("[1]", "red"), colored("Yes", "green"))
											print(colored("[2]", "red"), colored("No", "red"))
											while True:
												print("")
												print(colored("Continue spam without proxy?", "yellow"))
												print("")
												how = input(colored("~# ", "red"))
												if how == "2":
													starting_spam = False
													return
												elif how == "1":
													proxy_ = None
													break
										else:
											print(colored("Taking the next proxy...", "green"))
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
												print(colored("Unfortunately, proxies are exhausted ;(", "yellow"))
												print("")
												print(colored("[1]", "red"), colored("Yes", "green"))
												print(colored("[2]", "red"), colored("No", "red"))
												while True:
													print("")
													print(colored("Continue spam without proxy?", "yellow"))
													print("")
													how = input(colored("~# ", "red"))
													if how == "2":
														starting_spam = False
														return
													elif how == "1":
														proxy_ = None
														break
									else:
										print(colored("Proxy works, continuing spam!", "green"))
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
			print(colored("Spam was stopped manually\n", "green"))
			print("Press Enter to go back")
			try:
				input()
			except KeyboardInterrupt:
				return
			return
		except Exception as e:
			starting_spam = False
			print("\n")
			print(colored("Due to an unknown issue, our program raised an error during spam\n", "yellow"))
			logs.error_logs(traceback.format_exc())
			print(colored("This error was saved to logs", "green"))
			print(colored("Please send us the log file using instructions from the main menu so we can improve the project with your help", "green"))
			print("\nPress Enter to go back")
			try:
				input()
			except KeyboardInterrupt:
				return
			return
