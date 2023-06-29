#Показывает инфрмацию в файле
def showData(fileName):
    print('\nПП | ФИО | Телефон')
    with open(fileName, 'r', encoding='utf-8') as data:
        print(data.read())
    print('')

#Записывает информацию в файл
def exportData(fileName):
    with open(fileName, 'r', encoding='utf-8') as data:
        tel_file = data.read()
    num = len(tel_file.split('\n'))

    with open(fileName, 'a', encoding='utf-8') as data:
        fio = input('Введите ФИО: ')
        phoneNumber = input('Введите номер телфона: ')
        data.write(f'{num} | {fio} | {phoneNumber}\n')
        print(f'Добавлена запись: {num} | {fio} | {phoneNumber}\n')

#Изменение информации в файле
def editData(fileName):
    print('\nПП | ФИО | Телефон')
    with open(fileName, 'r', encoding='utf-8') as data:
        telBook = data.read()
        print(telBook)
        print('')
        indexDeleteData = int(input('Введите номер строки для редактирования: ')) - 1
        telBookLines = telBook.split('\n')
        editTelBookLines = telBookLines[indexDeleteData]
        elements = editTelBookLines.split('\n')
        fio = input('Введите фамилию: ')
        phone = input('Введите номер телефона: ')
        num = elements[0]
        if len(fio) == 0:
            phone == elements[2]
        editLine = f'{num} | {fio} | {phone}'
        telBook[indexDeleteData] = editLine
        print(f'Запись {editTelBookLines} изменена на {editLine}\n')
        with open(fileName, 'w', encoding='utf-8') as f:
            f.write('\n'.join(telBookLines))

#Удаление информации из файла
def deleteData(fileName):
    print('\nПП | ФИО | Телефон')
    with open(fileName, 'r', encoding='utf-8') as data:
        telBook = data.read()
        print(telBook)
    print('')
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))