from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# relevant websites
website_1 = 'https://www.geekbuying.com/search?keyword=laptop'
website_2 = 'http://automationpractice.com/index.php'

# initialize Chrome
driver = webdriver.Chrome('E:\\EngSoft\\Cursos\\Udemy\\Web Scraping for Data Science - Python & Selenium - Basics\\Drivers\\chromedriver.exe')

# open website
driver.get(website_1)

#maximize window
driver.maximize_window()

'''LOCATORS'''

#Xpath locator
price = driver.find_element_by_xpath('(//li[@class="searchResultItem"]/div/div[3])[1]')

print('\nPrint out the price')
print(price.text)

prices = driver.find_elements_by_xpath('//li[@class="searchResultItem"]/div/div[3]')
print('\nQt of prices: ',len(prices))

print('\nPrint out all price points')
for p in prices:
    print(p.text)

print('\nType of prices: ', type(prices))

#class name locator
names = driver.find_elements_by_class_name('name')

print('\nQt of names: ', len(names))
print('\nType of names: ', type(names))

print('\nPrint out all names points')
for n in names:
    print(n.text)

print('\nprint specific item from the list: ', names[28].text)


driver.get(website_2)
time.sleep(1)
#id locator
search = driver.find_element_by_id('search_query_top')

#click
search.click()
time.sleep(1)
search.send_keys('hellohello')

#name locator
search_button = driver.find_element_by_name('submit_search')
search_button.click()

#link text locator
contact = driver.find_element_by_link_text('Contact us')
contact.click()

#similar to previous step
driver.get(website_2)
driver.maximize_window()
time.sleep(1)

#partial link text locator
contact_partial = driver.find_element_by_partial_link_text('ntact u')
contact_partial.click()

'''
DIFFERENT WAYS TO USE LOCATORS

# Option 1 - XPath Locator
prices = driver.find_elements_by_xpath('//li[@class="searchResultItem"]/div/div[3]')

# Option 1 - ID Locator
search = driver.find_element_by_id('search_query_top')

# Option 2 - XPath Locator
prices_2 = driver.find_elements(By.XPATH('//li[@class="searchResultItem"]/div/div[3]'))

#Option 2 - ID Locator
search_2 = driver.find_elements(By.ID('search_query_top'))
'''
