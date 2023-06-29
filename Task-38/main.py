import functions

myChoise = -1
fileTel = 'tel.txt'

#Создаем файл если его нет
with open(fileTel, 'a', encoding='utf-8') as file:
    file.write('')

while myChoise != 0:
    print('Выберите одно из действий: ')
    print('1 - Вывести информацию на экран')
    print('2 - Произвести экспорт данных')
    print('3 - Произвести изменение данных')
    print('4 - Произвести удаление данных')
    print('0 - Выход из программы')

    action = int(input('Дейстие: '))

    if action == 1:
        functions.showData(fileTel)
    elif action == 2:
        functions.exportData(fileTel)
    elif action == 3:
        functions.editData(fileTel)
    elif action == 4:
        functions.deleteData(fileTel)
    elif action == 0:
        print('До свидания!')
        exit()