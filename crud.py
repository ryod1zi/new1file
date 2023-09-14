def read_lists(filename):
    try:
        with open(filename, 'r') as file:
            lists = file.read().splitlines()
        return lists
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создаем новый файл.")
        with open(filename, 'w') as file:
            return []
def write_lists(filename, lists):
    with open(filename, 'w') as file:
        file.write('\n'.join(lists))
def create_list(list_name):
    lists = read_lists('lists.txt')
    lists.append(list_name)
    write_lists('lists.txt', lists)
    print(f"Создан новый список: {list_name}")
def delete_list(list_name):
    lists = read_lists('lists.txt')
    if list_name in lists:
        lists.remove(list_name)
        write_lists('lists.txt', lists)
        print(f"Список {list_name} удален.")
    else:
        print(f"Список {list_name} не найден.")
def list_lists():
    lists = read_lists('lists.txt')
    print("Списки:")
    for index, list_name in enumerate(lists):
        print(f"{index + 1}. {list_name}")
while True:
    print("\nВыберите действие:")
    print("1. Создать новый список")
    print("2. Удалить список")
    print("3. Показать все списки")
    print("4. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        list_name = input("Введите название нового списка: ")
        create_list(list_name)
    elif choice == '2':
        list_name = input("Введите название списка для удаления: ")
        delete_list(list_name)
    elif choice == '3':
        list_lists()
    elif choice == '4':
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")
