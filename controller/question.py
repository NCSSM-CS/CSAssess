#!/usr/bin/python3

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/2/2015
"""

# imports
import constants

# classes
class Question:
    'Question object to hold attributes and functions for a question'

    def __init__(self, id, created, created_by, language, type, difficulty, prev_question_id, version_number, last_given, content, topic_list):
        """
        self             - the question in question
        id               - the id number of the question 'self' in the database
        created          - the date when the question 'self' was created
        created_by       - the user that created the question 'self'
        language         - the programming language that the question 'self' was written for
        type             - the type of question 'self' is
        difficulty       - the difficulty of the question 'self'
        prev_question_id - the id number of a previous version of the question 'self'
        version_number   - the current version number of the question 'self'
        last_given       - the date that the question 'self' was last given
        content          - the content of the question 'self'
        topic_list       - a list of topics that apply to the question 'self'

        this function acts as the constructor to define a new question object
        """
        self.id               = id
        self.created          = created
        self.created_by       = created_by
        self.language         = language
        self.type             = type
        self.difficulty       = difficulty
        self.prev_question_id = prev_question_id
        self.version_number   = version_number
        self.last_given       = last_given
        self.content          = content
        self.topic_list       = topic_list

    @classmethod
    def noID(cls, created, created_by, language, type, difficulty, prev_question_id, version_number, last_given, content, topic_list):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new question with the id parameter set as None and the other
        parameters set as they are passed in

        this function acts as a second constructor where you have created a
        question that has not yet been assigned an id from the database
        """
        return cls(None, created, created_by, language, type, difficulty, prev_question_id, version_number, last_given, content, topic_list)

    def __eq__(self, other):
        """
        self  - the question in question
        other - another question that you are comparing 'self' to

        return a boolean telling if the attributes of self and 'other'
        are the same

        this function overrides the way python compares two questions
        and decides if they are equal instead of checking if they are the
        exact same object
        """
        return (
        self.id               == other.id               and
        self.created          == other.created          and
        self.created_by       == other.created_by       and
        self.language         == other.language         and
        self.type             == other.type             and
        self.difficulty       == other.difficulty       and
        self.prev_question_id == other.prev_question_id and
        self.version_number   == other.version_number   and
        self.last_given       == other.last_given       and
        self.content          == other.content          and
        self.topic_list       == other.topic_list)

    def setID(self, id):
        """
        self - the question in question
        id   - the id for the question from the database

        this function allows you to assign an id to the question
        after inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the question in question

        returns a string that fully describes the question 'self'

        this function allows you to convert the question object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "                   + str(self.id)               + "\n"
        string += "created: "              + str(self.created)          + "\n"
        string += "created by: "           + str(self.created_by)       + "\n"
        string += "language: "             +     self.language          + "\n"
        string += "type: "                 +     self.type              + "\n"
        string += "difficulty: "           + str(self.difficulty)       + "\n"
        string += "previous question id: " + str(self.prev_question_id) + "\n"
        string += "version number: "       + str(self.version_number)   + "\n"
        string += "last given: "           + str(self.last_given)       + "\n"
        string += "content: "              +     self.content           + "\n"

        string += "\nTopics:\n"
        for i in self.topic_list:
            string += "\t" + i.name + "\n"

        return string
    def toJson(self):
        data = [{
        "id"            : self.id,
        "created"       : self.created,
        "created by"        : self.created_by,
        "language"      : self.language, 
        "type"          : self.type,
        "difficulty"        : self.difficulty,
        "previous question id"  : self.prev_question_id,
        "version number"    : self.version_number,
        "last given"        : self.last_given,
        "content"       : self.content,
        "topics"        : self.topic_list
    }]
        return json.dumps(data)
