#!/usr/bin/python3

"""
created_by:         Ebube Chuba
created_date:       3/4/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/6/2015
"""

# imports
import json
import utils
from sql.user import User
from sql.question import Question

# Format of JSON - EC
# requestType: getQuestion
# session: sessionID
# topic: someTopic
# difficulty: Integer

def iChooseU(form):
    thisUser = utils.findUser(form)
    
    qByType = []
    for i in range(len(form.getlist("topics"))):
        theseQuestions = Question.get(0, form.getlist("topics")[i])
        for j in range(len(theseQuestions)):
            thisQuestion = theseQuestions[j]
            if not thisQuestion in qByType:
                qByType.append(thisQuestion)
    qByDiff = Question.get(0, form.getlist("difficulty")[0])
    intersect = [];
    for q in qByType:
        if q in qByDiff:
            intersect.append(q.toJson())
    out = {}
    out["questionList"] = intersect
    out["sessionID"] = form.getlist("session")[0]
    
    return json.dumps(out)
