from tools import tools
from tools import proxy
from termcolor import colored
import requests

# Why are you reading this?

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
		tool = input(colored("\n~❆ ", "blue"))
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
	#elif tool == "2":
		#tools.faq_proxy()
	#elif tool == "3":
		#tools.quick_guide()
	#elif tool == "4":
		#tools.disclaimer()
	elif tool == "2":
		tools.donate()
	elif tool == "3":
		tools.inst_logs()
	elif tool.lower() == "clear logs":
		tools.clear_logs()
	elif tool.lower() == "update":
		tools.force_update()
	else:
		pass