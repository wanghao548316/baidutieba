#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Copyright (c) 2016 Trio.com, Inc. All Rights Reserved
#Filename:    spider.py
#Author:        lvfeifei
#Email:        lyufeifei@trio.ai
#Date:        2018-07-11
#Desc:        
#
#===============================================================================
import scrapy
import json
import re
import sys
import string
import random
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')

class tiebaspider(scrapy.Spider):
    name = "douban1"
#    allowded_domians = ['m.douban.com']
   # start_urls = ['https://www.douban.com/group/studenttravel/discussion?start=0']
   # start_urls = ['https://www.douban.com/group/topic/117122519/']
    start_urls = ['https://www.douban.com/group/Appearance/discussion?start=0','https://www.douban.com/group/cat/discussion?start=0','https://www.douban.com/group/minimalists/discussion?start=0']
    def parse(self,response):
        urls = response.xpath('//*[@class="title"]/a/@href').extract()
        for url1 in urls:
            if "topic" in url1:
                url = 'https://m.douban.com/group/topic'+url1.split('topic')[1]
                yield scrapy.Request(url,callback = self.content_parse )
        next_page=response.xpath('//*[@class="next"]/a/@href').extract()
        if next_page:
            next_page = ''.join(next_page)
            yield scrapy.Request(next_page,callback = self.parse )

    def content_parse(self,response):
 #   def parse(self,response):
        url1 = response.url
        title = response.xpath('//*[@class="header s-content"]//h1/text()').extract()
        title = ''.join(title)
        content = response.xpath('//*[@id="content"]').extract()
        content = "".join(content)
        content = re.sub(r'<div.*?>|</div>|<a.*?>|</a>|<span.*?>|</span>|</p>|</h1>|<p>|<h1>|<br.*?>|</br>',"",content)
        zan_num= response.xpath('//*[@class="note-content paper"]//a[contains(@rel,"nofollow")]/span/text()').extract()      
        zan_num=''.join(zan_num)
        user_date = response.xpath('//*[@class="user-title"]/span').extract()
        user_date = ''.join(user_date)
        user_date = re.sub(r'<div.*?>|</div>|<a.*?>|</a>|<span.*?>|</span>|<p>|<h1>|<br>|</p>|</h1>|<br.*?>|</br>',"",user_date)
        user_date=user_date.replace('\n','\t')
        author = user_date.split('\t')[1]
        user_dates = user_date.split('\t')[2]
        author = author.strip()
        user_dates = user_dates.strip()
        zuire = response.xpath('/html/body/div[3]/div[1]/section[4]/h2[1]/text()').extract()
        comment =[]
        comment_pop=[]
        zuire=''.join(zuire)
        if "最热回应" in zuire:
            cc = response.xpath('//*[@class="s-content"]//li[contains(@class,"reply-item")]')
            for dd in cc:
                user_id1 = dd.xpath('.//div[1]/a/@href').extract()
                user_id1 = ''.join(user_id1)
                user_id1 = user_id1.strip()
                user_id1 = user_id1.split('people')[1]
                user_id1 = user_id1.replace('/','')
                user1 = dd.xpath('.//div[1]/div/span').extract()
                user1 = ''.join(user1)
                user1 = user1.strip()
                user1 = re.sub(r'<div.*?>|</div>|<a.*?>|</a>|<span.*?>|</span>|</p>|</h1>|<p>|<h1>|<br.*?>|</br>|ss+',"",user1)
                date1 = dd.xpath('.//div[1]/div/time').extract()
                date1 = ''.join(date1)
                date1 = date1.strip()
                date1 = re.sub(r'<div.*?>|</div>|<a.*?>|<time>|</time>|</a>|<span.*?>|</span>|</p>|</h1>|<p>|<h1>|<br.*?>|</br>|ss+',"",date1)
                content1 = dd.xpath('.//div[2]').extract()
                content1 = ''.join(content1)
                content1 = re.sub(r'<div.*?>|</div>|<a.*?>|</a>|<span.*?>|</span>|</p>|</h1>|<p>|<h1>|<br.*?>|</br>|ss+',"",content1)
                content1 = content1.strip()
                content1 = re.sub(r'\n','',content1)
                zan1 = dd.xpath('.//div[3]/a[1]').extract()
                zan1 = ''.join(zan1)
                zan1 = zan1.strip()
                zan1 = re.sub(r'<.*?>','',zan1)
                comment_pop.append(str(user_id1)+'\t'+str(user1)+'\t'+str(content1)+'\t'+str(date1)+'\t'+str(zan1))
      #  huiyingshu = response.xpath('//*[@id="n_comments"]/text()').extract()
      #  huiyingshu = ''.join(huiyingshu)
      #  if huiyingshu:
      #      proxyHost = "http-pro.abuyun.com"
      #      proxyPort = "9010"
                    # 代理隧道验证信息
      #      proxyUser = "H21RW3199042D5IP"
      #      proxyPass = "067F847F6189E995"
      #      proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      #      "host" : proxyHost,
      #      "port" : proxyPort,
      #      "user" : proxyUser,
      #      "pass" : proxyPass,
      #          }      

      #      proxies = urllib2.ProxyHandler({
      #          "http": proxyMeta,
      #          "https": proxyMeta,
      #          })
      #      opener = urllib2.build_opener(proxies)
      #      urllib2.install_opener(opener)
            
            
      #      page_num=int(huiyingshu)/25+1
      #      for i in range(0,page_num):
      #          url = url1+'comments?start='+str(i*25)

      #          html = urllib2.urlopen(url).read()
      #          soup = BeautifulSoup(html,'lxml')
      #          a = soup.find_all("li",class_="reply-item")
      #          for bb in a:
      #              bb = str(bb)
      #              cc = BeautifulSoup(bb,'lxml')
      #              user_id2 = cc.find("div",class_="reply-meta").a
      #              user_id2 =  user_id2.get('href')
      #              user11 = user_id2.split('people')[1]
      #              user_id2 = user11.replace('/','')
      #              user2 = cc.find("div",class_="reply-meta").div.span.string
      #              date2 = cc.find("div",class_="reply-meta").div.time.string
      #              zan_num2 = cc.find("a",class_="reply-like").string
      #              content2 = cc.find("div",class_="reply-content")
      #              content2 = str(content2)
      #              content2 = re.sub(r'<div.*?>|</div>|<a.*?>|</a>|<span.*?>|</span>|</p>|</h1>|<p>|<h1>|<br.*?>|</br>|ss+',"",content2)
      #              content2 = content2.strip()
         #           content2 = re.sub("ss+" , " ", content2)
      #              content2 = re.sub(r'\n','',content2)
      #              comment.append(str(user_id2)+'\t'+str(user2)+'\t'+str(content2)+'\t'+str(date2)+'\t'+str(zan_num2))

        ww = {}
        ww['title']=title.strip()
        ww['content']= content.strip()
        ww['zan'] = str(zan_num)
        ww['date'] = str(user_dates) 
        ww['user'] = str(author)
        ww['pop_comment'] = comment_pop
       # ww['comment'] = comment    
        ww['url']=url1 
       # print ww
       # print user_date
        with open('douban.txt','a+') as f:
            f.write(json.dumps(ww,ensure_ascii=False)+'\n')
                
       # print user_date
#  print response.body
       # title = response.xpath('//*[@id="content"]/h1').extract()
       # title = "".join(title)
       # title = title.replace('\n','')
       # title = re.sub(r'<div.*?>|</div>|<a.*?>|</a>|<span.*?>|</span>|<p>|<h1>|<br>|</p>|</h1>|</br>',"",title)
       # content = response.xpath('//*[@id="link-report"]/div').extract()
       # content = "".join(content)
       # content = content.replace('\n','')
       # content = re.sub(r'<div.*?>|</div>|<a.*?>|</a>|<span.*?>|</span>|</p>|</h1>|<p>|<h1>|<br>|</br>',"",content)
       # url = response.url
        ####################################
       # user_id = response.xpath('//*[@class="topic-doc"]/h3/span[1]/a/@href').extract()
       # user_id = ''.join(user_id)
       # user = response.xpath('//*[@class="topic-doc"]/h3/span[1]/a/text()').extract()
       # user = ''.join(user)
       # floor_date = response.xpath('//*[@class="topic-doc"]/h3/span[2]/text()').extract()
       # floor_date = ''.join(floor_date)
        #######################################################################
      #  html = response.body
      #  html = str(html)
      #  selector = BeautifulSoup(html,'lxml')
      #  li = selector.find_all("li",class_="clearfix comment-item")
      #  for li_s in li:
      #      c_user_id = li_s.h4.a.get('href')
       #     c_date = li_s.h4.span.string
       #     c_user = li_s.h4.a.string
       #     
       #     li_s1 = str(li_s)
       #     selector1 = BeautifulSoup(li_s1,'lxml')
       #     b = selector1.find("a",class_="comment-vote lnk-fav")
       #     cc = b.string
       #     print cc









        ###########################################################################


        #    with open('douban1.txt','a+') as f:
         #   if title and content:
         #       f.write(title.strip()+'\t'+content.strip()+'\t'+url.strip()+'\t'+user_id +'\t'+user+'\t'+floor_date+'\t'+cc+'\n')
            
    




