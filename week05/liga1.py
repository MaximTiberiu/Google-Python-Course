import requests
from bs4 import BeautifulSoup

r = requests.get("https://lpf.ro/liga-1")
# print(r)

s1 = BeautifulSoup(r.text, "html.parser")
# print(s1)

f = open("programariliga1.html", "w", encoding="utf-8")

rand = s1.table.find("tr")
f.write("<html><head>Programare</head><body><table><thead><tr style='color:red;'>")
for tr in s1.table.select('tr')[:1]:
    for x in tr.select('td'):
        f.write(f"<th>{x.text}</th>")
f.write('</tr></thead><tbody>')
for tr in s1.table.select('tr')[1:]:
    f.write("<tr>")
    for x in tr.select('td'):
        f.write(f'<td style="background-color: grey; border: 1px solid black">{x.text}</td>')
    f.write("</tr>")
f.write("</tbody></table></body></html>")


