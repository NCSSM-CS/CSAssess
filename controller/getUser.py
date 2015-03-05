#!/usr/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Keshav Patel
last_modified date: 3/4/2015
"""

# imports
from sql.user import User
from sql.topic import Topic
from sql.session import Session

#Format of JSON -KP
#requestType: getUser
#firstName: "string"
#lastName: "string"
#section: "string"
#assessment: "string"

def iChooseU(json):
    #from Ebube pt. 2
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)

    firstName = json["firstName"]
    lastName = json["lastName"]
    section = json["section"]
    assessment = json["assessment"]

    complete = []
    count = 0

    if not firstName == None:
        complete += Topic.get(0, firstName)
        count+=1
    if not lastName == None:
        complete += Topic.get(0, lastName)
        count+=1
    if not section == None:
        complete += Topic.get(0, section)
        count+=1
    if not Assessment == None:
        complete += Topic.get(0, assessment)
        count+=1

    collect = []
    intersect = []

    for response in complete:
        if collect.count(response) < count:
            collect.append(response)
        else collect.count(response) >= count:
            intersect.add(response)

            

    out = {}
    
    for num in range(len(intersect)):
        out[num] = intersect[num]

    return json.dumps(out)
