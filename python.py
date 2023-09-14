from logins import register, login


while True:
    choice = input('Выберите действие: зарегистрироваться - 1, логин - 2, выйти -3: ')
    if choice =='1' :
        email = input('Введите ваш адрес электронной почты (Gmail): ')
        password = input('Введите пароль: ')
        register(email, password)
        print('Регистрация успешно завершена.')
    elif choice == '2':
        email = input('Введите ваш адрес электронной почты (Gmail): ')
        password = input('Введите пароль: ')
        result = login(email, password)

        if result:
            print('Вход выполнен успешно')
        else:
            print('Неверный email или пароль')
    else:
        break