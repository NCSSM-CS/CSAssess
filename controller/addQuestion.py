#!/usr/bin/python3

"""
created_by:         Ebube Chuba
created_date:       3/3/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/4/2015
"""

# imports
import cgi
import cgitb
import time
import constants
from sql.user import User
from sql.question import Question
from sql.topic import Topic

cgitb.enable()

# TODO: Session things (and IP address) - EC
#       Wait for Micah to finish objects (specifically questions) - EC

# Format of questions - EC
# requestType: question
# language: "language"
# type: "test"
# difficulty: Integer(1-10)
# content: "string"
# topic: list of topics

## This will work later - EC
thisUser = User.get(1)[0]
print(thisUser)
form = cgi.FieldStorage()

language = ""
topics = []
difficulty = 0
content = ""
qType = ""

#print(Topic.get())

for field in list(form.keys()):
    if field == "language":
        language = form[field]
    if field == "type":
        qType = form[field]
    if field == "difficulty":
        difficulty = form[field]
    if field == "content":
        content = form[field]
    if field == "topics":
        for topic in form[field]:
            if not topic in ["swag", "Swag", "SWAG"]: #Topic.get():
                newTopic = Topic.noID(TIME_STAMP, thisUser, topic, ACTIVE)
                newTopic.add()
        topics = form[field]

#newQuestion = Question.noID(TIME_STAMP, thisUser, language, qType, difficulty, 1, 1, None, content, topics)
#newQuestion.add()
