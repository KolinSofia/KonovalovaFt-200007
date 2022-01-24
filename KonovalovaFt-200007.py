import sys
import msvcrt as m

#Вспомогательная функция для определения целочисленности
def convertToInt(x):
    try:
        x = int(x)
    except Exception:
        return -1
    return x
#Ввод отношений критериев в матрицу x*x
def inputTable(table, x):
    #Ввод отношений для верхней половины матрицы, считая от главной диагонали
    for i in range(x):
        for j in range(x):
            if (i == j):
                table[i][j] = 1 #Элементы главной диагонали равные единице
            if (i < j):
                while table[i][j] == 0: #Для выхода из цикла ввода элемента ожидается число, удовлетворяющее условиям
                    temp = input("Введите целочисленное отношение критерия {0} к критерию {1} ".format(i+1, j+1))
                    temp = convertToInt(temp)
                    if (temp == -1) or (1 <= temp <= 9) == False: #Проверка на соответствие условиям
                        print('Введеное отношение некорректно, введите целочисленное значение от 1 до 9')
                    else:
                        table[i][j] = temp
    #Отражение матрицы по главной диагонали и возведение её элементов в -1 степень
    for i in range(x):
        for j in range(x):
            if (i > j):
                table[i][j] = 1/table[j][i]
    return table
#Вывод матрицы
def outputTablePrecise(table, x):
    for i in range(x):
        for j in range(x):
            print("{0:.4f}".format(table[i][j]), end=" ")
        print()
#Cуммирование всех элементов
def tableSum(table, x):
    sum = 0
    for i in range(x):
        for j in range(x):
            sum += table[i][j]
    return sum
#Расчёт коэффициентов
def countWQ(table,x,sum):
    columnsum = 0
    arrayA  = list()
    #расчёт суммы отношений для каждого критерия
    for i in range(x):
        for j in range(x):
            columnsum += table[j][i]
        arrayA.append(columnsum/sum)
    return arrayA

x = 0
#Ввод количества критериев
while x == 0: #Цикл будет запрашивать ввод, пока количество не будет целым числом, превосходящим 0
    x = input("Введите количество оценочных критериев: ")
    x = convertToInt(x)
    if (x == -1) or (x < 1):
        print("Количество критериев должно целым числом, превосходящим 0")
        x = 0
a = [[0] * x for i in range(x)]
a = inputTable(a,x)
print("\nМатрица сравнения по парам: ")
outputTablePrecise(a,x)
a_sum = tableSum(a,x)
print("\nСумма элементов матрицы: {0:.4f}".format(a_sum))
WQ = countWQ(a,x,a_sum) #Создание массива, хранящего весовые коэффициенты
WQ.reverse()
print("Весовые коэффициенты:", end=" ")
for elem in WQ:
    print("{0:.2f}".format(elem), end=" ") #Форматирование вывода
m.getch()
sys.exit() 
