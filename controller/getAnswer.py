#!/usr/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/4/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/4/2015
"""

# imports
from sql.user import User
from sql.question import Question
from sql.answer import Answer

#Format of JSON -AM
#requestType: getAnswer
#question: question.id (Integer)
#created_by: user.id (Integer)

def iChooseU(json):
    #from Ebube pt. 2
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)

    question = json["question"]
    created_by = json["user"]

    aByQuestion = []
    aByUser = []

    if not question == None:
        aByQuestion.append(Answer.get(0, question))

    if not created_by == None:
        aByUser.append(Answer.get(0, created_by))

    intersect = []

    for a in aByQuestion:
        if a in aByUser:
            intersect.append(a.toJson())
    
    out = {}
    
    for num in range(len(intersect)):
        out[num] = intersect[num]

    return json.dumps(out)
