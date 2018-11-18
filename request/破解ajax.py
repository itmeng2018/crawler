import urllib.request
import ssl


def crawlerAjax(args):
    # 模拟请求头(防封ip)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XHLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36",
        "Content-Type": "application/x-www-from-urlencoded; charset=UTF-8"
    }
    req = urllib.request.Request(args, headers=headers)
    # 使用ssl创建未验证的上下文(抓取https)
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req, context=context)
    # 选择使用 json字符串形式, 方便写入文件
    jsonStr = response.read().decode('utf-8')
    return jsonStr


# 破解Ajax动态
for i in range(1, 11):
    url = r"https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
        i * 20) + r"&limit=20"
    info = crawlerAjax(url)
    fileName = './data/douban0' + str(i) + ".json"
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(info)
    print('爬取成功%d次, 生成文件 -- data/douban%d.json' % (i, i))
