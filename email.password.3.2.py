import re 
def truth_email():
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    while True:
        email=str(input())
        if re.match(pattern,email):
            return email 
        else:
            print('expression@string.string')
def truth_password():
    while True :
          password=str(input())
          digit=any(char.isdigit() for char in password)
          alpha=any(char.isalpha() for char in password)

          if  digit and alpha:
            return password
def save_to_db(email,password):
        import mysql.connector
        cnx=mysql.connector.connect(
            user='root',
            password='0250477351javad',
            host='127.0.0.1',
            database='info'
        )
        cursor=cnx.cursor()
        sql='insert into info  (username,password)  values (%s,%s)'
        val=email,password

        cursor.execute(sql,val)
        cnx.commit()

        cursor.close()
        cnx.close()

email=truth_email()
password=truth_password()
save_to_db(email,password)




