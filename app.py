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
    title_shuzu = []
    img_src_shuzu = []
    paly_src_shuzu = []
    zidian = {}
    for i in leibie:
        # 去除gif文件
        if i.find('img').get('data-original').endswith('.jpg'):
            # print(i.find('img').get('data-original'))
            title = i.find('img').get('alt')
            img_src = i.find('img').get('data-original')
            paly_src = 'https://053113.cm.100av.app/video/' + \
                re.split('/', img_src)[-2]
            # zidian.update({'title': title, 'lianjie': lianjie})
            # print(i.find('img').get('title'))
            # shuzu.append(img_src)
            zidian.update(
                {"title": title, "img_src": img_src, "paly_src": paly_src})
            # json_str = json.dumps(zidian, ensure_ascii=False)
            # print(zidian)
            title_shuzu.append(title)
            img_src_shuzu.append(img_src)
            paly_src_shuzu.append(paly_src)

            # print(json_str)
    
    # return render_template('index.html', name=zidian)
    return render_template('index.html', name_title=title_shuzu, name_img_src=img_src_shuzu, name_paly_src=paly_src_shuzu)
# d['icon_add'] = str(request.args.get('url'))
    #  dp['title'] = xinxi
    # dp['url'] = xiazai

    # return jsonify(dc)


if __name__ == '__main__':
    app.run(debug=True)
