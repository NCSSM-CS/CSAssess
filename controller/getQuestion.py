#!/usr/bin/python3

"""
created_by:         Ebube Chuba
created_date:       3/4/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/4/2015
"""

# imports
import json
from sql.user import User
from sql.question import Question
from sql.session import Session

# Format of JSON - EC
# requestType: getQuestion
# session: sessionID
# topic: someTopic
# difficulty: Integer

def iChooseU(json):
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)
    
    qByType = []
    for i in range(len(json["topics"])):
        theseQuestions = Question.get(0, json["topics"][i])
        for j in range(len(theseQuestions)):
            thisQuestion = theseQuestions[j]
            if not thisQuestion in qByType:
                qByType.append(thisQuestion)
    qByDiff = Question.get(0, json["difficulty"])
    intersect = [];
    for q in qByType:
        if q in qByDiff:
            intersect.append(q.toJson())
    out = {}
    for num in range(len(intersect)):
        out[num] = intersect[num]
    return json.dumps(out)
