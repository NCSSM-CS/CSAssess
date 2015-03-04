#!/usr/bin/python3

"""
created_by:         Ebube Chuba
created_date:       3/3/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/4/2015
"""

# imports
import constants
import json
from sql.user import User
from sql.question import Question
from sql.topic import Topic

# TODO: Session things (and IP address) - EC
#       Wait for Micah to finish objects (specifically questions) - EC

# Format of questions - EC
# requestType: question
# language: "language"
# type: "test"
# difficulty: Integer(1-10)
# content: "string"
# topic: list of topics

def iChooseU(json):
    ## This will work later - EC
    
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)

    language = ""
    topics = []
    difficulty = 0
    content = ""
    qType = ""

    for field in list(json.keys()):
        if field == "language":
            language = json[field]
        if field == "type":
            qType = json[field]
        if field == "difficulty":
            difficulty = json[field]
        if field == "content":
            content = json[field]
        if field == "topics":
            for topic in json[field]:
                if not topic in Topic.get():
                    newTopic = Topic.noID(TIME_STAMP, thisUser, topic, ACTIVE)
                    newTopic.add()
            topics = json[field]

    newQuestion = Question.noID(TIME_STAMP, thisUser, language, qType, difficulty, 1, 1, None, content, topics)
    newQuestion.add()

    successJson = {"success":True, "session": session.toJson()}

    return json.dumps(successJson)
