from bs4 import BeautifulSoup
import requests
import time

def Phrase_ETF_Components():
    ETF_List_URL = "https://www.twse.com.tw/zh/page/ETF/list.html"
    try:
        page = requests.get(ETF_List_URL)
        text = BeautifulSoup(page.text, 'html.parser').find('tbody').text
        text = list(filter(None, text.splitlines()))
        table = []
        comp = []
        cnt = 0
        for i in text:
            if cnt < 4:
                comp.append(i)
                cnt=cnt+1
            else:
                table.append(comp)
                comp = []
                cnt = 0
        print(table)
    except:
        print("Failed to get list from twse website.")

def Get_Historical_Stock():
    URL = "https://www.twse.com.tw/exchangeReport/FMSRFK?response=json&date=20200101&stockNo=2330"
    page = requests.get(URL)
    

Phrase_ETF_Components()

list = []






















































'''
cookies = {
    'CpeAdminCookie': '3d1pqhdvagrwbsdx5m2ucput',
}
headers1 = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://172.16.1.78',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://172.16.1.78/CpeAdmin/Login.aspx',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
data1 = {
  'txtName': 'yintao',
  'txtPassword': 'Cbn123',
}

headers2 = {
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'http://172.16.1.78',
    'Referer': 'http://172.16.1.78/CpeAdmin/CPEs/AdvancedView_new.aspx',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'X-MicrosoftAjax': 'Delta=true',
}

data2 = {

}


with requests.Session() as s:
    response1 = requests.post('http://172.16.1.78/CpeAdmin/Default.aspx', headers=headers1, cookies=cookies, data=data1, verify=False)
    print(response1.text)
    print("==================================================")
    index_page= s.post('http://172.16.1.78/CpeAdmin/CPEs/AdvancedView_new.aspx', headers=headers2, cookies=cookies, data=data2, verify=False)
    fp = open("filename.txt", "a")
    fp.write(index_page.text)
    fp.close()
    print("==================================================")
    soup = BeautifulSoup(index_page.text, 'html.parser')
    print(soup.textarea)
'''