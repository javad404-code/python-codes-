text=input()
sentences=text.split('.')
result=[]
w_count=1 
for sentence in sentences:
    words=sentence.split()
    for word in words:
        if word[0].isupper() and word != words[0]:
            result.append((word,w_count))
        w_count+=1 
if len(result)>0:
    for word,index in result :
        print(f'{index}:{word}')
else :
    print('None')
 


              







    