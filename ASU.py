#Tusbol By Sazxt
import os
import interpreter
import requests
from data.color import *
os.system("clear")
if os.path.exists('config'):
	if os.path.exists('config/config.json'):
		if os.path.getsize('config/config.json') != 0:
			interpreter.ASU()
		else:
			interpreter.login()
	else:
		interpreter.login()
else:
	os.mkdir('config')
	open('config/config.json', 'w').close()
	interpreter.login()