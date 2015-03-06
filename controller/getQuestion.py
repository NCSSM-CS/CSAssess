#!/usr/local/bin/python3

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
from sql.topic import Topic

# Format of JSON - EC
# requestType: getQuestion
# session: "string"
# topics: "string"
# difficulty: integer

def iChooseU(form):
    thisUser = utils.findUser(form)
    
    qByTopic = Question.get(0, Topic.get(0, form.getlist("topics")[0]))
    qByDiff = Question.get(0, form.getlist("difficulty")[0])
    intersect = [];
    for q in qByTopic:
        if q in qByDiff:
            intersect.append(q.toJson())
    out = {}
    out["questionList"] = intersect
    out["sessionID"] = form.getlist("session")[0]
    
    return json.dumps(out)
