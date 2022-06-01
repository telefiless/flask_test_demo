from audioop import cross
from unicodedata import name
import requests
import re
import json
from flask_cors import *

from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>你好</h1>'


# if __name__ == '__main__':
#     app.run(debug=True)
# @app.route('/api', methods=['GET'])
# def hello_world_1():
#     d = {}
#     # d['icon_add'] = str(request.args.get('url'))
#     d['icon_add'] = request.args.get('url')+'/favicon.ico'

#     return jsonify(d)


# @app.route('/windows', methods=['GET'])
# def hello_world_2():
#     dc = {}
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#     r = requests.get(
#         'https://www.microsoft.com/zh-cn/software-download/windows10/', "lxml", headers=headers)
#     r.encoding = "utf-8"
#     soup = BeautifulSoup(r.text)
#     xinxi = soup.find_all('h2')[0].text
#     xiazai = soup.find_all('a', id='windows10-upgrade-now')[0]['href']

# # d['icon_add'] = str(request.args.get('url'))
#     dc['title'] = xinxi
#     dc['url'] = xiazai

#     return jsonify(dc)

# 开始毛片


@app.route('/index', methods=['GET'])
# 开启跨越请求
@cross_origin()
def hello_world_3():
    # dp = {}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    r = requests.get(
        'https://053113.cm.100av.app/videos/3d', "lxml", headers=header)

    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text)
    leibie = soup.find_all('div', class_='thumb-overlay')
    shuzu = []
    zidian = {}
    for i in leibie:
        # 去除gif文件
        if i.find('img').get('data-original').endswith('.jpg'):
            # print(i.find('img').get('data-original'))
            title = i.find('img').get('alt')
            img_src = i.find('img').get('data-original')
            # paly_src='https://053113.cm.100av.app/video/'+img_src[-9:-6]
            paly_src = 'https://053113.cm.100av.app/video/' + \
                re.split('/', img_src)[-2]
            # zidian.update({'title': title, 'lianjie': lianjie})
            # print(i.find('img').get('title'))
            # shuzu.append(img_src)
            zidian.update(
                {"title": title, "img_src": img_src, "paly_src": paly_src})
            # json_str = json.dumps(zidian, ensure_ascii=False)
            print(zidian)

            # print(json_str)

    return render_template('index.html', name=zidian)
# d['icon_add'] = str(request.args.get('url'))
    #  dp['title'] = xinxi
    # dp['url'] = xiazai

    # return jsonify(dc)


if __name__ == '__main__':
    app.run(debug=True)
