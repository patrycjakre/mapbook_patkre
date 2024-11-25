


def hello(user:str)->None:
    print(f'Witaj {user}!!')

def read_users(users:list)->None :
    for user in users:
        print(f'twój znajomy {user['name']}, {user['city']} opublikował {user['posts']} postów')