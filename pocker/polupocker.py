#made by govnyak productions™
#да мне похуй, что манера кода клоунская, пишу, как хочу
#вся это поеботня написана на телефоне в 4 часа ночи перед сессией
from random import shuffle
import os
from time import sleep
#генерация колоды - 1 число номинал, второе масть(aue) 

stuck=[I for I in range(52)]
for i in range(52):
    stuck[i]=[i//4,i%4]
shuffle(stuck)





# визуализация
def vi(arr):
    a=['Двойка' , 'Тройка' , 'Четверка' , 'Пятерка' , 'Шестерка' , 'Семерка' , 'Восьмерка' , 'Девятка' ,'Десятка' ,'Валет' ,'Дама' ,'Король' ,'Туз']
    b=['Черви','Буби','Черви','Крести']
    print(a[arr[0]],b[arr[1]])
    return 

#ахует' робит
#небольшая функция для 'красивого' вывода
def cls():#очистка экрана
    os.system('cls')
def out(time):
    sleep(time)
    cls()
def pprint(arr):
    for i in arr:
        print(i)
#раздача карт
desk=[]
flag=True
while flag:
    #n_player=int(input('Введите количество игроков (максимум 4)'))
    n_player=4
    if n_player>4:
        print('Сука, это покер, а не групповая маструрбация')
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
#старшая карта 100+x
for i in range(len(desk)-1):
    for j in desk[i]:
        pre.append(j[0])
for i in range(n_player):
    pre[i]=max(pre[2*i],pre[2*i-1])+100
fill(pre)

 #robit
#пара,тройка,сет алгоритм 2.0(28)
pre=[]
past=[]
prescores=[0 for i in range(n_player)]
current=0
for current in range(n_player):
    for j in desk[current]:
        pre.append(j[0])
    for j in desk[-1]:
        pre.append(j[0])

    pre.sort(reverse=True)
    print(pre)




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

    past.sort(key=lambda i: len(i), reverse=True)






    print(past,'!')
    # в комбинации участвует 5 карт, поэтому нужно отсечь 2 пследние каки
    s = 0
    for i in range(len(past)):
        s += len(past[i])
        if s >= 5:
            past = past [:i+1: ]
            break
    past[i]=[past[i][0] for j in range(5-s+len(past[i]))]

    #ветка ифов для определения комбо (другого сбособа не придумал)

    if len(past[0])==4:
        prescores[current]=past[0][0]+800 #Каре(800)
    elif len(past[0])==3 and len(past[1])==2:
        prescores[current] = past[0][0]*1.3+past[1][0]+700  #фуллхаус(700)
    elif len(past[0])==3:
        prescores[current] = past[0][0]+400 #трипс(400)
    elif len(past[0])==2 and len(past[1])==2:
        prescores[current] = past[0][0]*1.3+past[1][0]+300#2 пары или +170р(300)
    elif len(past[0])==2 and len(past[1])==1:
        prescores[current] = past[0][0]+200 #(шм)пара (200)
    #сука андрей ты мне до сих пор 90р торчишь

    #стрит стритфлеш и роял флеш(нет блять,клеш рояль)

    fill(prescores)

    pre.clear()
    for j in desk[i]:
        pre.append(j)
    for j in desk[-1]:
        pre.append(j)



    pre.sort(reverse=True)



    count=0
    pre1.clear()
    for i in range(len(pre)+1):#с учетом того, чт стрит может начаться с туза
        if count==4:
            pre1.append(pre[i%7])
            break
        elif pre[i%7][0]==pre[(i+1)%7][0]+1 or (pre[i%7][0]==0 and pre[(i+1)%7][0]==12):
            count+=1

            pre1.append(pre[i%7])
        else:
            pre1.clear()
            count=0
    #дополнительная проверка на флеш
    try:
        check=pre1[0][1]
    except:
        pass
    flag=True
    for i in pre1:
        if i[1]!=check:
            flag=False


    if count==4:
        if flag and pre1[0][0]==12:
            prescores[current]=1000#как получишь, позвони
        elif flag:
            prescores[current]=pre1[0][0]+900
        else:
            prescores[current]=pre1[0][0]+500




    i=0
    #проста флеш
    pre.clear()
    for j in desk[i]:
        pre.append(j)
    for j in desk[-1]:
        pre.append(j)
    pre.sort()
    pre.sort(key=lambda i:i[1], reverse=True)

    count=0
    for i in range(len(pre)-1):
        if count==4:
            pre1.append(pre[i%7])
            break
        elif pre[i%7][1]==pre[(i+1)%7][1]:
            count+=1
        else:
            pre1.clear()
            count=0
    if count==4:
        prescores[current]=600+pre1[0][0]
    pre.clear()
pprint(desk)
print(scores)
#!!!!!Доработать проверку на пары


#Процедура игры

out(0.5)
print('Made by m1nus0ne')
out(0.5)
print('Покер')
out(1)
print('Именно он')
out(0.5)
print('Это мой первый проект, сделанный через слезы, stuckowerflow, пот и еще раз слезы, \n'
      'Он емеет пару недочетов в оптимизации, некоторых фишек самого покера, но это poxui absolutno')


