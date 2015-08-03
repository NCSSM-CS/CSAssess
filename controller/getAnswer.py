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
#question: integer
#created_by: "string"

def iChooseU(form):
    thisUser = utils.findUser(form)

    question = Question.get(form.getlist("question")[0])[0]
    createdBy = User.get(form.getlist("createdBy")[0])[0]

    aByQuestion = []
    aByUser = []

    if not question == None:
        aByQuestion.append(Answer.get(question))

    if not created_by == None:
        aByUser.append(Answer.get(createdBy))

    intersect = []

    for a in aByQuestion:
        if a in aByUser:
            intersect.append(a.toJson())
    
    out = {}
    out["answerList"] = intersect
    out["sessionID"] = form.getlist("session")[0]

    return json.dumps(out)
