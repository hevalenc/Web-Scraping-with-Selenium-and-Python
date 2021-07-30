from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('E:\\EngSoft\\Cursos\\Udemy\\Web Scraping for Data Science - Python & Selenium - Basics\\Drivers\\chromedriver.exe')

driver.get('https://pokemondb.net/pokedex/all')
driver.maximize_window()

# Policy Policy
button = driver.find_element_by_class_name('gdpr-accept')

try:
    button.click()
except:
    pass

#name
pokemon_name = driver.find_elements_by_xpath('//tbody/tr/td[2]')

#type
pokemon_type = driver.find_elements_by_xpath('//tbody/tr/td[3]')

#total
pokemon_total = driver.find_elements_by_xpath('//tbody/tr/td[4]')

#HP
pokemon_hp = driver.find_elements_by_xpath('//tbody/tr/td[5]')

#Attack
pokemon_attack = driver.find_elements_by_xpath('//tbody/tr/td[6]')

#Defense
pokemon_defense = driver.find_elements_by_xpath('//tbody/tr/td[7]')

#Sp.Atk
pokemon_sp_attack = driver.find_elements_by_xpath('//tbody/tr/td[8]')

#SP.Def
pokemon_sp_defense = driver.find_elements_by_xpath('//tbody/tr/td[9]')

#Speed
pokemon_speed = driver.find_elements_by_xpath('//tbody/tr/td[10]')

pokemon_results = []

for i in range(len(pokemon_name)):
    pokemon_dictionary = {'Name': pokemon_name[i].text,
                          'Type': pokemon_type[i].text,
                          'Total': pokemon_total[i].text,
                          'HP': pokemon_hp[i].text,
                          'Attack': pokemon_attack[i].text,
                          'Defense': pokemon_defense[i].text,
                          'Sp.Attack': pokemon_sp_attack[i].text,
                          'Sp.Defense': pokemon_sp_defense[i].text,
                          'Speed': pokemon_speed[i].text}

    pokemon_results.append(pokemon_dictionary)

dataframe_pokemon = pd.DataFrame(pokemon_results)

print(dataframe_pokemon)
print()

#replace '\n' with '/'
dataframe_pokemon['Name'] = dataframe_pokemon['Name'].apply(lambda x: x.replace ('\n', '/'))

dataframe_pokemon['Type'] = dataframe_pokemon['Type'].apply(lambda x: x.replace ('\n', ','))

# updated dataframe
print(dataframe_pokemon)

dataframe_pokemon.to_excel('pokemon_database_cleaned.xlsx', index=False)
