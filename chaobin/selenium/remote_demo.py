#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2019/5/23 10:32
@Author  : xumj
'''
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Remote
from time import sleep

dr = Remote(
command_executor='http://127.0.0.1:4444/wd/hub',
desired_capabilities={
'platfrom':'ANY',
'browserName':'chrome',
'version':'',
'javascriptEnabled':True}
)

dr.get('http://baidu.com')

dr.find_element_by_id('kw').send_keys('hello')
sleep(3)
dr.quit()