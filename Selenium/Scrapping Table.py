from selenium import webdriver
import pandas as pd

website = "https://www.adamchoi.co.uk/overs/detailed"
path = '/Users/ayushsingh/Downloads/chromedriver_mac_arm64/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []
for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home = match.find_element_by_xpath('./td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)
driver.quit()

df = pd.DataFrame({'date' : date, 'home_team' : home_team,
              'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index = False)
print(df)