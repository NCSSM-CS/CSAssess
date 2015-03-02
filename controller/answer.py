#!/usr/bin/python

"""
created_by:         Ebube Chuba
created_date:       3/2/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/2/2015
"""

# imports
import constants
import json

# classes
class Answer:
    'Question object to hold attributes and functions for a question'

    def __init__(self, id, created, created_by, question, score, answer_text):
        """
        self             - the answer in answer
        id               - the id number of the answer 'self' in the database
        created          - the date when the answer 'self' was created
        created_by       - the user that created the answer 'self'
        question_id      - the id number of the question the answer 'self' belongs to
        score            - the score of the answer
        answer_text      - the content of hte answer

        this function acts as the constructor to define a new answer object
        """
        self.id               = id
        self.created          = created
        self.created_by       = created_by
        self.question_id      = question
        self.score            = score
        self.answer_text      = answer_text

    @classmethod
    def noID(self, id, created, created_by, question, score, answer_text):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new question with the id parameter set as None and the other
        parameters set as they are passed in

        this function acts as a second constructor where you have created a
        answer that has not yet been assigned an id from the database
        """
        return self(None, id, created, created_by, question, score, answer_text)

    def __eq__(self, other):
        """
        self  - the answer in answer
        other - another answer that you are comparing 'self' to

        return a boolean telling if the attributes of self and 'other'
        are the same

        this function overrides the way python compares two answers
        and decides if they are equal instead of checking if they are the
        exact same object
        """
        return (
        self.id               == other.id               and
        self.created          == other.created          and
        self.created_by       == other.created_by       and
        self.question         == other.question         and
        self.score            == other.score            and
        self.answer_text      == other.answer_text
        )

    def setID(self, id):
        """
        self - the answer in answer
        id   - the id for the answer from the database

        this function allows you to assign an id to the answer
        after inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the answer in answer

        returns a string that fully describes the answer 'self'

        this function allows you to convert the answer object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "                   + str(self.id)               + "\n"
        string += "created: "              + str(self.created)          + "\n"
        string += "created by: "           + str(self.created_by)       + "\n"
        string += "question: "             + str(question)              + "\n"
        string += "score: "                + str(score)                 + "\n"
        string += "answer text: "          + str(answer_text)           + "\n"

        return string
    def toJson(self):
        data = [{
<<<<<<< HEAD
        "id" 	    	:     self.id, 
        "created"   	: str(self.created),
=======
<<<<<<< HEAD
        "id" 		: self.id, 
=======
<<<<<<< HEAD
        "id" 		:     self.id, 
        "created"	: str(self.created),
>>>>>>> 0f781f3513d91fa623b39ab12f9f9c0f3e9b67fa
        "created by"	:     self.created_by,
        "question id"	:     self.question_id,
        "score"	    	:     score,
        "answer text"	:     answer_text
<<<<<<< HEAD
=======
=======
        "id" 		: self.id,
>>>>>>> 9c64bfc51a18f52c0ce4492c23b8b88c91a446c8
        "created"	: self.created,
        "created by"	: self.created_by,
        "question id"	: self.question_id,
        "score"		: score,
        "answer text"	: answer_text
<<<<<<< HEAD
=======
>>>>>>> 2f1c846e9b3a19bbc9e6f3c28bcbc10e2f0816eb
>>>>>>> 9c64bfc51a18f52c0ce4492c23b8b88c91a446c8
>>>>>>> 0f781f3513d91fa623b39ab12f9f9c0f3e9b67fa
        }]
        return json.dumps(data)
