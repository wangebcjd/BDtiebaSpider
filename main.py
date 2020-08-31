import requests
from lxml import etree
num = -1
def Textspider(url, page):
    content = requests.get(url, headers=headers).text
    html = etree.HTML(content)
    print(type(html))
    l = html.xpath('//*[@class="d_post_content j_d_post_content "]/text()')
    with open("1.txt", 'a') as f:
        f.write("第{}页".format(page)+'\n')
        f.writelines([Fnum()+i+'\n' for i in l])
    for i in l:
        pass
        print(i)
def Fnum():
    global num
    num += 1
    return str(num)+': '
max = 21
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
for i in range(max):
    page = i+1
    url = "https://tieba.baidu.com/p/3467849589?see_lz=1&pn={}".format(page)
    Textspider(url, page)