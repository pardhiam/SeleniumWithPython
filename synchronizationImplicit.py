import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.get("http://demoqa.com/login")
username = driver.find_element(By.ID, "userName")
password = driver.find_element(By.ID, "password")
#btn_login = driver.find_element(By.ID,"login")
button = driver.find_element(By.XPATH,"//*[@id='login']")
username.send_keys("pardhiam")
password.send_keys("Akshay@123")
driver.execute_script("arguments[0].click();", button)
time.sleep(5)
#btn_login.click()
driver.close()
