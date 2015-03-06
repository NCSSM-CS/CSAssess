#!/usr/local/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/5/2015
last_modified_by:   Keshav Patel
last_modified_date: 3/6/2015
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
#user: username "string"

def iChooseU(form):
    thisUser = utils.findUser(form)

    token = form["token"]
    ip = form["ip"]
    user = form["user"]
    theUser = User.get(0, None, form["user"])[0]

    newSession = Session.noID(token, ip, theUser, ACTIVE)
    newSession.add()

    return utils.successJson(form)
