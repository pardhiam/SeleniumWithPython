from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://demoqa.com/login")
uname = driver.find_element(By.ID,"userName")
passwd = driver.find_element(By.ID,"password")
button = driver.find_element(By.XPATH,"//*[@id='login']")
uname.send_keys("pardhiam")
passwd.send_keys("Akshay@123")
driver.execute_script("arguments[0].click();", button)
time.sleep(5)
#driver.close()
try:
    ele = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"searchBox")))
    ele.send_keys("Learn Javascript")
    time.sleep(5)
finally:
    driver.close()