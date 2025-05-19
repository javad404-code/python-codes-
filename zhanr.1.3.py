genres={'Horror':0,
      'Romance':0,
      'Comedy':0, 
      'History':0,
       'Adventure':0, 
       'Action':0
}
num=int(input())
for numbers in range  (0,num):
    line=input().split(' ')
    f=line[1:]
    for genre in f :
        genre =genre.strip()
        if genre in genres :
            genres[genre]+=1 
sorted_genres=sorted(genres.items(), key=lambda x: (-x[1] , x[0]))
for genre , count in sorted_genres :
    print(genre,':',count )
  


