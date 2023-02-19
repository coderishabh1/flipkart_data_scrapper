from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
al=[]
comment_list=[]
l ="https://www.flipkart.com/apple-iphone-14-midnight-128-gb/p/itm9e6293c322a84?pid=MOBGHWFHECFVMDCX&lid=LSTMOBGHWFHECFVMDCXBOYSND&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=b038612b-4c14-486c-9dc3-faeddf9ae382.MOBGHWFHECFVMDCX.SEARCH&ppt=hp&ppn=homepage&ssid=15er7zuzls0000001676704517193&qH=0b3f45b266a97d70"
r = requests.get(l)
soup=BeautifulSoup(r.text,"lxml")
#print (soup)
for i in soup.findAll('a',attrs= {'href':re.compile("/product-reviews/")}):
    a=i.get('href')
    al.append(a)
#print (al)
for i in al:
    if "LSTMOBGHWFHECFVMDCXBOYSND" in i:
        a=i
main_review_link ="https://www.flipkart.com"+(a)
print (main_review_link)
rr=requests.get(main_review_link)
soup1=BeautifulSoup(rr.text,'lxml')
num_page=soup1.find("div",class_="_2MImiq _1Qnn1K")
pa= (num_page.text.split())
paa=[]
#print (pa[3])
for i in pa[3]:
    paa.append(i)
total_pages=((int(paa[0]))*10+int(paa[1]))

# while(p==1):
#     review_page_link=main_review_link+"&page"+str(p)
#     rr=requests.get(review_page_link)
#     soup1 = BeautifulSoup(rr.text,"lxml")
#     for i in soup1.findAll("div",class_="t-ZTKy"):
#         c=i.text
#         com.append(c)
#     p=p+1
# print (com)
#print (soup1)
# com=soup1.find('div',class_="t-ZTKy")
# print (com.text)
for i in range (1,total_pages+1):
    main_l=main_review_link+"&page"+str(i)
    rr=requests.get(main_l)
    soup1=BeautifulSoup(rr.text,"lxml")
    for i in soup1.findAll('div',class_="t-ZTKy"):
        comment_list.append(i.text)
print ((comment_list))
# num_page=soup1.find("div",class_="_2MImiq _1Qnn1K")
# pa= (num_page.text.split())
# #print (pa[3])
# for i in pa[3]:
#     paa.append(i)
# total_pages=((int(paa[0]))*10+int(paa[1]))

   
