#[H[2J[3J uncompyle6 version 3.4.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Aug  6 2019, 01:11:15) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <string>
con()
req = requests.Session()
req.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36'})
e = raw_input('[!] No Account Detected\n[*] Login Your Fb\n[?] Username: ')
p = raw_input('[?] Password: ')
print '[*] Login ...'
s = req.post('https://mbasic.facebook.com/login', data={'email': e, 'pass': p}).url
if 'save-device' in s or 'm_sess' in s:
    i = json.dumps({'email': e, 'pass': p, 
       'name': bs4.BeautifulSoup(req.get('https://mbasic.facebook.com/me').text, features='html.parser').find('title').text})
    open('config/config.json', 'w').write(i)
    exit('[*] Login Success..\n[!] Run again: python2 ASU.py')
if 'checkpoint' in s or 'challange' in s:
    exit('[!] checkpoint challange,your account was locked by facebook,pls open your facebook in browser before you login with asu toolkit\n[!] Run again: python2 ASU.py')
else:
    exit('[!] Login Failed.\n[!] Run again: python2 ASU.py')