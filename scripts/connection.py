import requests
from bs4 import BeautifulSoup
from scripts.ipSettup import get_random_ip

def statusCode(response):
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')


def getRatingComments(url, headers, proxies):
    # 调取所有短评
    r = requests.get(url=url,headers=headers, proxies = proxies)
    print('正在处理: %s' % url)
    statusCode(r)
    data = r.content.decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    commentInfo = soup.find_all('span', class_='comment-info')
    return commentInfo


def getRatingCommentsDetail(shortCommentInfo):
    # 调取所有短评中的评分，用户ID以及短评时间
    rating = shortCommentInfo.find_all("span")[1]["title"]
    userid = shortCommentInfo.find("a")["href"][30:-1]
    time = shortCommentInfo.find("span", class_="comment-time")['title']
    return rating, userid, time


def outputHotShortComments(ip_list, subjectId, fileName, headers):
    # 将某个剧的所有最热点评中的评分,用户ID以及
    page = 0
    fpath = "output/" + fileName +".txt"
    with open(fpath, 'a', encoding='utf-8') as f:
        while page < 500 :
            proxies = get_random_ip(ip_list)
            url = "https://movie.douban.com/subject/" + subjectId + "/comments?start=" + str(page) + "&limit=20&status=P&sort=new_score"
            commentInfo = getRatingComments(url, headers, proxies)

            for info in commentInfo:
                rating, userid, time = getRatingCommentsDetail(info)
                f.write(rating + "\t"  + userid + "\t" + time + '\n')
            page+=20