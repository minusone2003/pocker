#made by govnyak productions™
#да мне похуй, что манера кода клоунская, пишу, как хочу
#вся это поеботня написана на телефоне в 4 часа ночи перед сессией
from random import randint, shuffle

#генерация колоды - 1 число номинал, второе масть(aue) 

stuck=[I for I in range(52)]
for i in range(52):
    stuck[i]=[i//4,i%4]
shuffle(stuck)



# визуализация
def vi(arr):
    a=['Двойка','Тройка','Четверка','Пятерка','Шестерка','Семерка','Восьмерка','Девятка','Десятка','Валет','Дама','Король','Туз']
    b=['Черви','Буби','Черви','Крести']
    print(a[arr[0]],b[arr[1]])
    return 

#ахует' робит
#небольшая функция для 'красивого' вывода
def out(obj):
    print('\n' *50)
    print('         ',obj)
    print('\n' *25)
def pprint(arr):
    for i in arr:
        print(i)
#раздача карт
desk=[]
flag=True
while flag:
    n_player=int(input('Введите количество игроков (максимум 4)'))
    if n_player>4:
        out('Сука, это покер, а не групповая маструрбация')
        print('   Введите количество игроков (максимум 4)\n')
    else:
            flag=False
for i in range(n_player):
    desk.append(stuck[:2])
    stuck=stuck[2:]
    
desk.append(stuck[:5])
#pprint(desk)

'''for i in  desk:
    for j in i:
        vi(j)'''
#начинается жопа
#автозаполнение очков по наилучшей комбинации
def fill(arr):
    for i in range(n_player):
        if arr[i]>scores[i]:
            scores[i]=arr[i]




 
#каждая комбинация дает некое количество очков
scores=[0 for i in range(n_player)]
pre=[]
pre=[]
past=[]
prescores=[]




#старшая карта 100+x
for i in range(len(desk)-1):
    for j in desk[i]:
        pre.append(j[0])
for i in range(n_player):
    pre[i]=max(pre[2*i],pre[2*i-1])+100
fill(pre)




#robit
#пара,тройка,сет алгоритм 2.0(28)
prescores=[0 for i in range(n_player)]

for j in desk[i]:
    pre.append(j[0])
for j in desk[-1]:
    pre.append(j[0])
pre=[2,2,3,3,3,4,4]
pre.sort(reverse=True)
print(pre,'!!')


current=0
#ебать что щас замучу
past = []
b = 0
pre1 = []
for i in range(len(pre)):
    if pre[i] == pre[b]:
        pre1.append(pre[i])
    else:
        past.append(pre1)
        b = i
        pre1 = [pre[i]]
past.append(pre1)
print(past)    
past.sort(key=lambda i: len(i), reverse=True)







# в комбинации участвует 5 карт, поэтому нужно отсечь 2 пследние каки
s = 0
for i in range(len(past)):
    s += len(past[i])
    if s >= 5:
        past = past [:i+1: ]
        break
past[i]=[past[i][0] for j in range(5-s+len(past[i]))]
print(past)  
#ветка ифов для определения комбо (другого сбособа не придумал)

if len(past[0])==4:
    prescores[current]=past[0][0]+800 #Каре
elif len(past[0])==3 and len(past[1])==2:
    prescores[current] = past[0][0]*1.3+past[1][0]*0.1+700
print(prescores)
