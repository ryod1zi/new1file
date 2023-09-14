
def register(email, password):
    with open('users.txt', 'a') as file:
        file.write(f'{email}:{password}\n')
def login(email, password):
    with open('users.txt', 'r') as file:
        for line in file:
            stored_email, stored_password = line.strip().split(':')
            if stored_email == email and stored_password == password:
                return True
    return False


