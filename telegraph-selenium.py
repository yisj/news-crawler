from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome()
target_url = 'https://telegraph.co.uk'
driver.get(target_url)

time.sleep(3.0)
s = BeautifulSoup(driver.page_source, 'lxml')
anchors = s.findAll('a')
