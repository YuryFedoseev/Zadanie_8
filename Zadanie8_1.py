'''
Открыть файл
  Положить все до пропуска в переменную
  Сделать проверку до пропуска
  
1 элемент сделать ключом
2 элемент игнор
все остальные сделать посточно списком  (опираться на символ |)
Добавить в словарь
Вывести полный словарь
'''
#line = ''
cook_book= {}
food=[]
size=[]
weight=[]
perem=''
n=0
with open('cook.txt','r',encoding='utf8') as document:
    for text in document:
        #perem=''

        
        text = text.strip()
        #line = line + text
        #print(f'text= {text}')
        co=len(text)
        if (co > 4) and ('|' not in text):
            key = text
            n = n + 1
            #print (f'Блюдо: {text}')
        elif '|' in text:
            #co=len(text)
            #print(f'Ингредиенты: {text}')

            up = text.split('|')
            food = up[0]
            size = up[1]
            weight = up[2]
            if (food != 0) and (size != 0) and (weight !=0):
                line = food + size + weight
                #print (f'line= {line}')
            if line != 0:
                if perem != '':
                    pust_str = ' ; '
                    perem = str(perem) + pust_str + str(line)
                else:
                    perem = str(perem) + str(line)
                #pust_str = ' ; '
                #perem = str(perem)+ pust_str +str(line)#тут нужно с новой строки
        if (key!=0) and (perem != 0):
            cook_bo = {key: perem}
            #perem = ''
            print (f'cook_bo= {cook_bo}')
            
'''                
            if (key!=0) and (perem != 0):#вынести на круг выше
                cook_bo = {key: perem}
                print (f'cook_bo= {cook_bo}')
'''                
    #print (perem)    
            #print(f'food= {food}')
            #print(f'size= {size}')
            #print(f'weight= {weight}')
        #cook_book ={key: food + size + weight}
        #print(cook_book)    
            
           
'''        
        if int(text) not in text and '|' not in text:
            print (text)
'''


    
    #print(document.read())
#    for ingridient in document:
#        eat = document.strip[0]
#print(eat)
    
