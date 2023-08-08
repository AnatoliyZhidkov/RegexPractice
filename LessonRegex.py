import re


""" 
nomera = ['С227НА777','КУ22777 ','Т22В7477 ','М227К19У9 ',' С227НА777 ']

def Opredelenie(nomer):
    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', nomer) :
        return 'Private'
    elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{2}\d{2,3}', nomer) :
        return 'Taxi'
    else:
        return 'Fail'

for i in range(0,len(nomera)):
    print(Opredelenie(nomera[i].replace(' ','')))
 
 """




""" text = '''Он --- серо-буро-малиновая редиска!! #
>>>:-> 
А не кот. 
www.kot.ru'''
print(re.findall(r'(?:[A-Za-zА-Яа-яёЁ]+[-]?)+',text)) """



text = ''' Иван Иванович! 
Нужен ответ на письмо от ivanoffffffff@ivan-chai.ru
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно. '''

result = re.findall(r'\b[A-Za-z0-9][0-9A-Za-z._+\'-]{0,62}[A-Za-z0-9]@[A-Za-z0-9][0-9A-Za-z.-]*[A-Za-z0-9]\b',text)
for i in range(len(result)-1,-1,-1):
   if len(result[i][result[i].find('@')+1:]) > 255:
     result.pop(i)
   
print(result)
