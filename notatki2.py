users: list[dict] = [
    {"name": "Mateusz", "surname": "Matulis", "posts": 9},
    {"name": "Janek", "surname": "Mielec", "posts": 20},
    {"name": "Maciej", "surname": "Przybytek", "posts": 45},
    {"name": "Bartosz", "surname": "Pietrasik", "posts": 60},
    {"name": "Tymoteusz", "surname": "Miszczak", "posts": 21},
    {"name": "Mateusz", "surname": "Matysiak", "posts": 33},
    {"name": "Paweł", "surname": "Paszkowski", "posts": 1},
]
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