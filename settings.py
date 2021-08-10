download_path = './B站漫画下载'
cookie_file = './B站漫画下载/cookie.txt'
url_Domestic_ImageToken = str('https://manga.bilibili.com/twirp/comic.v1.Comic/ImageToken?device=pc&platform=web')
url_Domestic_GetImageIndex = str('https://manga.bilibili.com/twirp/comic.v1.Comic/GetImageIndex?device=pc&platform=web')
url_Domestic_GetEpisode = str('https://manga.bilibili.com/twirp/comic.v1.Comic/GetEpisode?device=pc&platform=web')
url_Domestic_ComicDetail = str("https://manga.bilibili.com/twirp/comic.v2.Comic/ComicDetail?device=pc&platform=web")
letter_legal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-type": "application/json;charset=UTF-8",
    "origin": 'https://manga.bilibili.com',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.61 Safari/537.36",
    "cookie": "SESSDATA=d31a5ac5%2C1641642785%2C43b27%2A71"
}
headers_cdn = {
    'Host': 'manga.hdslb.com',
    'Origin': 'https://manga.bilibili.com',
}
