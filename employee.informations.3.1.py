import mysql.connector
mydb=mysql.connector.connect(
user='root',
password='0250477351javad',
host='127.0.0.1',
database='people'
)
cursor=mydb.cursor()
cursor.execute('SELECT * FROM people ORDER BY Height DESC,Weight ASC')
result=cursor.fetchall()
for x in result:
    print(f'{x[0]} {x[1]} {x[2]}')


mydb.close()

      



    



