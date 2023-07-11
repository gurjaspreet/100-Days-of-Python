password = 'cskdnjcasa#!'

if len(password) >= 11 and password.find('!') != -1:
    print('Password correct')
else:
    print('Password too short')