import pandas as pd
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = "https://www.fundamentus.com.br/detalhes.php?papel=ITSA4"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
html = urlopen(Request(url, headers=headers)).read()
soup = BeautifulSoup(html, 'html.parser')

# Extraindo os dados das tabelas
tabelas = soup.find_all('table')
dataframes = {}

for i, tabela in enumerate(tabelas, start=1):
    headers = [th.get_text() for th in tabela.find_all('th')]
    rows = [[td.get_text().strip() for td in row.find_all('td')] for row in tabela.find_all('tr')]
    if headers and rows:
        dataframe = pd.DataFrame(rows[1:], columns=headers) # Ignora a primeira linha se for cabeçalho
    else:
        dataframe = pd.DataFrame(rows)
    dataframes[f'Tabela{i}'] = dataframe

def escolher_tabela(numero):
    nome_tabela = f'Tabela{numero}'
    if nome_tabela in dataframes:
        return dataframes[nome_tabela]
    else:
        return f"Tabela {numero} não encontrada."







