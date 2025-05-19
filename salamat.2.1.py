class studentgroup():
    def __init__(self,ages,heights,weights):
     self.ages=ages
     self.heights=heights
     self.weights=weights

    def avg_age(self):
        return sum(self.ages) / len(self.ages)
    

    def avg_heights(self):
        return sum(self.heights) / len(self.heights)   


    def avg_weights(self):
        return sum(self.weights) / len(self.weights)
    

def readclass():
    n=int(input())
    ages=list(map(int,input().split()))
    heights=list(map(int,input().split()))
    weghits=list(map(int,input().split()))
    return studentgroup(ages,heights,weghits)

class_A=readclass()
class_B=readclass()

print(class_A.avg_age())
print(class_A.avg_heights())
print(class_A.avg_weights())



print(class_B.avg_age())
print(class_B.avg_heights())
print(class_B.avg_weights())


avg_heights_A=class_A.avg_heights()
avg_heights_B=class_B.avg_heights()

avg_weights_A=class_A.avg_weights()
avg_weights_B=class_B.avg_weights()

if avg_heights_A>avg_heights_B:
    print('A')
elif avg_heights_B>avg_heights_A:
    print('B')
else:
    if avg_weights_A<avg_weights_B:
     print('A')
    elif avg_weights_B<avg_weights_A:
       print('B')
    else:
       print('Same')





