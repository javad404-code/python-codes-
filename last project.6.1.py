import pandas as pd
from sklearn.linear_model import LinearRegression
from bs4 import BeautifulSoup
import requests
import mysql.connector

cnx=mysql.connector.connect(user='root',password= '0250477351javad',database='web',host='127.0.0.1')
cursor=cnx.cursor()

web_addres='https://www.scrapethissite.com/pages/simple/'
headers={ 'User-Agent': 'Mozilla/5.0'}

respond=requests.get(web_addres,headers)
info=BeautifulSoup(respond.text,'html.parser')

all_code=info.find_all("div", class_="col-md-4 country")
chart=all_code[:20]

for all_information in chart :
       name=all_information.find("h3", class_="country-name").text.strip()
       capital=all_information.find("span", class_="country-capital").text.strip()
       poplution=all_information.find("span", class_="country-population").text.strip()
       area=all_information.find("span", class_="country-area").text.strip()
       sql='insert into web (name,capital,poplution,area) values (%s,%s,%s,%s)'
       val=(name,capital,poplution,area)   
       cursor.execute(sql,val)

cursor.execute('select poplution,area from web where  poplution >0 and area >0 ')
rows=cursor.fetchall()
df=pd.DataFrame(rows, columns=["poplution", "area"])
df["poplution"] = df["poplution"].astype(float)
df['area'] = df['area'].astype(float)

model=LinearRegression()
model.fit(df[["poplution"]],df["area"])

cursor.execute('select  name,poplution from web where poplution>0 and area= 0 ' )
mis_rows= cursor.fetchall()

for name,poplution in mis_rows:
       rem_area=model.predict([[float(poplution)]])[0]
       cursor.execute("UPDATE web SET area = %s WHERE name = %s", (rem_area, name))
       print(f'{name}{rem_area:.2f}')

cnx.commit()
cursor.close()
cnx.close()

