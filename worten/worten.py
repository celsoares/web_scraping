#pip install requests
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import math


link="https://www.worten.pt/pequenos-eletrodomesticos/aspiradores/aspiradores-robo"

head={
    'user-agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

site=requests.get(link, headers=head)
print(site.status_code)
#colocar o conteudo da página de forma que a biblioteca possa trabalhar
cont=BeautifulSoup(site.content, 'html.parser')

#ver numero de elementos a ver
qtd_cont=cont.find('span', class_='js-filters-total').getText()
qtd=qtd_cont.split("\xa0")
print(qtd)
qtd=qtd[0]
print(qtd)
#determinar a ultima página com 48 artigos por pagina
ultima_pagina=math.ceil(int(qtd)/48)


for pag in range(1, ultima_pagina+1):
    novo_link=f"https://www.worten.pt/pequenos-eletrodomesticos/aspiradores/aspiradores-robo?page={pag}"
    site=requests.get(link, headers=head)
    cont=BeautifulSoup(site.content, 'html.parser')

    produtos = cont.find_all("div", class_="w-product__wrapper")
    #print(produtos)
    print("------------>Pagina: ", pag, "total rpodutos", len(produtos))
    for produto in produtos:
        desc=produto.find("h3", class_="w-product__title").get_text()
        preco=produto.find('span', class_="w-product-price__main").get_text()
        #gravar num ficheiro
        with open ("aspitadores.csv", "a", encoding="utf_8") as file:
            file.write(f"{desc};{preco}\n")
        #print(desc)
        #print (preco)
