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
# content: "string"
# language: "string"
# difficulty: integer
# qType: "string"
# topics: []

def iChooseU(form):
    thisUser = utils.findUser(form)

    content = form.getlist("content")[0]
    language = form.getlist("language")[0]
    difficulty = form.getlist("difficulty")[0]
    qType = form["qType"]
    topics = []
    for topic in form.getlist("topics"):
        topics.append(Topic.get(0, topic)[0])

    newQuestion = Question.noID(None, thisUser, language, qType, difficulty, constants.NULL_OBJ, 1, constants.NULL_OBJ, content, topics, constants.ACTIVE)
    newQuestion.add()
    
    return utils.successJson(form)
