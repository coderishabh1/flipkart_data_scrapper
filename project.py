from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
#product=input("enter the product namae :")
product="iphone"
product_url = (f"https://www.flipkart.com/search?q={product}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
##print (product_url) generate the product page 
#number_of_product_pages=int(input("enter the number of pages you want to scrape:"))
number_of_product_pages=2
number_of_product_pages_links=[]
# total_product_link=[]
### this function collect the all product pages links which you want to scrape
def product_pages_links(number_of_product_pages):
    for i in range (1,number_of_product_pages+1):
        link = product_url+"&page="+str(i)
        number_of_product_pages_links.append(link)
    return number_of_product_pages_links
product_pages=product_pages_links(number_of_product_pages)
#print (product_pages[4])
product_page_html=requests.get(product_url)
soup=BeautifulSoup(product_page_html.text,'lxml')
Big_Box=soup.find('div',class_="_1YokD2 _3Mn1Gg")
Box=Big_Box.findAll("div",class_="_2kHMtA")
# print (len(Box))
# print (Big_Box)
#number_of_product_links=[]
# number_of_product_links=Box[0].find("a",class_="_1fQZEK").get('href')
# print (number_of_product_links)
# total_Box_link=[]
# def number_of_product():
#     for i in range (product_pages):
#         html=requests.get(product_pages[i])
#         soup1=BeautifulSoup(html.text,'lxml')
#         Big_Box=soup.find('div',class_="_1YokD2 _3Mn1Gg")
#         Box=Big_Box.findAll("div",class_="_2kHMtA")
#         for i in range (len(Box)):
#             links=Box[i].find("a",class_="_1fQZEK").get('href')
#             total_Box_link.append(links)
#     return total_Box_link
# total_box_links=number_of_product()
# print (total_box_links)
### this part of code collect the all product links 
total_product_link=[]
for i in range (0,len(product_pages)):
    #print (product_pages[i])
    product_page_html=requests.get(product_pages[i])
    soup=BeautifulSoup(product_page_html.text,'lxml')
    Big_Box=soup.find('div',class_="_1YokD2 _3Mn1Gg")
    Box=Big_Box.findAll("div",class_="_2kHMtA")
    #print (len(Box))
    for i in range (len(Box)):
        links=Box[i].find("a",class_="_1fQZEK").get('href')
        #print (links)
        # print (i)
        complete_link="https://www.flipkart.com"+links
        total_product_link.append(complete_link)
#print (len(total_product_link))
# html2=requests.get(total_product_link[i])
# soup2=BeautifulSoup(html2.text,'lxml')
# name=soup2.find("span",class_="B_NuCI")
# print (name.text)
product_name=[]
def product_Name(total_product_link):
    for i in range (0,len(total_product_link)):
        html2=requests.get(total_product_link[i])
        soup2=BeautifulSoup(html2.text,'lxml')
        name=soup2.find("span",class_="B_NuCI")
        try:
            product_name.append(name.text)
        except:
            product_name.append(name)
    return product_name
all_names=product_Name(total_product_link)
print ((all_names))
###This part of code is for to store all product price in list
product_price=[]
def all_product_price(total_product_link):
    for i in range (0,len(total_product_link)):
        html2=requests.get(total_product_link[i])
        soup2=BeautifulSoup(html2.text,'lxml')
        price=soup2.find("div",class_="_30jeq3 _16Jk6d")
        try:
            product_price.append(price.text)
        except:
            product_price.append(price)
    return product_price
all_product_price_list=all_product_price(total_product_link)
print ((all_product_price_list))
###this part od code for store rating of all product
product_rating=[]
def all_product_rating(total_product_link):
    for i in range (0,len(total_product_link)):
        html2=requests.get(total_product_link[i])
        soup2=BeautifulSoup(html2.text,'lxml')
        rating=soup2.find("div",class_="_3LWZlK")
        try:
            product_rating.append(rating.text)
        except:
            product_rating.append(rating)
    return product_rating
all_product_rating_list=all_product_rating(total_product_link)
print (all_product_rating_list)
###this code is store discount on the product
product_discount=[]
def all_product_discount(total_product_link):
    for i in range (0,len(total_product_link)):
        html2=requests.get(total_product_link[i])
        soup2=BeautifulSoup(html2.text,'lxml')
        discount=soup2.find("div",class_="_3Ay6Sb _31Dcoz")
        try:
            product_discount.append(discount.text)
        except:
            product_discount.append(discount)
    return product_discount
all_product_discount_list=all_product_discount(total_product_link)
print (all_product_discount_list)
###this part of code collect the all specification fo the product
product_specification=[]
def all_product_specification(total_product_link):
    list1=[]
    for i in range (0,len(total_product_link)):
        html2=requests.get(total_product_link[i])
        soup2=BeautifulSoup(html2.text,'lxml')
        specification=soup2.findAll("li",class_="_21Ahn-")
        print (len(specification))
        for i in range (len(specification)):
            try:
                list1.append(specification[i].text)
            except:
                list1.append(specification[i])
        product_specification.append(list1)
        list1=[]
    return product_specification
all_product_specification_list=all_product_specification(total_product_link)
print (all_product_specification_list)
##collect the specification of the all product
# l2=[] ###is use to store the one specific product 
# main_sp_list=[]##is use to collect the list of l2
# for i in range (len(total_product_link)):
#     html2=requests.get(total_product_link[i])
#     soup2=BeautifulSoup(html2.text,"lxml")
#     l1=soup2.findAll('li',class_="_21Ahn-")
#     for i in range (len(l1)):
#         try:
#             l2.append(l1[i].text)
#         except:
#             l2.append(l1[i])
#     main_sp_list.append(l2)
#     l2=[]
# print ((main_sp_list))
##this function scrape best offers of the project
product_offers=[]
def all_product_offers(total_product_link):
    list1=[]
    for i in range (0,len(total_product_link)):
        html2=requests.get(total_product_link[i])
        soup2=BeautifulSoup(html2.text,'lxml')
        offers=soup2.findAll("li",class_="_16eBzU col")
        print (len(offers))
        for i in range (len(offers)):
            try:
                list1.append(offers[i].text)
            except:
                list1.append(offers[i])
        product_offers.append(list1)
        list1=[]
    return product_offers
all_product_offers_list=all_product_offers(total_product_link)
print (all_product_offers_list)  


##convert the data into dataframe 


df=pd.DataFrame({"Product_Links":total_product_link , "Product_Name": all_names , "Product_Price" : all_product_price_list , "Product_Rating": all_product_rating_list , "Discount": all_product_discount_list , "Product_Specification" : all_product_specification_list , "Product_offers":all_product_offers_list})
df.to_csv("scrape_data.csv")



    




