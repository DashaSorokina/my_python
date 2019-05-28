def writer(filename, numbers):
    import json
    try:
        with open(filename, 'w') as file:
            json.dump(numbers, file)
    except Exception as x:
        print(x)

def read(filename):
    import json
    try:
        with open(filename) as file:
            numbers = json.load(file)
        return numbers
    except Exception as x:
        return x

def do():
    print('\ntodo: \n1. Добавить задачу. \n2. Вывести список задач. \n3. Выход.')

command = 0
todo = list()

while command != 3:
    do()
    command = int(input('\nУкажите число: '))
    if command == 1:
        new = {}
        new['Task'] = input('СФормулируйте задачу: ')
        new['Category'] = input('Добавьте категорию к задаче: ')
        new['Date'] = input('Добавьте время к задаче: ')
        todo.append(new)
        writer('list_of_tasks.json', todo)
    if command == 2:
        print()
        for task in todo:
            print()
            for option in task:
                print(option, ':', task[option])
