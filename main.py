# -*- coding:utf-8 -*-
import os
import sys
import requests
import time
import copy
import logging
import random

from lxml.etree import HTML

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# API_URL
LIKIE_URL = "https://tieba.baidu.com/f/like/mylike"
TBS_URL = "http://tieba.baidu.com/dc/common/tbs"
SIGN_URL = "https://tieba.baidu.com/sign/add"

ENV = os.environ


SIGN_DATA = {
    "ie": "utf-8",
    "kw": "",
    "tbs": ""
}

s = requests.Session()


def get_tbs():
    logger.info("获取tbs!")
    try:
        tbs = s.get(url=TBS_URL, timeout=5).json()["tbs"]
    except Exception as e:
        logger.error(e)
        sys.exit(1)
    logger.info("获取tbs结束!")
    return tbs


def get_favorite():
    logger.info("获取关注的贴吧!")
    # 客户端关注的贴吧
    try:
        res = s.get(url=LIKIE_URL, timeout=5)
    except Exception as e:
        logger.error("获取关注的贴吧出错!")
        logger.error(e)
        sys.exit(1)
    html = HTML(res.text)
    names = html.cssselect("tr td:first-child a")

    ret = []
    for name in names:
        ret.append(name.get('title'))
    return ret


def client_sign(tbs, kw):
    # 客户端签到
    logger.info("开始签到贴吧：" + kw)
    data = copy.copy(SIGN_DATA)
    data.update({"kw": kw, "tbs": tbs})
    res_json = s.post(url=SIGN_URL, data=data).json()
    if res_json["no"] == 1101:
        logger.info(f"{kw}吧 已签到!")
    elif res_json["no"] != 0:
        logger.error(f"{kw}吧 签到出现错误!")


def main():
    if 'COOKIE' not in ENV:
        logger.error("未配置COOKIE")
        return
    cookies = ENV['COOKIE'].splitlines()
    headers = {
        'Host': 'tieba.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    }
    for i, cookie in enumerate(cookies):
        logger.info("开始签到第" + str(i+1) + "个用户!")
        headers.update({"Cookie": cookie})
        s.headers.update(headers)
        favorites = get_favorite()
        tbs = get_tbs()
        for name in favorites:
            time.sleep(random.randint(2, 3))
            client_sign(tbs, name)
        logger.info("完成第" + str(i+1) + "个用户签到!")
    logger.info("所有用户签到结束!")


if __name__ == '__main__':
    main()