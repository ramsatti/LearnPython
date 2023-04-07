import getpass

usernme = input('Username: ')
paswrd = getpass.getpass('Password: ')
print('You have been registered')

def register(username, password):
    if username == usernme and password == paswrd:
        return 'You are logged in!'
    else:
        return 'Incorrect username or password'

userIpt = input('Username: ')
pwdIpt = getpass.getpass('Password: ')

ans = register(userIpt, pwdIpt)
print(ans)