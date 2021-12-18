import secrets, os
password = secrets.token_urlsafe(32)

file = open('password.txt', 'w')
file.write(password)