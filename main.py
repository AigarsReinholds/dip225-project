import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = option)

url = "https://www.cv.lv/"
driver.get(url)

# Filtri
location = "Rīga"
#location2 = "Iespēja strādāt attālināti"
category = "Informācijas tehnoloģijas"
keywords = ['web', 'frontend']
sort_results = "Parādīt jaunākos vispirms"

#atrasanas vieta
location_input = driver.find_element(By.CLASS_NAME, "css-bg1rzq-control")
location_input.click()
location_input_2 = driver.find_element(By.ID, "react-select-2-input")
location_input_2.send_keys(location)
location_input_3 = driver.find_element(By.XPATH, "//div[contains(@class, 'css-dpec0i-option')]")
location_input_3.click()
#darba kategorija
category_input = driver.find_elements(By.CLASS_NAME, "css-bg1rzq-control")[0]
category_input.click()
category_input_2 = driver.find_element(By.ID, "react-select-3-input")
category_input_2.send_keys(category)
category_input_3 = driver.find_element(By.XPATH, "//div[contains(@class, 'css-dpec0i-option')]")
category_input_3.click()
#atslegvardi
keyword_input = driver.find_elements(By.CLASS_NAME, "css-bg1rzq-control")[1]
keyword_input.click()
for keyword in keywords:
  capitalize_keyword = keyword.capitalize()
  keyword_input_2 = driver.find_elements(By.ID, "react-select-2-input")[1]
  keyword_input_2.send_keys(capitalize_keyword)
  keyword_input_3 = driver.find_element(By.CLASS_NAME, "css-dpec0i-option")
  keyword_input_3.click()

#poga papildus filtriem
button_filters = driver.find_element(By.XPATH, "//span[contains(@class,'jsx-2818744897') and contains(@class, 'search-form__additional-toggle')]")
button_filters.click()

#poga rezultatu radisanai
button_results = driver.find_element(By.XPATH, "//span[contains(@class, 'jsx-2818744897') and contains(@class, 'search-form-footer__item')]")
button_results.click()

#sort_options = driver.find_element(By.XPATH, "//div[contains(@class, 'jsx-1778535529') and contains(@class, 'select__dropdown--disabled')]")
#sort_options.click()
#button_sort_newest = driver.find_element(By.XPATH, "//button[contains(@class, 'jsx-1778535529')]")
#button_sort_newest.click()

time.sleep(4)
driver.quit()
