
def read(users: list[dict])->None:
    for user in users[1:]:
        print(f'Twój znajomy {user["name"]} opublikował: {user["posts"]}')

def create_user(users: list[dict])->None:
    name: str = input("Podaj imię użytkownika: ")
    surname: str = input("Podaj nazwisko użytkownika: ")
    posts: int = int(input("Podaj liczbę postów: "))
    user: dict = {"name": name, "surname": surname, "posts": posts}
    users.append(user)
def search(users: list[dict])->None:
    user_name: str = input("Kogo szukasz: ")
    for user in users[1:]:
        if user["name"] == user_name:
            print(f'Twój znajomy {user["name"]} opublikował: {user["posts"]}')

def remove(users: list[dict])->None:
    user_name: str = input("Kogo chcesz usunąć: ")
    for user in users[1:]:
        if user["name"] == user_name:
            users.remove(user)

def update (users: list[dict]) -> None:
    user_name: str = input("Kogo szukasz: ")
    for user in users[1:]:
        if user["name"] == user_name:
            new_user_name = input("Wprowadź nowe imię: ")
            new_user_surname = input("Wprowadź nowe nazwisko: ")
            new_user_posts = input("Wprowadź nową ilość postów: ")
            user["surname"] = new_user_surname
            user["name"] = new_user_name
            user["posts"] = new_user_posts
    print(users)