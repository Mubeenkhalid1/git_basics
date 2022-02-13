vehicles = ['car', 'bike', 'scooty','truck',23]
print(vehicles)

print(vehicles[2].title())




names = ["Mubeen", 'Usama', 'Areeesh','ghufran','linus']
for name in names:
    print(f'hello {name}!')



usre_0 = {
    'username': 'abc',
    'password': '123',

}

for key,value in usre_0.items():
    print(f'{key}: {value}')



for user in sorted(usre_0.keys()):
    print(user)



def greet_user(username):
    """Display a simple greeting with username.
    params:
        username(string): a username to be printed.
    """

    print(f"Hello, {username.title()}!")
greet_user(username='Mubeen Khalid')