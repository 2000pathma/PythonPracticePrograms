word='Priya'
count=len(word)
for terms in range(len(word)):
    for letter in range(count):
       print(word[letter],end='')
    count=count-1   
    print()
    
