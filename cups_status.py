#Libs necessarias
import requests
from bs4 import BeautifulSoup

#Faz o get das informacoes
link = "http://192.168.112.225:631/printers/"
site_cups = requests.get(link).text
soup = BeautifulSoup(site_cups, 'html.parser')
corpo_tabela = soup.findAll("tbody")

#Limpeza
for elementos in corpo_tabela:
    valores = elementos.findAll("td")

#Lista dos valores com problema
msg = True
array_valores = []
for i in range(4, len(valores), 5):
    if valores[i].text == "Paused - \"Paused\"":
        array_valores.append("{}".format(valores[i-4].text))
        msg = False

#Msg de tudo certo
if msg:
    print(0)
else:
    print("Impressora\\s: {}".format(" - ".join(array_valores)))
