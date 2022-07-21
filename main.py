from tools import tools
from tools import proxy
from tools import headers
from termcolor import colored
import requests

# Зачем ты это читаешь?
# Топай в папку tools

tools.clear()
tools.ICC()


while True:
	tools.clear()
	tools.banner()
	tools.banner_tools()

	tool = input(colored("\n~# ", "red"))
	if tool == "1":
		numb, ct, pr = tools.start_input()
		if numb != 0:
			tools.start(numb, ct, proxy_=pr)
	elif tool == "0":
		tools.clear()
		break
	elif tool == "99":
		tools.banner_info()