import os
import sys
import requests
from colorama import init
from colorama import init, Fore, Back, Style

Views = 0

def title_worker():
    global Views
    while True:
        os.system(f"title Views sent: {Views}")
        time.sleep(0.1)
        

Video = input('Video id [123456789] -> ')
url = "https://homedecoratione.com/v4.php"
hat = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length': '52',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'cookie': 'PHPSESSID=c1a15a17a74a3c4fa17d859ce3e3cc90; n=1',
'origin': 'https://homedecoratione.com',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'sec-gpc': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',
}
date =  {
'0429a': 'tok_free',
'af49f': 'views',
'9a898': '{Video}'}
while True:
    tiktoker = requests.post(url, data=date, headers=hat)
    print(Fore.GREEN + '[+] Succesfully sent view. Response -> ', tiktoker)

init(convert=True)