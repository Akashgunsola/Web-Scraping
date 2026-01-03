from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = 'https://www.google.com'

driver.get(url)
time.sleep(2)

search_bar_xpath = "//textarea[@id='APjFqb']"

search_bar = driver.find_element(by = By.XPATH, value = search_bar_xpath)

search_bar.send_keys("machine learning")
time.sleep(5)



search_bar.send_keys(Keys.ENTER)

input('Captcha Detected solve your captha')


btn = '/html/body/div[3]/div/div[12]/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/span/a/h3'

link = driver.find_element(by=By.XPATH, value = btn)

link.click()
time.sleep(5)
