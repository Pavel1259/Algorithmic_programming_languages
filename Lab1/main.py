# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Person:
    name = ""
    age = 0

class Student(Person):
    number_ticket = 0
    name_specialty = ""

class Teacher(Person):
    experience_age = 0



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # список (то же что и массив)
    name_person = ['Иванов Иван Иванович','Петров Михаил Игоревич', 'Козлов Виктор Евгеньевич','Носов Кирилл Игоревич']

    # словарь (связка ключ - значение)

    # кортеж (не изменяемый)
    names_specialty = ('ASU', 'EHVT', 'ASU', 'RIS')
    # names_specialty.append('ATPP') - не добавится
    print("Все направления на кафедре")
    print(set(names_specialty))  # вывести уникальные значения в множестве

    # множество
    all_names_specialty = set(names_specialty)
    all_names_specialty.add('ATPP')
    all_names_specialty.add('ATPP') # оно не добавится, так как
    # множество это неупорядоченная коллекция уникальных элементов
    print("Все направления на факультете")
    for x in all_names_specialty:
        print(x)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
