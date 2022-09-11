from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
browser.get('https://www.emag.ro/')
get_element = browser.find_element(by=By.ID, value="searchboxTrigger")
get_element.send_keys('iphone 13')
get_element.submit()

find_element = browser.find_element(by=By.ID, value="card_grid")
print(find_element.text)

for i in range(1, 2):
    browser.find_element = by=By.XPATH, value=f'//*[@id="card_grid"]/div[{i}]/div/div/div[4]/div[2]/form/button'.click()
    # find_element = browser.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[{i}]/div/div/div[4]/div[2]/form/button').click()
    # print(find_element.text)
    # print('***************')