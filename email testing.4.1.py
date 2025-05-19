import re 
def valid_email():
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email=str(input())
    if re.match(pattern,email):
            print('OK')
    else:
            print('WRONG')
valid_email()
        
