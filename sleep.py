# -*- coding: gbk -*-
import requests
import sys
from requests import ConnectTimeout

url="http://cat-match.easygame2021.com/sheep/v1/game/game_over"
url2="http://cat-match.easygame2021.com/sheep/v1/game/personal_info"
if len(sys.argv) != 3:
    print("ȱ�ٲ���!!!\n"  + "Usage:sleep.exe [token] [total-����ͨ�ش���]")
    exit()
tonken=sys.argv[1]
total=int(sys.argv[2])
num=0
getParams={
    "rank_score":1,
    "rank_state":1,
    "rank_time":1,
    "rank_role":1,
    "skin":1
}
headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
	81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',

	'Referer':'https://servicewechat.com/wx141bfb9b73c970a9/18/index.html',

    't':tonken,

    'Content-Type':'application/json',

    'Accept-Encoding':'gzip,compress,br,deflate'
		 }
def do_get(total):
    print('��ʼͨ��...')
    for i in range(total):
        try:
            res = requests.get(url=url, headers=headers,params=getParams,timeout=1)
            res_json=res.json()
            if res_json['err_code']==0:
                print('��',i+1,'�γɹ�')
            else:
                print('��',i+1,"��ʧ��!����!����!����ִ����ʧ��",++num,"��")
        except ConnectTimeout:
            print('��', i + 1, "��ʧ��!����!����!����ִ����ʧ��",++num,"��")
            continue
    print('ͨ�ز�������������')
    res2=requests.get(url=url2, headers=headers)
    res2_json = res2.json()
    res2_daily_count=res2_json['data']['daily_count']
    print('Ŀǰ���ƴ���',res2_daily_count,'��')
if __name__=="__main__":
    do_get(total)