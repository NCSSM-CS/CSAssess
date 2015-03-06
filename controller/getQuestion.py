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

def iChooseU(form):
    thisUser = utils.findUser(form)
    
    qByType = []
    for i in range(len(json["topics"])):
        theseQuestions = Question.get(0, json["topics"][i])
        for j in range(len(theseQuestions)):
            thisQuestion = theseQuestions[j]
            if not thisQuestion in qByType:
                qByType.append(thisQuestion)
    qByDiff = Question.get(0, form["difficulty"])
    intersect = [];
    for q in qByType:
        if q in qByDiff:
            intersect.append(q.toJson())
    out = {}
    out["questionList"] = intersect
    out["sessionID"] = form["session"]
    
    return json.dumps(out)
