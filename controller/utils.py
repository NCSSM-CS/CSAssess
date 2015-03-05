#!/usr/bin/python3

from sql.user import User
from sql.session import Session

def findUser():
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)
    return thisUser

def successJson():
    successJson = json.dumps({"success":True, "session":session.toJson()})
    return successJson
