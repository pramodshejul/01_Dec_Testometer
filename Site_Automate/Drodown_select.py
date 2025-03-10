# import time
#
# from select import select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# driver= webdriver.Chrome()
# driver.get("https://www.opencart.com/")
# #driver.get("https://www.opencart.com/index.php?route=account/register")
# driver.maximize_window()
# time.sleep(100)
# #drpcountry_ele = driver.find_element(By.XPATH,"//select[@id='input-country']")
#
# drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))
# time.sleep(6)
#
# #select option from the dropdown
# drpcountry.select_by_visible_text("India")
# time.sleep(5)
#
# # drpcountry.select_by_value("10")  #Argentina
# #
# # drpcountry.select_by_index(223)  #United states

#Above dropdown handle code

#################Second website33333333333333333333333#######################################################
# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
#
# from selenium.webdriver.support.select import Select
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
#
# dropdown_ele=select(driver.find_element(By.XPATH,'//select[@id="dropdown-class-example"]'))
# dropdown_ele


# import time
#
# from select import select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# #
# #
# driver= webdriver.Chrome()
#
# driver.get("https://www.shaadi.com/")
# driver.maximize_window()
# time.sleep(10)
# #drpcountry_ele = driver.find_element(By.XPATH,"//select[@id='input-country']")
#
# dropdown_ele=select(driver.find_element(By.XPATH,'//div[@class="PreferenceForm_formGroup__7JJxn col-md-2 col-6'][2]))
# time.sleep(6)
#
# #select option from the dropdown
# drpcountry.select_by_visible_text("")  #"option1"l
# time.sleep(5)

#drpcountry.select_by_value("10") #Argentina

#drpcountry.select_by_index(223)  #United states


#============================================================
import time   #Dropdown Run Successfully  - Samjay kumar code

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft ")
driver.maximize_window()
driver.implicitly_wait(15)

dropdown = driver.find_element(By.XPATH,'//select[@name="UserTitle"]')
dd=Select(dropdown)
time.sleep(5)
dd.select_by_visible_text('Marketing / PR Manager')
time.sleep(6)
dd.select_by_value("CxO_General_Manager_ANZ")
time.sleep(5)
dd.select_by_index(1)
time.sleep(6)




