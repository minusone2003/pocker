# made by ToivoTech™
# да мне похуй, что манера кода клоунская, пишу, как хочу
# вся это поеботня написана на телефоне в 4 часа ночи перед сессией
from random import shuffle
from time import sleep
import os


# ахует' робит
# небольшая функция для 'красивого' вывода
def cls():  # очистка экрана
    os.system('cls')


def out(time):
    sleep(time)
    cls()


def print_array(arr):
    for i in arr:
        print(i)


'''генерация колоды - 1 число номинал, второе масть(aue)'''

stuck = []  # колода
for i in range(52):
    stuck.append([i // 4, i % 4])
shuffle(stuck)  # перемешивание колоды


# визуализация
def print_card(arr):
    a = ['Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет',
         'Дама', 'Король', 'Туз']
    b = ['Черви', 'Буби', 'Черви', 'Крести']
    print(a[arr[0]], b[arr[1]])
    return


'''Раздача карт'''

desk = []
table = stuck[-1]  # карты на столе

# TODO: нужно ли убирать карты из колоды?

while True:
    player_count = int(input('Введите количество игроков (максимум 4):'))
    player_count = 4
    if player_count > 4:
        print('Сука, это покер, а не групповая маструрбация')
        print('   Введите количество игроков (максимум 4)\n')
    else:
        break

for i in range(player_count):
    desk.append(stuck[:2])
    stuck = stuck[2:]

desk.append(stuck[:5])  # все карты принимающие участие в раздаче(руки + стол)

'''for i in  desk:
	for j in i:
		print_card(j)'''


# начинается жопа
# автозаполнение очков по наилучшей комбинации
def fill(arr):
    for i in range(player_count):
        if arr[i] > scores[i]:
            scores[i] = arr[i]


# каждая комбинация дает некое количество очков
scores = [0 for i in range(player_count)]


def hight_card(list):
    '''старшая карта 100+x'''
    return max(list[0][0], list[1][0]) + 100


# паралельно провдим его и для карт на столе, чтобы убрать лишние комбинации

def same(list: list):
    '''пара,тройка,сет алгоритм 2.0(28)'''
    list.sort(key=lambda a: a[0], reverse=True)
    for i in range(len(list)):
        list[i] = list[i][0]
    start = 0
    stop = 1
    flag = True
    while flag:
        print(start, stop, len(list), sep='   ')
        if list == [] or stop == len(list):
            list[start:stop:1] = [[list[start] for i in range(stop - start)]]

            flag = False
        else:
            # print(start,stop,len(list),sep='   ')
            if list[start] == list[stop]:
                stop += 1
            else:
                list[start:stop:1] = [[list[start] for i in range(stop - start)]]
                print(list)
                start += 1
                stop = start + 1

    list.sort(key=lambda i: len(i), reverse=True)
    # в комбинации участвует 5 карт, поэтому нужно отсечь 2 пследние каки
    s = 0
    for i in range(len(list)):
        s += len(list[i])
        if s >= 5:
            list = list[:i + 1:]
            break
    list[i] = [list[i][0] for j in range(5 - s + len(list[i]))]

    # ветка ифов для определения комбо (другого сбособа не придумал)

    if len(list[0]) == 4:
        end = list[0][0] + 800  # Каре(800)
    elif len(list[0]) == 3 and len(list[1]) == 2:
        end = list[0][0] * 1.3 + list[1][0] + 700  # фуллхаус(700)
    elif len(list[0]) == 3:
        end = list[0][0] + 400  # трипс(400)
    elif len(list[0]) == 2 and len(list[1]) == 2:
        end = list[0][0] * 1.3 + list[1][0] + 300  # 2 пары или +170р(300)
    elif len(list[0]) == 2 and len(list[1]) == 1:
        end = list[0][0] + 200  # (шм)пара (200)
    # сука андрей ты мне до сих пор 90р торчишь
    return end


def in_row(list: list):
    '''стрит стритфлеш, флеш и роял флеш(нет блять,клеш рояль)'''
    count = 1
    pre = []
    list.sort(key=lambda a: a[0], reverse=True)
    print(list)
    for i in range(1, len(list)):
        if count == 5:
            pre.append(list[i])

            break
        elif list[i][0] == list[i - 1][0] - 1:
            count += 1

            pre.append(list[i - 1])
            if i + 1 == len(list):
                pre.append(list[i])
        elif list[i][0] == list[i - 1][0]:
            pre.append(list[i - 1])
            if i + 1 == len(list):
                pre.append(list[i])

        else:

            pre.clear()
            count = 1
    print(count, pre, sep='  ')
    if count == 5:
        if list[0][0] == 12 and list[-1][0] == 0:
            pre.append(list[0][0])

        suit = pre[0][1]
        stritflash = True
        for i in pre:
            if i[1] != suit:
                stritflash = False

        if stritflash and pre[0][0] == 12:
            end = 1000  # как получишь, позвони
        elif stritflash:
            end = pre[0][0] + 900
        else:
            end = pre[0][0] + 500


def flesh(list: list):
    '''Просто флеш'''
    end = 0
    list.sort(key=lambda i: i[1], reverse=True)
    pre = []
    count = 0
    for i in range(1, len(list)):
        if count == 4:
            list.append(list[i])
            break
        elif list[i - 1][1] == list[i][1]:
            count += 1
            pre.append(list[i - 1])
        else:

            pre.clear()
            count = 0
    if count == 4:
        end = 600 + pre[0][0]
    return end


combo = [hight_card, same, in_row, flesh]
table = desk[-1]

#print_array(desk[:-1])
for hand in range(len(desk) - 1):  # применяем все функции ко всем рукам()
    for func in combo:
        if func != 'hight_card':  # хотел сделать через декоратры? А ебись оно в рот!
            t = desk[hand].copy()
            t.extend(table)
            scores[hand] = func(t)
        else:
            t = desk[hand].copy()
            scores[hand] = func(t)

print(scores)


# илья, ещё раз такую хуйню напишешь и все узнают что ты на бабанова по ночам дрочишь
#ветка шпака
