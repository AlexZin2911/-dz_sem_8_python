import student_info as si
import cabinet_info as cab
import os.path

FILE_NAME = 'text.txt'

def option():
    print("\nВас приветствует программа мониторинга процессов обучения учеников нашей школы!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID ученика по фамилии \n \
    2: Посмотреть класс и место которое занимает ученик \n \
    3: Оценки\n \
    4: Выход\n \
    Ваш выбор: '))
# Поиск ученка
    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(Surn)
        print(f"{si.stud_card['ID'][index]}, {si.stud_card['Имя'][index]},{si.stud_card['Фамилия'][index]}\n,{si.stud_card['Дата рождения'][index]}, {si.stud_card['Успеваемость'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()
# Какое место занимает
    elif ch == 2:
        c = input('Введите ID ученика для вывода по классам: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(f" Сидит в классе - {cab.class_card['Предмет'][index]}\n\, за партой номер - {cab.class_card['Номер парты'][index]}, это {cab.class_card['Ряд'][index]}, парта - {cab.class_card['Вид парты'][index]}, Имя: {si.stud_card['Имя'][index]}, Фамилия - {si.stud_card['Фамилия'][index]}, и успеваемасть ученика: {si.stud_card['Успеваемость'][index]}")
            print('\nХотите выполнить другую операцию??? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
# Оценки
    elif ch == 3:
        while True:
            choice = input('1-Просмотреть оценки\n2-Изменить оценки\n3-Удаление оценок\n4-Выход\nВаш выбор - ')
            # вывод
            if choice == '1':
                if os.path.isfile(FILE_NAME):
                    with open(FILE_NAME, 'r') as file:
                        journal = file.read()
                        if journal:
                            journal = eval(journal)
                            for student, lessons in journal.items():
                                print(student)
                                for lesson, mark in lessons.items():
                                    print(lesson, mark, sep=' - ')
                        else:
                            print('Файл пустой')
                else:
                    print('Файл не существует')
            # ввод
            elif choice == '2':
                if os.path.isfile(FILE_NAME):
                    with open(FILE_NAME, 'r') as file:
                        journal = file.read()
                    if journal:
                        journal = eval(journal)
                    else:
                        journal = {}
                    student = input('Введите имя ученика:')
                    lesson = input('Введите предмет:')
                    mark = input('Введите оценку:')
                    if student in journal:
                        journal[student].update({lesson: mark})
                    else:
                        journal[student] = ({lesson: mark})
                    with open(FILE_NAME, 'w') as file:
                        file.write(str(journal))
                else:
                    print('Файла не существует')
            # удаление
            elif choice == '3':
                if os.path.isfile(FILE_NAME):
                    with open(FILE_NAME, 'r') as file:
                        journal = file.read()
                    if journal:
                        journal = eval(journal)
                    else:
                        journal = {}
                    choice2 = input('1-Удалить ученика\n2-Удалить оценку\n')
                    if choice2 == '1':
                        student = (input('Имя ученика\n'))
                        if student in journal:
                            del journal[student]
                        if student not in journal:
                            print('Такого ученика нет в журнале')
                    elif choice2 == '2':
                        student = input('Введите имя ученика у которого нужно удалить оценку:\n')
                        lesson = input('Введите предмет по которому нужно удалить оценку:\n')
                        if student in journal:
                            if lesson in journal[student]:
                                del journal[student[lesson]]
                            elif lesson not in journal[student]:
                                print('По этому предмету у ученика нет оценок')
                        if student not in journal:
                            print('В журнале нет такого ученика')
                    else:
                        print('Введено неправильное значение')
                else:
                    print('Файла не существует')

            else:
                print('Введено неправильное значение')
            
            if choice == '4':
                print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
                num = input()
                if num == 'Y' or 'y' or 'У' or 'у':
                    option()
                exit()
        else:
            print('Всего доброго!')
        exit()
option()