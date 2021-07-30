from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')

website = 'http://automationpractice.com/index.php'

'''SELENIUM IN ACTION - Chrome will opens'''

# open website
driver = webdriver.Chrome(executable_path='E:\\EngSoft\\Cursos\\Udemy\\Web Scraping for Data Science - Python & Selenium - Basics\\Drivers\\chromedriver.exe')
driver.get(website)
time.sleep(1)

#send keys and click on button
search = driver.find_element_by_id('search_query_top')
search.click()
time.sleep(1)

# type a text inside the search bar
search.send_keys('hello')
time.sleep(1)

# submit your search request
search_button = driver.find_element_by_name('submit_search')
search_button.click()

#go back
driver.back()
time.sleep(1)

# click Contact us - Link Text Locator
contact_us = driver.find_element_by_link_text('Contact us')
contact_us.click()
time.sleep(1)

# close driver at the end
driver.close()

chrome_options = Options()
chrome_options.add_argument('--headless')

'''Run everything in one Step - Headless'''

# open website
driver = webdriver.Chrome(executable_path='E:\\EngSoft\\Cursos\\Udemy\\Web Scraping for Data Science - Python & Selenium - Basics\\Drivers\\chromedriver.exe', options=chrome_options)
driver.get(website)
time.sleep(1)

print('Website was opened')

#send keys and click on button
search = driver.find_element_by_id('search_query_top')
search.click()
time.sleep(1)

# type a text inside the search bar
search.send_keys('hello')
time.sleep(1)

print('A text was typed inside the search bar')

# submit your search request
search_button = driver.find_element_by_name('submit_search')
search_button.click()

print('Search Request was submitted')

#go back
driver.back()
time.sleep(1)

print('Go back to Initial Page')

# click Contact us - Link Text Locator
contact_us = driver.find_element_by_link_text('Contact us')
contact_us.click()
time.sleep(1)

print('Contact Us button was clicked using the Link Text Locator')

# close driver at the end
driver.close()

print('Driver was closed - Bye Bye')