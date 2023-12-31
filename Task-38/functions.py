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
# Изменяет информацию из файла
def editData(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

#Удаление информации из файла
def deleteData(filename):
    print("\nПП | ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))