#!/bin/usr/python3

extremeiplookupkey = 'key-here'
numverifykey = 'key-here'

import sys
import os
import random
from bs4 import BeautifulSoup
import time
import requests
import colorama
from colorama import Fore
from requests import get

def Clear():
   if sys.platform == "linux":
    os.system("clear")
   elif sys.platform == "win32":
    os.system("cls")

def get_random_user_agent():
    userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
    userAgent = random.choice(userAgents)
    return userAgent

def peoplesearch():
    #does people searches
    Clear()
    name = input(f'{Fore.GREEN}Enter name (eg. john doe): ')
    location = input(f'{Fore.GREEN}Enter city (eg. palm bay): ')
    state = input(f'{Fore.GREEN}Enter state (eg. fl): ')
    name2 = name.replace(' ', '-')
    location2 = location.replace(' ', '-')
    state2 = state.replace(' ', '-')
    name3 = name.replace(' ', '+')
    location3 = location.replace(' ', '+')
    url0 = f'https://www.google.com/search?q=inurl:{name3}+{location3}+{state2}'
    url01 = f'https://www.google.com/search?q=intitle:{name3}+{location3}+{state2}'
    url02 = f'https://www.google.com/search?q=intext:{name3}+{location3}+{state2}'
    url1 = f'https://fastpeoplesearch.com/name/{name2}_{location2}-{state2}'
    url2 = f'https://www.truepeoplesearch.com/results?name={name2}&citystatezip={location2}-{state2}'
    url3 = f'https://www.fastbackgroundcheck.com/people/{name2}/{location2}-{state2}'
    url4 = f'https://voterrecords.com/voters/{location3}-{state2}/{name3}/'
    url5 = f'https://thatsthem.com/name/{name2}/{location2}-{state2}'
    url6 = f'https://www.searchpeoplefree.com/find/{name2}/{state2}/{location2}'
    url7 = f'https://www.usphonebook.com/{name2}/{state2}/{location2}'
    Clear()
    print (f'{Fore.GREEN}Googledorks:\n\n{Fore.RED}{url0}\n{url01}\n{url02}\n\n')
    print (f'{Fore.GREEN}Records:\n\n{Fore.GREEN}Fastpeoplesearch: {Fore.RED}{url1}\n{Fore.GREEN}Truepeoplesearch: {Fore.RED}{url2}\n{Fore.GREEN}Fastbackgroundcheck: {Fore.RED}{url3}\n{Fore.GREEN}Voterrecords: {Fore.RED}{url4}\n{Fore.GREEN}Thatsthem: {Fore.RED}{url5}\n{Fore.GREEN}Searchpeoplefree: {Fore.RED}{url6}\n{Fore.GREEN}Usphonebook: {Fore.RED}{url7}\n{Fore.RESET}')

def hole():
    Clear()
    mail = input(f'{Fore.GREEN}Enter email here (eg. example@example.com): {Fore.RESET}')
    Clear()
    os.system(f'holehe {mail}')

def geoip():
    Clear()
    if extremeiplookupkey == ('key-here'):
        print(f'{Fore.RED}[ERROR]:{Fore.YELLOW} You did not provide a numverify API key{Fore.RESET}')
        os._exit(1)
    else:
        pass
    ip = input(f'{Fore.GREEN}Enter IP here (eg. 1.1.1.1): ')
    print(f'{Fore.RESET}')
    Clear()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}?key={extremeiplookupkey}')
    geo = r.json()
    print(f"{Fore.GREEN}IP Whois:\nIP: {Fore.RED}{geo['query']}\n{Fore.GREEN}Status: {Fore.RED}{geo['status']}\n{Fore.GREEN}IP Type: {Fore.RED}{geo['ipType']}\n{Fore.GREEN}Org: {Fore.RED}{geo['org']}\n{Fore.GREEN}ISP: {Fore.RED}{geo['isp']}\n{Fore.GREEN}Country: {Fore.RED}{geo['country']}\n{Fore.GREEN}City: {Fore.RED}{geo['city']}\n{Fore.GREEN}Continent: {Fore.RED}{geo['continent']}\n{Fore.GREEN}Region: {Fore.RED}{geo['region']}\n{Fore.GREEN}Latitude: {Fore.RED}{geo['lat']}\n{Fore.GREEN}Longitude: {Fore.RED}{geo['lon']}")
    print(f'{Fore.RESET}')

def numverif():
    Clear()
    if numverifykey == ('key-here'):
        print(f'{Fore.RED}[ERROR]:{Fore.YELLOW} You did not provide a numverify API key{Fore.RESET}')
        os._exit(1)
    else:
        pass
    num = input(f'{Fore.GREEN}Enter Number here (eg. 14158586273): ')
    print(f'{Fore.RESET}')
    Clear()
    r = requests.get(f'http://apilayer.net/api/validate?access_key={numverifykey}&number={num}')
    verify = r.json()
    print(f"{Fore.GREEN}Number Whois:\nNumber: {Fore.RED}{verify['number']}\n{Fore.GREEN}Valid: {Fore.RED}{verify['valid']}\n{Fore.GREEN}Local Format: {Fore.RED}{verify['local_format']}\n{Fore.GREEN}International Format: {Fore.RED}{verify['international_format']}\n{Fore.GREEN}Country: {Fore.RED}{verify['country_name']}\n{Fore.GREEN}Country Code: {Fore.RED}{verify['country_code']}\n{Fore.GREEN}Country Prefix: {Fore.RED}{verify['country_prefix']}\n{Fore.GREEN}Location: {Fore.RED}{verify['location']}\n{Fore.GREEN}Line Type: {Fore.RED}{verify['line_type']}")
    print(f'{Fore.RESET}')
    
def usernameSearch():
    #searches for usernames
    Clear()
    userAgent = get_random_user_agent()
    headers = {
        "User-Agent": userAgent,
        "cookie": f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-CA",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-CA,en",
        "referer": "https://www.google.com/",
        "DNT": "1"
    }
    username = input(f"{Fore.GREEN}Enter Username: ")
    Clear()
    print(f'{Fore.GREEN}Results: \n')
    print(f'{Fore.GREEN}Google Dorks: \nhttps://www.google.com/search?q=inurl:{username}\nhttps://www.google.com/search?q=intitle:{username}\nhttps://www.google.com/search?q=intext:{username}\n')
    print(f'{Fore.GREEN}[-] = username taken \n{Fore.RED}[+] = username not found or rate limited\n{Fore.RESET}')

    instaurl = 'https://instagram.com/' + username
    instaresponse = get(instaurl, headers=headers)
    if instaresponse.status_code == 200:
        print(f'{Fore.GREEN}Instagram [-] {instaurl}')
    else:
        print(f'{Fore.RED}Instagram [+]')
    
    twitterurl = 'https://twitter.com/' + username
    twitterresponse = get(twitterurl, headers=headers)
    if twitterresponse.status_code == 200:
        print(f'{Fore.GREEN}Twitter [-] {twitterurl}')
    else:
        print(f'{Fore.RED}Twitter [+]')

    tumblrurl = 'https://' + username + '.' + 'tumblr.com'
    tumblrresponse = get(tumblrurl, headers=headers)
    if tumblrresponse.status_code == 200:
        print(f'{Fore.GREEN}Tumblr [-] {tumblrurl}')
    else:
        print(f'{Fore.RED}Tumblr [+]')

    viberurl = 'https://chats.viber.com/' + username
    viberresponse = get(viberurl, headers=headers)
    if viberresponse.status_code == 200:
        print(f'{Fore.GREEN}Viber [-] {viberurl}')
    else:
        print(f'{Fore.RED}Viber [+]')

    vkurl = 'https://vk.com/' + username
    vkresponse = get(vkurl, headers=headers)
    if vkresponse.status_code == 200:
        print(f'{Fore.GREEN}VK [-] {vkurl}')
    else:
        print(f'{Fore.RED}VK [+]')

    pinteresturl = 'https://pinterest.com/' + username
    pinterestresponse = get(pinteresturl, headers=headers)
    if pinterestresponse.status_code == 200:
        print(f'{Fore.GREEN}Pinterest [-] {pinteresturl}')
    else:
        print(f'{Fore.RED}Pinterest [+]')

    redditurl = 'https://reddit.com/user/' + username
    redditresponse = get(redditurl, headers=headers)
    if redditresponse.status_code == 200:
        print(f'{Fore.GREEN}Reddit [-] {redditurl}')
    else:
        print(f'{Fore.RED}Reddit [+]')

    taringaurl = 'https://taringa.net/' + username
    taringaresponse = get(taringaurl, headers=headers)
    if taringaresponse.status_code == 200:
        print(f'{Fore.GREEN}Taringa [-] {taringaurl}')
    else:
        print(f'{Fore.RED}Taringa [+]')

    taggedurl = 'http://tagged.com/' + username
    taggedresponse = get(taggedurl, headers=headers)
    if taggedresponse.status_code == 200:
        print(f'{Fore.GREEN}Tagged [-] {taggedurl}')
    else:
        print(f'{Fore.RED}Tagged [+]')

    badoourl = 'https://badoo.com/profile/' + username
    badooresponse = get(badoourl, headers=headers)
    if badooresponse.status_code == 200:
        print(f'{Fore.GREEN}Badoo [-] {badoourl}')
    else:
        print(f'{Fore.RED}Badoo [+]')

    githuburl = 'https://github.com/' + username
    githubresponse = get(githuburl, headers=headers)
    if githubresponse.status_code == 200:
        print(f'{Fore.GREEN}Github [-] {githuburl}')
    else:
        print(f'{Fore.RED}Github [+]')
    
    myspaceurl = 'https://myspace.com/' + username
    myspaceresponse = get(myspaceurl, headers=headers)
    if myspaceresponse.status_code == 200:
        print(f'{Fore.GREEN}Myspace [-] {myspaceurl}')
    else:
        print(f'{Fore.RED}Myspace [+]')

    mixurl = 'https://mix.com/' + username
    mixresponse = get(mixurl, headers=headers)
    if mixresponse.status_code == 200:
        print(f'{Fore.GREEN}Mix [-] {mixurl}')
    else:
        print(f'{Fore.RED}Mix [+]')

    wattpadurl = 'https://wattpad.com/user/' + username
    wattpadresponse = get(wattpadurl, headers=headers)
    if wattpadresponse.status_code == 200:
        print(f'{Fore.GREEN}Wattpad [-] {wattpadurl}')
    else:
        print(f'{Fore.RED}Wattpad [+]')

    deviantarturl = 'https://deviantart.com/' + username
    deviantartresponse = get(deviantarturl, headers=headers)
    if deviantartresponse.status_code == 200:
        print(f'{Fore.GREEN}Deviant Art [-] {deviantarturl}')
    else:
        print(f'{Fore.RED}Deviant Art [+]')

    goodreadsurl = 'https://goodreads.com/' + username
    goodreadsresponse = get(goodreadsurl, headers=headers)
    if goodreadsresponse.status_code == 200:
        print(f'{Fore.GREEN}Good Reads [-] {goodreadsurl}')
    else:
        print(f'{Fore.RED}Good Reads [+]')
    
    couchsurfurl = 'https://couchsurfing.com/people/' + username
    couchsurfresponse = get(couchsurfurl, headers=headers)
    if couchsurfresponse.status_code == 200:
        print(f'{Fore.GREEN}Couch Surfing [-] + {couchsurfurl}')
    else:
        print(f'{Fore.RED}Couch Surfing [+]')
    
    askfmurl = 'https://ask.fm/' + username
    askfmresponse = get(askfmurl, headers=headers)
    if askfmresponse.status_code == 200:
        print(f'{Fore.GREEN}Ask Fm [-] {askfmurl}')
    else:
        print(f'{Fore.RED}Ask Fm [+]')

    flickrurl = 'https://flickr.com/' + username
    flickrresponse = get(flickrurl, headers=headers)
    if flickrresponse.status_code == 200:
        print(f'{Fore.GREEN}Flickr [-] {flickrurl}')
    else:
        print(f'{Fore.RED}Flickr [+]')

    imgururl = 'https://imgur.com/user/' + username
    imgurresponse = get(imgururl, headers=headers)
    if imgurresponse.status_code == 200:
        print(f'{Fore.GREEN}Imgur [-] {imgururl}')
    else:
        print(f'{Fore.RED}Imgur [+]')

    scurl = 'https://soundcloud.com/' + username
    scresponse = get(scurl, headers=headers)
    if scresponse.status_code == 200:
        print(f'{Fore.GREEN}Soundcloud [-] {scurl}')
    else:
        print(f'{Fore.RED}Soundcloud [+]')

    mindsurl = 'https://minds.com/' + username
    mindsresponse = get(mindsurl, headers=headers)
    if mindsresponse.status_code == 200:
        print(f'{Fore.GREEN}Minds [-] {mindsurl}')
    else:
        print(f'{Fore.RED}Minds [+]')

    keyurl = 'https://keybase.io/' + username
    keyresponse = get(keyurl, headers=headers)
    if keyresponse.status_code == 200:
        print(f'{Fore.GREEN}Keybase [-] {keyurl}')
    else:
        print(f'{Fore.RED}Keybase [+]')

    doxurl = 'https://doxbin.com/user/' + username
    doxresponse = get(doxurl, headers=headers)
    if doxresponse.status_code == 200:
        print(f'{Fore.GREEN}Doxbin [-] {doxurl}')
    else:
        print(f'{Fore.RED}Doxbin [+]')

    replurl = 'https://replit.com/@' + username
    replresponse = get(replurl, headers=headers)
    if replresponse.status_code == 200:
        print(f'{Fore.GREEN}Replit [-] {replurl}')
    else:
        print(f'{Fore.RED}Replit [+]')

    solourl = 'https://solo.to/' + username
    soloresponse = get(solourl, headers=headers)
    if soloresponse.status_code == 200:
        print(f'{Fore.GREEN}Soloto [-] {solourl}')
    else:
        print(f'{Fore.RED}Soloto [+]')

def startup():
    Clear(  )
    print(f'''

    {Fore.RED}
    ╔═╗┌─┐┬┌┐┌┌┬┐  ╔╦╗┌─┐┌─┐┬   ╦╔═┬┌┬┐
    ║ ║└─┐││││ │    ║ │ ││ ││───╠╩╗│ │ 
    ╚═╝└─┘┴┘└┘ ┴    ╩ └─┘└─┘┴─┘ ╩ ╩┴ ┴ 
    ╔╗ ┬ ┬  ╦  ┌─┐┌┬┐┬ ┬┌─┐            
    ╠╩╗└┬┘  ║  │ │ │ │ │└─┐            
    ╚═╝ ┴   ╩═╝└─┘ ┴ └─┘└─┘            

    {Fore.BLUE}[1]{Fore.RESET} {Fore.GREEN}- {Fore.CYAN}Search for someones public records
    {Fore.BLUE}[2]{Fore.RESET} {Fore.GREEN}- {Fore.CYAN}Check if username is available on different social platforms
    {Fore.BLUE}[3]{Fore.RESET} {Fore.GREEN}- {Fore.CYAN}Preform whois lookup on the specified IP
    {Fore.BLUE}[4]{Fore.RESET} {Fore.GREEN}- {Fore.CYAN}Preform whois lookup on the specified phone number
    {Fore.BLUE}[5]{Fore.RESET} {Fore.GREEN}- {Fore.CYAN}Check what an email is used on{Fore.RESET}
    ''')
    print()
    initial = int(input(f'    {Fore.GREEN}> '))
    if initial == 1:
	    peoplesearch()
    elif initial == 2:
	    usernameSearch()
    elif initial == 3:
        geoip()
    elif initial == 4:
        numverif()
    elif initial == 5:
        hole()
    else:
	    print(f'{Fore.RED}[ERROR]: {Fore.YELLOW}Action not found')
startup()
