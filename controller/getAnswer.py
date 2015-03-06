#!/usr/local/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/4/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/6/2015
"""

# imports
from sql.user import User
from sql.question import Question
from sql.answer import Answer
from sql.session import Session

#Format of JSON -AM
#requestType: getAnswer
#question: Question
#created_by: User

def iChooseU(json):
    thisUser = utils.findUser(json)

    question = json["question"]
    createdBy = json["user"]

    aByQuestion = []
    aByUser = []

    if not question == None:
        aByQuestion.append(Answer.get(question["id"]))

    if not created_by == None:
        aByUser.append(Answer.get(createdBy["id"]))

    intersect = []

    for a in aByQuestion:
        if a in aByUser:
            intersect.append(a.toJson())
    
    out = {}
    out["answerList"] = intersect
    out["sessionID"] = json["session"]

    return json.dumps(out)
