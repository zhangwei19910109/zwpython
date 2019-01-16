'''
用于爬取豆瓣电影的评论头像。
电影id：9592082
头像名称为用户名称
保存文件夹 E:\crewdatas\doubancommits\\
'''

import requests
from bs4 import BeautifulSoup

BASEURL = "https://movie.douban.com/review/9592082/"
BASEDIR = "E:\crewdatas\doubancommits\\"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": 'bid=GHtmXbS_AZI; douban-fav-remind=1; ll="118124"; __utmc=30149280; __utmc=223695111; __yadk_uid=2DEIPqYqzw185HXxDePJhxsN9m0q6ncH; __utmz=30149280.1543281312.7.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1543281312.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1543286875%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dj1wjkwWmLUSX-ODctN8PYOzYFx7SDLUlnbpxGFtHMPBR-AzRcLz7g8oOhLzx58xc%26wd%3D%26eqid%3Daa95775500039d50000000035bfc9aa5%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.983750084.1532157255.1543281312.1543286876.8; __utmt_douban=1; __utma=223695111.2043986183.1543218469.1543281312.1543286876.3; __utmb=223695111.0.10.1543286876; _pk_id.100001.4cf6=9bcb796364b8ca37.1543218469.3.1543286951.1543282359.; __utmb=30149280.2.10.1543286876',
    "Host": "movie.douban.com",
    "Referer": "https://movie.douban.com/review/best/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


def getpage(BASEURL):
    response = requests.get(BASEURL, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        None


def dealImg(name, imgurl):
    response = requests.get(imgurl)
    if response.status_code == 200:
        with open(BASEDIR + name, "wb") as f:
            f.write(response.content)


def dealData(responseText):
    soup = BeautifulSoup(responseText, 'html5lib')
    soup.prettify()
    tagscom = soup.select("div #comments")
    tags = tagscom[0].select(".comment-item")
    if tags:
        for tag in tags:
            name = ''
            name += tag.attrs['data-user_name']
            # tag.select(".comment-text")
            src_ = tag.select(".left a img")[0]['src']
            name += src_[-4:]
            dealImg(name, src_)


def main():
    responseText = getpage(BASEURL)
    dealData(responseText)


if __name__ == '__main__':
    main()
