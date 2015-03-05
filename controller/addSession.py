#!/usr/local/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/5/2015
last_modified_by:   Aninda Manocha
last_modified_date: 3/5/2015
"""

import constants
import utils
import json
from sql.session import Session
from sql.user import User

#Format of session
#requestType: addSession
#token: "string"
#ip: "string"
#user: User

def iChooseU(json):
    thisUser = utils.findUser(json)

    token = json["token"]
    ip = json["ip"]
    user = json["user"]
    theUser = User.get(user["id"])[0]

    newSession = Session.noID(token, ip, theUser, ACTIVE)
    newSession.add()

    return utils.successJson(json)
