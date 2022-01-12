import requests
from bs4 import BeautifulSoup
import pandas as pd
import pickle
import time

header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }


def get_ids(tid):

    ids_list = []
    n_page = 1544 if tid == 1 else 1457

    for page in range(n_page):
        url = 'https://www.baobeihuijia.com/list.aspx?tid=%d&page=%d' % (tid, page+1)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features='html.parser')
        pic_bot = soup.find('div', class_='pic_bot')
        kids = pic_bot.find_all('input')
        for kid in kids:
            ids_list.append(kid.attrs['id'][:-4])
        print('已爬取%d页信息...' % (page+1))

    print('=' * 50)
    print('共爬取%d条信息' % len(ids_list))
    with open('ids_%d.txt' % tid, 'wb') as f:
        pickle.dump(ids_list, f)


def get_infos(type, id):
    """
    type=1 : 家寻宝贝
    type=2 : 宝贝寻家
    """
    url = 'https://www.baobeihuijia.com/view.aspx?type=%d&id=%s' % (type, id)
    r = requests.get(url, headers=header)
    html = r.text
    soup = BeautifulSoup(html, features='html.parser')
    table = soup.find('table')
    infos = table.find_all('li')
    infos_list = [info.text.split('：')[-1] for info in infos][2:]

    return infos_list


def save_to_excel(type):

    with open('ids_%d.txt' % type, 'rb') as f:
        ids = pickle.load(f)

    with open('failed_ids_%d.txt' % type, 'r') as f:
        failed_ids = f.read().split('\n')[:-1]

    if type == 1:
        finished_ids = pd.read_csv('家寻宝贝.csv')['寻亲编号'].astype(str)
    if type == 2:
        finished_ids = pd.read_csv('宝贝寻家.csv')['寻亲编号'].astype(str)

    ids = list(set(ids) - set(finished_ids) - set(failed_ids))

    l = len(ids)
    print('本次共%d条数据待爬取' % l)

    df = []
    count = 0
    for id in ids:
        print('正在爬取编号为%s的数据，已爬取%d/%d条数据' % (id, count, l))
        try:
            row = get_infos(type, id)
            df = pd.DataFrame([row])
        except:
            print('=' * 50)
            print('编号为%s的数据爬取失败' % id)
            with open('failed_ids_%d.txt' % type, 'a') as f:
                f.write(id + '\n')
            continue
        finally:
            if type == 1:
                df.to_csv('家寻宝贝.csv', mode='a', header=False)
            if type == 2:
                df.to_csv('宝贝寻家.csv', mode='a', header=False)
        count += 1


def main():

    save_to_excel(1)


if __name__ == '__main__':
    main()