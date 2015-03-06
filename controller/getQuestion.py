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
    
    topic = form.getlist("firstName")[0]
    difficulty = form.getlist("lastName")[0]

    complete = []
    count = 0

    if not topic == "":
        complete += Question.get(0, Topic.get(topic)[0])
        count += 1
    if not difficulty == 0:
        complete += Question.get(0, difficulty)
        count += 1

    collect = []
    intersect = []

    for response in complete:
        if collect.count(response) < count:
            collect.append(response)
        else:
            intersect.add(response)

    out = {}
    out["questionList"] = intersect
    out["sessionID"] = form.getlist("session")[0]
    
    return json.dumps(out)
