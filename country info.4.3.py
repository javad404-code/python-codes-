import mysql.connector
from bs4 import BeautifulSoup
import requests

cnx=mysql.connector.connect(user='root' ,password='0250477351javad',database='chart', host= '127.0.0.1' )
cursor = cnx.cursor()

country_address='https://www.scrapethissite.com/pages/simple/'
headers=headres= { 'User-Agent': 'Mozilla/5.0'}

respond=requests.get(country_address,headres)
all_info_site=BeautifulSoup(respond.text,'html.parser')

all_code_of_country=all_info_site.find_all("div", class_="col-md-4 country")
all_country_count=all_code_of_country[:20]     

for country_information in all_country_count:
   name=country_information.find("h3", class_="country-name").text.strip()
   capital=country_information.find("span", class_="country-capital").text.strip()
   crowd=country_information.find("span", class_="country-population").text.strip()
   size=country_information.find("span", class_="country-area").text.strip()

   sql = 'insert into chart (name,capital,crowd,size) VALUES (%s,%s,%s,%s)'
   val=(name,capital,crowd,size)

   cursor.execute(sql,val)
   cnx.commit()

cursor.close()
cnx.close()



   

    




    

    


