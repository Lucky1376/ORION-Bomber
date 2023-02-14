from tools import tools
from tools import proxy
from termcolor import colored
import requests

#   ____  ___  ________  _  __
#  / __ \/ _ \/  _/ __ \/ |/ /
# / /_/ / , _// // /_/ /    / 
# \____/_/|_/___/\____/_/|_/  
# 
#  https://t.me/orion_bomber | https://t.me/orion_smsbomber_bot                            

# Why are you reading this?
# Better subscribe to Telegram - https://t.me/orion_bomber

# There are 1592 lines in this project,
# if you count user_agent.py and services.json,
# then there will be 2267 lines,
# Wow, right?

tools.clear()
tools.ICC()
tools.clear()
tools.check_files()
tools.CFU()
tools.CTF()

while True:
	tools.clear()
	tools.banner()
	tools.banner_tools()

	try:
		tool = input(colored("\n~# ", "blue"))
	except KeyboardInterrupt:
		continue
	if tool == "1":
		numb, ct, pr = tools.start_input()
		if numb != 0:
			tools.start(numb, ct, proxy_=pr)
	elif tool == "0":
		tools.clear()
		break
	elif tool == "99":
		tools.banner_info()
	elif tool == "2":
		tools.donate()
	elif tool == "3":
		tools.inst_logs()
	elif tool.lower() == "4":
		tools.telebot()
	elif tool.lower() == "clear logs":
		tools.clear_logs()
	elif tool.lower() == "update":
		tools.force_update()
	else:
		pass