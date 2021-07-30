from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(executable_path= 'E:\\EngSoft\\Cursos\\Udemy\\Web Scraping for Data Science - Python & Selenium - Basics\\Drivers\\chromedriver.exe')
driver.get('https://www.yelp.com/search?find_desc=dentists&find_loc=San+Francisco%2C+CA&ns=1')

driver.maximize_window()
time.sleep(10)

# accept cookies
cookies = driver.find_element_by_id('onetrust-accept-btn-handler')
cookies.click()

# names
names =driver.find_elements_by_xpath('//h4[@class="css-1l5lt1i"]/span/a')

# telephone
telephone = driver.find_elements_by_xpath('//div[@class=" container__09f24__2th0K padding-l2__09f24__1jCR9 border-color--default__09f24__3Epto text-align--right__09f24__2w_vG"]/div/div/div/p')

# address
address = driver.find_elements_by_xpath('//address//span[@class=" raw__09f24__3Azrj"]')

# expertise
expertise = driver.find_elements_by_xpath('//div[@class=" border-color--default__09f24__3Epto"]/div/div/div/p')

# stars
stars = driver.find_elements_by_xpath('//div[@class=" attribute__09f24__1La1D display--inline-block__09f24__3SvIn margin-r1__09f24__3PebR border-color--default__09f24__3Epto"]/span/div')

# rating count
rating_count = driver.find_elements_by_xpath('//span[@class="reviewCount__09f24__3GsGY css-e81eai"]')

#for r in rating_count:
#    print(r.text)

#for s in stars:
#    print(s.get_attribute('aria-label'))

dentist_example = pd.DataFrame(columns=['Name', 'Phone', 'Address'])

print(dentist_example)

'''
Empty Lists

1. Loop through the results
2. Append the results in a list
3. Use this lists as the "value-pair" part for the dictionary (Remember: Dictionaries consist of Key-Value Pairs)
3. Hand this Dictionary over to the Pandas Dataframe
'''

names_list = []
phone_list = []
address_list = []
expertise_list =[]
stars_list = []
rating_count_list = []

'''Loop and Append to List'''

for n in names:
    names_list.append(n.text)

for t in telephone:
    phone_list.append(t.text)

for a in address:
    address_list.append(a.text)

for e in expertise:
    expertise_list.append(e.text)

for s in stars:
    stars_list.append(s.get_attribute('aria-label'))

for r in rating_count:
    rating_count_list.append(r.text)

'''Dictionary'''

dent_dictionary = {'Name': names_list, 'Phone': phone_list, 'Address': address_list, 'Expertise': expertise_list,
                  'Stars': stars_list, 'Rating_Count': rating_count_list}

df = pd.DataFrame.from_dict(dent_dictionary)

# dataframe before cleaning
print(df)

#Clean the Data
df['Stars'] = df['Stars'].apply(lambda x: x.replace('star rating', ''))

#Save Data in Excel
df.to_excel('data_done.xlsx', index= False)
