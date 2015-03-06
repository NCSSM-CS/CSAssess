#!/usr/local/bin/python3

"""
created_by:         Aninda Manocha
created_date:       3/5/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/5/2015
"""

# imports
import constants
import utils
import json
from sql.session import Session
from sql.user import User
from sql.comment import Comment

#Format of comment -AM
#requestType: addComment
#answer: Answer
#content: "string"

def iChooseU(json):
    thisUser = utils.findUser(json)

    answer = json["answer"]
    theAnswer = Answer.get(answer["id"])[0]
    content = json["content"]

    newComment = Comment.noID(None, thisUser, theAnswer, content, ACTIVE)
    newComment.add()

    return utils.successJson(json)
