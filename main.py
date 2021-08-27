import configparser
from scripts.ipSettup import get_ip_list
from scripts.connection import outputHotShortComments, getUserAllRatings


config = configparser.ConfigParser()
config.read("config/config.txt")

cookies = config.get("configuration","cookie")
userAgent = config.get("configuration","userAgent")
ipUrl = config.get("configuration","ipUrl")

headers={
    "Cookie": cookies,
    "User-Agent": userAgent
    }


subjectId = "35096882"
fileName = "与君歌短评"

ip_list = get_ip_list(ipUrl, headers=headers)
# outputHotShortComments(ip_list, subjectId, fileName, headers)

subList = ['241541103', 'anyeruge', 'hw18311202258']
num = 1
for id in subList:
    print('正在处理: 第%s个用户!'% num)
    getUserAllRatings(id, ip_list, headers)
    num += 1
