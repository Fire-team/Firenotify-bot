import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = 'https://interwencje.straz.lodz.pl'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')


title = soup.find('title').text
tables = soup.find_all("table")


table = None
for t in tables:
    header_row = t.find("tr")
    header_columns = header_row.find_all("th")
    column_names = [col.get_text(strip=True) for col in header_columns]
    if "Data zgłoszenia" in column_names and "Data zakończenia" in column_names:
        table = t
        break

rows = table.find_all("tr")


print(title)


data = []
data_rows = rows[1:]
for row in data_rows:
    row_data = []
    columns = row.find_all("td")
    for col in columns:
        row_data.append(col.get_text(strip=True))
    data.append(row_data)


print(tabulate(data, headers=column_names, tablefmt="grid"))
