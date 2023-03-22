word='PRIYA '
count=len(word)
terms=1
for terms in range(len(word)):#terms---->row
    for letter in range(terms):#letter--->column
       print(word[letter],end='')
    count=count+1   
    print()
    
