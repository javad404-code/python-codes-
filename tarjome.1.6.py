n=int(input())
dict={}
for _ in range(n):
    word,english,french,german=input().split(' ')
    dict[word]={english,french,german}
s=input()
lst=s.split(' ')
translated=[]
for word in lst :
   found=False 
   for key,values in dict.items():
       if word in values :
          translated.append(key)
          found=True
          break 
   if not found :
         translated.append(word)
print(' '.join(translated))

      


