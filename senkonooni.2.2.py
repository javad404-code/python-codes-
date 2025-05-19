from datetime import date,datetime

def mohasebe(date_str):
    try:
        year,month,day=map(int,date_str.split('/'))
        if not month<13 :
         return ('WRONG')
        if not day <32 :
         return ('WRONG')
        d=date(year,month,day)
        return d 
    except ValueError:
       return ('WRONG')

birthday=input()
birthday_date=mohasebe(birthday)

today_time=('2025/04/23')
today_times=mohasebe(today_time)

years=today_times.year - birthday_date.year
months=today_times.month - birthday_date.month
days=today_times.day- birthday_date.day 


print(years)






    




