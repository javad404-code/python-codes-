import random 

class human():
    def __init__(self,name=str):
        self.name=name
class footballer(human):
    def __init__(self,name=str):
        super().__init__(name)
        self.team=None 
    def __repr__(self):
       return f'{self.name}{self.team}'
    
def main():
    
        players=[
'حسین','مازیار','اکبر','نیما ','مهدی','فرهاد','محمد',
'خشایار','میلاد ','مصطفی','سعید','پویا','پوریا',
'رضا','علی ','بهزاد ', 'سهیل ',
'بهروز','شهروز','سامان','محسن']

        random.seed(42)

        footballers=[footballer(name) for name in players] 

        random.shuffle(footballers)
        for idx,player in enumerate(footballers):
            player.team=('A') if idx < 11 else ('B')
        for p in footballers:
            print(f'{p.name}{p.team}')
if__name__='__main__'
main()



    




