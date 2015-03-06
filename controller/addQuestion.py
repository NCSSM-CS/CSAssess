#!/usr/local/bin/python3

"""
created_by:         Ebube Chuba
created_date:       3/3/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/6/2015
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
# requestType: addQuestion
# questionContent: "string"
# language: "string"
# difficulty: integer
# qType: "string"
# topics: []

def iChooseU(form):
    thisUser = utils.findUser(form)

    content = form["questionContent"]
    language = form["language"]
    difficulty = form["difficulty"]
    qType = form["qType"]
    topics = []
    for topic in form["topics"]:
        theTopics.append(Topic.get(0, topic)[0])

    newQuestion = Question.noID(None, thisUser, language, qType, difficulty, 1, 1, None, content, topics, ACTIVE)
    newQuestion.add()
    
    return utils.successJson(form)
