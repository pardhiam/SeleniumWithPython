from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://facebook.com/")
ele = driver.find_element(By.NAME,"email")
print(ele.is_displayed())
print(ele.is_enabled())
#print(ele.is_selected())

ele1 = driver.find_element(By.NAME,"pass")
print(ele1.is_displayed())
print(ele1.is_enabled())

#driver.close()
driver.quit()