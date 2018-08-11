#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Copyright (c) 2016 Trio.com, Inc. All Rights Reserved
#Filename:    1.py
#Author:        lvfeifei
#Email:        lyufeifei@trio.ai
#Date:        2018-07-11
#Desc:        
#
#===============================================================================
import base64
proxyServer = "http://http-dyn.abuyun.com:9020"
proxyUser = "H015H0290I3L0HCD"


proxyPass = "40D3C92B5DCEFCF6"
proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth


