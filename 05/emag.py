from datetime import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')


def search_product(product):
    get_element.send_keys('telefon')
    get_element.submit()

    url = requests.get(browser.current_url)
    page = BeautifulSoup(url.text, 'html.parser')

    data = {}
    counter = 1
    for i in page.find_all('div', attrs={'class': 'card-v2-wrapper'}):
        # print(i)
        product_name = i.find('a', attrs={'class': 'card-v2-title'}).get_text()
        rating_number = i.find('span', attrs={'class': 'average-rating'}).get_text()
        reviews_number = int(i.find('span', attrs={'class': 'visible-xs-inline-block'}).get_text().replace('(' , '').replace(')' , ''))
        price = float(i.find('p', attrs={'class': 'product-new-price'}).get_text().replace(' Lei', '').replace('.', '').replace(',', '.'))
        data[f"product_{counter}"] = {'product_name': product_name, 'rating_number': rating_number, 'reviews_number': reviews_number, 'price': price}
        counter += 1

    print(data, '30')

    titlu_fisier = str(product.title() + str(datetime.now())).replace(':', '_')

    export = pd.DataFrame(data).transpose().to_csv(titlu_fisier, sep=',' ,header=['Product name', 'Rating number', 'Reviews', 'Price'])
    # export_data = pd.DataFrame(data).transpose().to_csv(f'{product.title()}_{str(datetime.datetime.now().date())}.csv', sep=',', header=['Product Name', 'Rating Number', 'Reviews Number', 'Price'])

search_product('Laptop')