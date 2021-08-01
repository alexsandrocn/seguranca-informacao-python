from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteudo da requisição http do site
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html
print(soup.prettify())
#transforma html em string e o print via exibir o html
#temperatura = soup.find(class_="-gray _flex _align-center")

print (temperatura.string)

print(soup.title.string)

print(soup.p.string)
