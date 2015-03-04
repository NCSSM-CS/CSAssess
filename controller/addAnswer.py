#!/usr/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/4/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/4/2015
"""

# imports
import constants
import json
from sql.user import User
from sql.question import Question
from sql.answer import Answer
from sql.topic import Topic
from sql.session import Session

#Format of answer -AM
#requestType: answer
#question: question.id (Integer)
#content: "string"
#isSolution: boolean

def iChooseU(json):
    #from Ebube
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)

    question = json["question"]
    content = json["content"]
    isSolution = True 

    newAnswer = Answer.noID(TIME_STAMP, thisUser.id, question, None, content, isSolution, ACTIVE)
    newAnswer.add()

    successJson = json.dumps({"success":True, "session":session.toJson()})
    return successJson 
