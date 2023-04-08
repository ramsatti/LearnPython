import getpass

print('Register Your Details')
usernme = input('Username: ')
paswrd = getpass.getpass('Password: ')
print('You have been registered')

def verify(username, password):
    if username == usernme and password == paswrd:
        return 'You are logged in!'
    else:
        return 'Incorrect username or password'

print('Login w/ Your Details')
userIpt = input('Username: ')
pwdIpt = getpass.getpass('Password: ')

ans = verify(userIpt, pwdIpt)
print(ans)