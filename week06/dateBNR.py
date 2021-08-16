import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
link = BeautifulSoup(r.text, "html.parser")

title = link.find_all('div', attrs={'class': 'contentDiv'})
header = []
data_list = []
for i in title:
    for tr_index in i.find_all('table'):
        for td_index in tr_index.find_all('tr'):
            if td_index.find_all('th'):
                header = [th_index.get_text() for th_index in td_index.find_all('th')]
            td_list = [trd_index.get_text().lstrip('   ') for trd_index in td_index.find_all("td")]
            data_list.append(td_list)

df = pd.DataFrame(data_list, columns=header)
df.to_csv('CursBNR.xls', header=header)
