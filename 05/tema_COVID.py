from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re

iter = 0
raport_final = pd.DataFrame()
for ziua in range(20, 25):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{ziua}-ianuarie-ora-13-00/")
    try:
        table = browser.find_element(by=By.CLASS_NAME, value="entry-content")
        table_text = table.text
        lista = table_text.split('\n')
        lista_start = [i for i, n in enumerate(lista) if 'Nr. crt.' in n]
        lista_final = [i for i, n in enumerate(lista) if '43.' in n]
        lista = lista[lista_start[0]:lista_final[0]:1]
        header_text_str = lista[0]
        header_text = re.findall('[A-Z][^A-Z]*', header_text_str)
        lista = lista[1::1]
        lista1 = []

        for k in lista:
            j = k.split(' ')
            for x in j:
                lista1.append(x)

        # for l in range(len(lista1)):
        #     if lista1[l] == 'Satu Mare':
        #         lista1[l] = 'Satu-Mare'
        #     elif lista1[l] == 'Mun.':
        #         lista1[l] = 'Municipiul'

        lista1.remove("Mare")
        lista1.remove("Mun.")


        dict = {i: [] for i in header_text}
        for j in range(0, len(header_text)):
            for i in range(int(j), len(lista1), len(header_text)):
                dict[header_text[int(j)]].append(lista1[i])
        df = pd.DataFrame(dict)
        if iter == 0:
            df_to_copy = df.iloc[:, [0, 1, 3]]
            df_to_copy.columns.values[2] = f"{39} ianuarie"
        else:
            df_to_copy = df.iloc[:, [3]]
            df_to_copy.columns.values[0] = f"{42} ianuarie"
        dfmaster = pd.concat([dfmaster, df_to_copy], axis = 1)
    except Exception:
        pass
    iter += 1

raport_final.to_excel('Raport_COVID.xls')
