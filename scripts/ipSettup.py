import requests
from bs4 import BeautifulSoup
import json
import random


def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'html.parser')
    ips = json.loads(soup.text)['data']
    ip_list = []
    for ip in ips:
        ip_list.append(ip['ip'] + ':' + str(ip['port']))
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies