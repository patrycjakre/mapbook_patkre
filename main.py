users: list = [
    {'name': 'Patrycja', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Poznań'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Toruń'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Łódź'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Kielce'},
    {'name': 'Amelia', 'posts': 11, 'city': 'Elbląg'},
    {'name': 'Karolina', 'posts': 13, 'city': 'Kraków'},
    {'name': 'Julka', 'posts': 15, 'city': 'Wrocław'},
    {'name': 'Aleksandra', 'posts': 17, 'city': 'Zamość'},
    {'name': 'Patrycja', 'posts': 19, 'city': 'Szczecin'},


]

print(f'Witaj {users[0]['name']}!!')
for user in users[1:]:
    print(f'twój znajomy {user['name']}, {user['city']} opublikował {user['posts']} postów')

# for idx, _ in enumerate(users[1:]):
#     print(f'Twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
