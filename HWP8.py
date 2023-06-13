# with open('phone book.txt', 'w', encoding='utf-8') as file:
#     some_list = ['Максимов', 'Кирилл', '89059991122']
#     for word in some_list:
#         file.write(word + '\n')


# with open('phone book.txt', 'a', encoding='utf-8') as file:
#     some_list = ['Петров', 'Иван', '89115678899']
#     for word in some_list:
#         file.write(word + '\n')
#     print('')

# def imp():
#     pass
#
# def exp():
#     pass
#
# mode = input('Введите режим работы: 1 - импортирование, 2 - экспортирование: ')
# if mode == 1:
#     imp()
# elif mode == 2:
#     exp()
# else:
#     print('Некорректный режим работы')


# =====================================================================================

# def show_data(tel_num):
#     with open('tel_num.txt', 'r', encoding='utf-8') as data:
#         print(data.read())
#         print('')

# def export_data(tel_num):
#     with open('tel_num.txt', 'r', encoding='utf-8') as data:
#         tel_num = data.read()
#         num = len(tel_num.split('\n'))
#     with open('tel_num.txt', 'a', encoding='utf-8') as data:
#         surname = input('Введите фамилию: ')
#         name = input('Введите имя: ')
#         phone_number = input('Введите номер телефона: ')
#     data.write(f'{num} | {surname} | {name} | {phone_number}\n')
#     print(f'Добавлена запись : {num} | {surname} | {name} | {phone_number}\n')

# def imp(tel_num):
#     with open('tel_num.txt', 'r', encoding='utf-8') as data:
#         flag = 1
#         name = input('фамилия: ')
#         for line in data:
#             if name in line:
#                 for i in range(2):
#                     flag = 0
#                     print(data.readline()[:-1])
#
#         if flag: print('некорректная фамилия')

print('Введите режим работы: 0 - Вывод всей книги, 1 - импортирование, 2 - экспортирование: ')
mode =int(input("Режим: "))
if mode == 0:
    with open('tel_num.txt', 'r', encoding='utf-8') as data:
        print(data.read())
        print('')
elif mode == 1:
    with open('tel_num.txt', 'r', encoding='utf-8') as data:
        flag = 1
        name = input('фамилия: ')
        for line in data:
            if name in line:
                for i in range(2):
                    flag = 0
                    print(data.readline()[:-1])

        if flag: print('некорректная фамилия')
elif mode == 2:
    with open('tel_num.txt', 'r', encoding='utf-8') as data:
        tel_num = data.read()

    with open('tel_num.txt', 'a', encoding='utf-8') as data:
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        phone_number = input('Введите номер телефона: ')
        data.write(f'{surname}\n{name}\n{phone_number}\n')
        print(f'Добавлена запись : {surname} \n {name} \n {phone_number}\n')
    print('\n')
else:
    print('Некорректный режим работы')