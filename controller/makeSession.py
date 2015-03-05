#!usr/local/bin/python3

from sql.session import Session
from sql.user import User

user = User.get(1)[0]

y = Session.noID("1234567890123456789012345678901234567890123456789012345678901234", "127.0.0.1", user, 1)

print(y)
y.add()
print(y)
