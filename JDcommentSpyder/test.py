import requests
import random
import time
import pandas as pd
import json
import re

head = [
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
]

headers = {
    'cookie': 'cna=K7rOF2J/nhMCAXeIkLUCxNPu; hng=CN%7Czh-CN%7CCNY%7C156; tk_trace=1; JSESSIONID=568E1847911C39255B099A6A849A351E; cookie2=291093acff45793b8841ff0fd789941e; t=3fddeb88d33ed12f18b22e1113ba864b; sm4=430100; xlly_s=1; _m_h5_tk=e44858a87c1b35b7a1184b9f72030071_1618233867437; _m_h5_tk_enc=f33e9e589cf2dc679ec5b32dc26300cd; dnk=%5Cu6C5F%5Cu5357%5Cu753B%5Cu89D2; uc1=pas=0&cookie14=Uoe1iuKPUsYyow%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=UIHiLt3xD8xYTw%3D%3D; uc3=nk2=3vuzDVBZ5m4%3D&vt3=F8dCuwuR80OJxKvG9Ig%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UU27KL2cg5Z6Ug%3D%3D; tracknick=%5Cu6C5F%5Cu5357%5Cu753B%5Cu89D2; lid=%E6%B1%9F%E5%8D%97%E7%94%BB%E8%A7%92; uc4=id4=0%40U2%2F8ng4Fg7h9j0sP7ZM8vf2ac6nr&nk4=0%403LJHTn3TYtZRZWINgLCEBBKzOA%3D%3D; _l_g_=Ug%3D%3D; unb=2597750169; lgc=%5Cu6C5F%5Cu5357%5Cu753B%5Cu89D2; cookie1=B0P6btSRhkQVxf880skF8k%2B3JY5EEm4zne6g6Um8HJ8%3D; login=true; cookie17=UU27KL2cg5Z6Ug%3D%3D; _nk_=%5Cu6C5F%5Cu5357%5Cu753B%5Cu89D2; sgcookie=E100RWO1dpQvwZsO2ZUlpaz2eHXLcVx3TiTJ6Awf62sPJiyYCMmODQsgZher38ZBv4mg3SgBby2lzr9q3g%2BmfJ9MQg%3D%3D; sg=%E8%A7%929a; csg=33b2126e; enc=H79hxg5wA8Ok5jEVPteFzRiRs4OMMjR55o1b39U%2B0bp83guKCooijzo6jL3ADm%2BB0Tbl40ttuuwcvW5Jru0Xxw%3D%3D; _tb_token_=3e76be85f3e11; x5sec=7b22726174656d616e616765723b32223a22346133326663373437356464383633353438376535303166323963306634306543492f6a30594d4745496a77395a616e7637754265426f4d4d6a55354e7a63314d4445324f5473784b41497737626e2f3350372f2f2f2f2f41513d3d227d; tfstk=cdZNBQ6oTGIZ4Jmfyci2GzddHL6Oa4q0VNHxSyXBF_wB0NutasqXMv0AU5FqwM0G.; l=eBMhcxC4jJ8lv1wvBO5whurza77O6BRf11PzaNbMiInca6QlGZYUWNCQybiwPdtjgtffletzhg8L7RKuu3Ud0ZqhuJ1REpZN0Yp6-; isg=BC8v_M7Gk9J8_5f5ELASVC4WvkM51IP2Md9cs0G6Nx-VkEySSaQLRyIGEoCu71tu',
    'user-agent': random.choice(head),
    'referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.12.2cda4cc94qigvO&id=611224893062&skuId=4519866672268&areaId=430100&user_id=1714128138&cat_id=2&is_b=1&rn=5e4f5884e30a4198cd35554c4629d0db',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9'
}


url = 'https://rate.tmall.com/list_detail_rate.htm'


# shop_id_dict = {
#     '小米官方旗舰店': '1714128138',
#     '苏宁易购官方旗舰店': '2616970884'
# }

# shop_referer_dict = {
#     '小米官方旗舰店': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.59.23fb7172b1D6Z4&id=611224893062&ns=1&abbucket=20&sku_properties=10004:7169121965;5919063:6536025',
#     '苏宁易购官方旗舰店': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.17.1bd14cc9IYFGXU&id=611525560119&skuId=4738749046979&areaId=430100&user_id=2616970884&cat_id=2&is_b=1&rn=01f46c0ddaffd9b92ad96c29f94a79c8'
# }

product_dict = {
    #'小米10': '611224893062'
     #'小米10至尊版': '100014565800'
    #  '小米11': '634228151538',
     '小米11pro': '640814759553'
    #  '小米11ultra': '639769508905'
}


def get_json(product_id, page):


    t = time.time()
    t_list = str(t).split('.')
    _ksTS = t_list[0] + t_list[1][:2] + '_' + t_list[1][3:]
    callback = 'jsonp' + str(int(t_list[1][3:]) + 1)

    params = {
        'itemId': product_id,
        'spuId': '1526565904',
        'sellerId': '1714128138',
        'order': 1,
        'currentPage': page,
        'append': 0,
        'content': 1,
        "callback": callback,
        "_ksTS": _ksTS
    }

    try:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        return r.text
    except:
        print('网络错误！')



def parse_json(json_str, data):

    json_text = re.findall('\{.*\}', text)[0]
    json_dict = json.loads(json_text)
    rate_detail = json_dict['rateDetail']
    rate_list = rate_detail['rateList']
    for rate in rate_list:
        rate_id = rate['id']
        item_type = rate['auctionSku']
        first_rate_time = rate['rateDate']
        first_rate_content = rate['rateContent']
        append_rate = rate['appendComment']
        if append_rate == None:
            append_rate_time = None
            append_rate_content = None
            after_days = None
        else:
            append_rate_time = append_rate['commentTime']
            append_rate_content = append_rate['content']
            after_days = append_rate['days']
        data.append([rate_id, product, item_type, first_rate_time, first_rate_content, append_rate_time, append_rate_content, after_days])

    #
    #
    #
    # for page in range(200, page_num+200):
    #     try:
    #         text = get_html(url, header, page)
    #         rate_time.extend(re.findall('"rateDate":"(.*?)"', text))
    #         item_type.extend(re.findall('"auctionSku":"(.*?)"', text))
    #         rate_content.extend(re.findall('"rateContent":"(.*?)"', text))
    #         append_com_lst = re.findall('"appendComment":(.*?),"fromMemory"', text)
    #         for append_com in append_com_lst:
    #             if append_com == "null":
    #                 append_comments.append(append_com)
    #             else:
    #                 append_comments.append(re.findall('"content":"(.*?)"', append_com)[0])
    #         print('第{}页爬取完成'.format(page + 1))
    #     except:
    #         print("未爬取到数据!")
    #
    # df = []
    # for i in range(len(rate_time)):
    #     df.append([rate_time[i], item_type[i], rate_content[i], append_comments[i]])
    # df1 = pd.DataFrame(df, columns=['rate_time', 'item_type', 'rate_content', 'append_comments'])
    # df1.to_csv('tb_mi10_comment.csv')



def get_last_page(product_id):

    text = get_json(product_id, page=0)
    json_text = re.findall('\{.*\}', text)[0]
    json_dict = json.loads(json_text)
    rate_detail = json_dict['rateDetail']
    paginator = rate_detail['paginator']
    last_page = paginator['lastPage']

    return last_page



if __name__ == '__main__':

    # shop_list = ['小米官方旗舰店', '苏宁易购官方旗舰店']
    i = 1
    data = []

    for product, product_id in product_dict.items():
        last_page = get_last_page(product_id)
        for page in range(1, last_page+1):
            text = get_json(product_id, page)
            parse_json(text, data)
            print('第{}页已爬取完成'.format(i))
            i += 1
            time.sleep(1)

    col_names = ['评论ID', '机型', '规格', '初评时间', '初评内容', '追评时间', '追评内容', '追评天数']
    df = pd.DataFrame(data, columns=col_names)
    print('爬取完成，共爬取{}条数据'.format(df.shape[0]))
    df.to_csv('tmall_guanfang_mi{}comment.csv'.format(product[2:]))