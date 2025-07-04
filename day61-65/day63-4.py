"""
example05.py - 多线程版本爬虫
"""
import os
from concurrent.futures import ThreadPoolExecutor

import requests


def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'images/pet/{filename}', 'wb') as file:
            file.write(resp.content)


def main():
    if not os.path.exists('images/pet'):
        os.makedirs('images/pet')
    with ThreadPoolExecutor(max_workers=16) as pool:
        for page in range(3):
            resp = requests.get(f'https://image.so.com/zjl?ch=pet&sn={page * 5}')
            if resp.status_code == 200:
                pic_dict_list = resp.json()['list']
                for pic_dict in pic_dict_list:
                    pool.submit(download_picture, pic_dict['qhimg_url'])


if __name__ == '__main__':
    main()