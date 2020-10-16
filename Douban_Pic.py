#!/usr/bin/env python
# coding: utf-8

# # 豆瓣明星图片的抓取

# In[1]:


import requests
import os
from bs4 import BeautifulSoup
import re


def hold(pic_url,page_url,name):
    kv={'user-agent':'Mozilla/5.0','Referer':page_url}

    root = "D:/" + name + '/'
    
    #path=root+pic_url.split('/')[-1]
    path = os.path.join(root,pic_url.split('/')[-1])
  
    if not os.path.exists(root):
            os.mkdir(root)
            
    if not os.path.exists(path):
            print(pic_url)
            r=requests.get(pic_url,headers=kv)
            with open(path,'wb') as f:
                f.write(r.content)
               
                #print('保存成功')
    else:
            print('文件已存在')

            
def deal(u,name):
    
    for i in range(0,300,30):
        r='photos/?type=C&start='
        l='&sortby=like&size=a&subtype=a'
        
        page_url = u + r + str(i) + l
        #print(page_url)
        kv={'user-agent':'Mozilla/5.0','Referer':page_url}
        r = requests.get(page_url,headers=kv)
        demo=r.text
        soup=BeautifulSoup(demo,"html.parser")
        labels= re.findall(r"img src.{58}\w?.jpg",demo) 
        
        for j in labels:
            #print(labels)
            pic_url=j[9:]
            #print(pic_url)
            hold(pic_url,page_url,name) 
            
            
            
name=input('请输入想要下载的明星名字：')     # 'linian'
link=input('请输入想要下载明星的豆瓣主页：') # 'https://movie.douban.com/celebrity/1274508/'
deal(link,name)
print('已在D盘生成文件夹')


# 
# ```
# import requests 
# import os #为了文件的读取和写入
# from bs4 import BeautifulSoup #为了解析网页代码，使代码看起来更整齐，更方便写正则。当然理论上，不用也是可以的
# import re  #为了直接获取每张图片的url，适用于比较整齐的url。也可以利用bs4进行找寻、或者lxml
# 
# #hold函数是保存图片的函数
#     
# def hold(pic_url,page_url,name):
#     kv={'user-agent':'Mozilla/5.0','Referer':page_url}
#    # 注意这里的Referer要设置成可以到达该图片的url，直接从图片的url到达会触发防盗链
#    
#     root = "D:/" + name + '/'
#    # 这里的文件名最好不要带有中文
#     
#     path=root+pic_url.split('/')[-1]
#     #path = os.path.join(root,pic_url.split('/')[-1])
#    # 这里大佬是建议第二种方法
#    
#     if not os.path.exists(root):
#             os.mkdir(root)
#             
#     if not os.path.exists(path):
#             print(pic_url)
#             r=requests.get(pic_url,headers=kv)
#             with open(path,'wb') as f:
#                 f.write(r.content)
#                
#                 #print('保存成功')
#     else:
#             print('文件已存在')
# 
# 
# #deal函数是解析网页代码，找出每张图片的url的函数
# 
# def deal(u,name):
#     
#     # 设置循环是为了翻页，设置大的数值，更具有普适性
#     for i in range(0,300,30):
#     
#         r='photos/?type=C&start='
#         l='&sortby=like&size=a&subtype=a'
#         
#         page_url = u + r + str(i) + l
#         #print(page_url)
#         
#         kv={'user-agent':'Mozilla/5.0','Referer':page_url}
#        # 发送请求，获取页面代码
#         r = requests.get(page_url,headers=kv)
#         demo=r.text
#        # 解析代码
#         soup=BeautifulSoup(demo,"html.parser")
#        # 寻找页面中的图片url，返回列表，这里有一个坑，就是怎么找到合适的正则去选择，参照李念图片的爬取就知道了
#         labels= re.findall(r"img src.{58}\w?.jpg",demo) 
#        # 对图片url列表进行遍历，处理，将图片url传入hold函数
#         for j in labels:
#             #print(labels)
#             pic_url=j[9:]
#             #print(pic_url)
#             hold(pic_url,page_url,name) 
#             
#                       
# name=input('请输入想要下载的明星名字：')
# link=input('请输入想要下载明星的豆瓣主页：')
# deal(link,name)
# print('已在D盘生成文件夹')
# ```

# 1. 如何快速的爬取？如何保证稳定正常爬取？
# 2. 如何实现不复制链接就可以爬取（只输入明星的名字？）
# 3. 如何实现exe文件和可视化界面？
