from bs4 import BeautifulSoup
import requests

adres='https://divar.ir/s/tehran'
headres= { 'User-Agent': 'Mozilla/5.0'}

respond=requests.get(adres,headres)
s = BeautifulSoup(respond.text,'html.parser')

ad = s.find_all('div', class_='kt-post-card__body')


for w in ad :
    tag=w.find('p',class_='kt-unexpandable-row__value')
    if tag and 'توافقی'  in tag.text :
       

        title_tag=w.find('h2')
        if title_tag: 
            print(title_tag.text)






