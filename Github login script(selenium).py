from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://github.com/login'

driver.get(url)
time.sleep(2)

username = '//*[@id="login_field"]'
password = '//*[@id="password"]'
signin = '/html/body/div[1]/div[4]/main/div/div[2]/form/div[3]/input'


username_feild = driver.find_element(By.XPATH , value=username)
password_feild = driver.find_element(By.XPATH, value=password)
signin_feild = driver.find_element(By.XPATH, value=signin)


username_feild.send_keys("your username here")
password_feild.send_keys('your password here')
signin_feild.click()

time.sleep(10)
