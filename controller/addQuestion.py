#!/usr/bin/python3

"""
created_by:         Ebube Chuba
created_date:       3/3/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/4/2015
"""

# imports
import constants
import utils
import json
from sql.user import User
from sql.question import Question
from sql.topic import Topic
from sql.session import Session

# Format of questions - EC
# requestType: question
# language: "language"
# type: "test"
# difficulty: Integer(1-10)
# content: "string"
# topic: list of topics

def iChooseU(json):
    findUser()

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

    newQuestion = Question.noID(None, thisUser.id, language, qType, difficulty, 1, 1, None, content, topics)
    newQuestion.add()
    
    successJson()
