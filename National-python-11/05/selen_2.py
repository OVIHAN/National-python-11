from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import openpyxl



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://bnr.ro/files/xml/nbrfxrates2021.htm')

table_head = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead')
print(table_head.text)
table_body = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/tbody')
print(table_body.text)

header = table_head.text.split('\n')
body = table_body.text.split('\n')

# print(header)
# print(body)

body_rows = []
counter = 0
for i in range(0, len(body), len(header)):
    counter = i
    body_rows.append(body[counter: counter + len(header)])

body_columns = {key: [] for key in range(len(header))}

df = pd.DataFrame(body_columns)
df.to_excel("CursBnr.xls", header=header)


