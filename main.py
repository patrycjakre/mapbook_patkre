from map_functions import single_user_map, multi_user_map
from mapbook.users import users
from mapbook.crud import hello, read_users, add_user, remove_user, update_user


def main():
    hello(users[0]['name'])
    while True:
        print('======MENU======')
        print('0. wyjście z programu')
        print('1. dodaj znajomego')
        print('2. wczytaj znajomego')
        print('3. aktualizuj znajomego')
        print('4. usuń znajomego')
        print('5. generuj mapę z lokalizacją znajomego')
        print('6. generuj mapę z lokalizacją wszystkich znajomych')

        menu_option: str = input('użytkowniku wybierz opcję menu: ')
        print(f'uzytkownik wybrał {menu_option}')
        if menu_option == '0':
            break
        if menu_option == '1':
            add_user(users)
        if menu_option == '2':
            read_users(users)
        if menu_option == '3':
            update_user(users)
        if menu_option == '4':
            remove_user(users)
        if menu_option == '5':
            single_user_map(users)
        if menu_option == '6':
            multi_user_map(users)


if __name__ == '__main__':
    main()


#sdfgyui