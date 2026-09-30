#سوال یک 

def analyse_text():
    text = input('enter text: ')
    words = len(text.split())
    print(f'words: {words}')
    
    letters =0
    for j in text:
        if j.isalpha():
            letters+=1
    print(f'letters: {letters}')
    
    digits=0
    for x in text:
        if x.isdigit():
          digits+=1
    print(f'number of digits: {digits}')
    
    word=text.split()
    most_common_words = max(word, key=word.count)
    print(f'most_common_words: {most_common_words}')
    
    longest_word= max(word,key=len)
    print(f'longest_word: {longest_word}')
    
    shortest_word= min(word,key=len)
    print(f'shortest_word: {shortest_word}')
    
    letters = ''.join(word)
    ml = max(letters.count(i) for i in letters)
    most_common_letters = set( i for i in letters if letters.count(i)== ml)
    print(f'most_common_letters: {most_common_letters}')
    
    for i in word:
     if i == i[::-1]:
      print(f'pilandrome : {i}')
      
    a=0
    b=0
    for i in text:
        if i.isupper():
            a +=1
           
        elif i.islower():   
            b+=1
    print(f'uperrcase:{a}')    
    
    print(f'lowercase:{b}')

       
    
analyse_text()
