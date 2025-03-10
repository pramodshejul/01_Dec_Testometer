import time   #Window Handle  - Samjay kumar code

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
driver.implicitly_wait(15)

time.sleep(5)
driver.switch_to.alert.dismiss()
parent_handle = driver.current_window_handle
print(parent_handle)
driver.find_element(By.XPATH,'//span[@style="font-size: 14px; font-weight: 500; color: rgb(37, 99, 235);"]').click()
all_handles = driver.window_handles
print(all_handles)

for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH, "//input[@class='yt-sme-mobile-input required_field email-login-box']").send_keys("pramod")
        time.sleep(7)
        driver.close()
        break
driver.switch_to.window(parent_handle)
driver.find_element(By.XPATH,'//span[@style="font-size: 14px; font-weight: 500; color: rgb(37, 99, 235);"]').click()
time.sleep(8)
