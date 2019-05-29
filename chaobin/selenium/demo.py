from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
url='http://news.sina.com.cn/o/2004-07-06/10433003819s.shtml'
driver.get(url)
e=driver.find_element_by_xpath('//*[@id="zoom"]/p[1]')
print(e.text)
driver.close()