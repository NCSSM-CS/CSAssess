#!/usr/local/bin/python3

# Created by:   Aninda Manocha
# Created date: 3/5/2014
# Last modified by:   Ebube Chuba
# Last modified date: 3/6/2014

import os
import json
from sql.user import User
from sql.session import Session

def findUser(form):
    return User.get(1)[0]
    ipAddress = "1234567.23"
    session = Session.get(json["session"],ipAddress )[0]
    thisUser = session.user
    if DEBUG > 1:
        print(thisUser)
    return thisUser

def successJson(form):
    return json.dumps({"success":True, "session":"127.0.0.1/test"})
    session = Session.get("1234567890123456789012345678901234567890123456789012345678901234", "127.0.0.1")[0]
    successJson = json.dumps({"success":True, "session":session.toJson()})
    return successJson
