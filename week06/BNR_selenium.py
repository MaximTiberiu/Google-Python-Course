from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pandas as pd

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2019.htm")
table = browser.find_element_by_xpath('//*[@id="Data_table"]')
table_text = table.text
# print(table_text)

lista = table_text.split('\n')
header_len = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}

# print(dictionar)
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        if '-' in lista[i]:
            dictionar[header[int(j)]].append(lista[i])
        else:
            dictionar[header[int(j)]].append(float(lista[i]))
# print(dictionar)

df = pd.DataFrame(dictionar)
df.to_csv("BNR_ALL_DATE.xls")
browser.close()
