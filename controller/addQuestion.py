#!/usr/bin/python2.6

"""
created_by:         Ebube Chuba
created_date:       3/3/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/3/2015
"""

# imports
import cgi
import cgitb
import time
from user import User
#from sql.question import Question

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
#thisUser = User.get(1)[0]

form = cgi.FieldStorage()

language = ""
topics = []
difficulty = 0
content = ""
qType = ""

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
        topics = form[field]

#newQuestion = Question.noID(time.strftime("%Y-%m-%d %H:%M:%S"), None, language, qType, difficulty, 1, 1, None, content, topics)
#newQuestion.add()
