#!/usr/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/6/2015
"""

# imports
import json
import utils
from sql.user import User
from sql.session import Session

#Format of JSON -KP
#requestType: getUser
#firstName: "string"
#lastName: "string"
#section: "string"
#assessment: "string"

def iChooseU(form):
    thisUser = utils.findUser(form)

    firstName = form["firstName"]
    lastName = form["lastName"]
    section = form["section"]
    assessment = form["assessment"]

    complete = []
    count = 0

    if not firstName == "":
        complete += User.get(0, firstName)
        count += 1
    if not lastName == "":
        complete += User.get(0, lastName)
        count += 1
    if not section == "":
        complete += User.get(0, section)
        count += 1
    if not assessment == "":
        complete += User.get(0, assessment)
        count += 1

    collect = []
    intersect = []

    for response in complete:
        if collect.count(response) < count:
            collect.append(response)
        else:
            intersect.add(response)

    out = {}
    
    for num in range(len(intersect)):
        out[num] = intersect[num]

    return json.dumps(out)
