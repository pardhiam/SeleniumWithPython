from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://google.com/")
print(driver.title)
driver.get("http://facebook.com/")
time.sleep(3)
print(driver.title)
driver.back()
time.sleep(3)
print(driver.title)
driver.forward()
time.sleep(3)
print(driver.title)
driver.close()