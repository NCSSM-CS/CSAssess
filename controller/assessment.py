#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   John Fang
last_modified date: 3/2/2015
"""

# imports
import constants

# classes
class Assessment:
    'Assessment object to hold attributes and functions for an assessment'

    def __init__(self, id, created, created_by, type, section, name, question_list, topic_list):
        """
        self          - the assessment in question
        id            - the id number of the assessment 'self' in the database
        created       - the date when the assessment 'self' was created
        created_by    - the user that created the assessment 'self'
        type          - the type of assessment 'self' is
        section       - the section that the assessment 'self' falls under
        name          - the name of the assessment 'self'
        question_list - a list of questions that make up the assessment 'self'
        topic_list    - a list of topics that apply to the assessment 'self'

        this function acts as the constructor to define a new assessment object
        """
        self.id            = id
        self.created       = created
        self.created_by    = created_by
        self.type          = type
        self.section       = section
        self.name          = name
        self.question_list = question_list
        self.topic_list    = topic_list

    @classmethod
    def noID(self, created, created_by, type, section, name, question_list, topic_list):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new assessment with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created an
        assessment that has not yet been assigned an id from the database
        """
        return self(None, created, created_by, type, section, name, question_list, topic_list)

    def __eq__(self, other):
        """
        self  - the assessment in question
        other - another assessment that you are comparing 'self' to

        returns a boolean telling if the attributes of 'self' and 'other'
        are the same

        this function overrides the way python compares two assignments
        and decides if they are equal instead of checking if they are the
        exact same object
        """
        return (
        self.id            == other.id            and
        self.created       == other.created       and
        self.created_by    == other.created_by    and
        self.type          == other.type          and
        self.section_id    == other.section_id    and
        self.name          == other.name          and
        self.question_list == other.question_list and
        self.topic_list    == other.topic_list)

    # sort question list by difficulty
    def sortByDifficulty(self, reverseOpt = False):
        """
        self       - the assessment in question
        reverseOpt - a boolean deciding a descending ascending order

        returns a sorted assessment object based on the difficulty
        of the questions

        this function allows for easy sorting of assessment questions
        by difficulty
        """
        self.question_list.sort(key=lambda i: i.difficulty, reverse = reverseOpt)
        return self

    # sort question list by topic
    def sortByTopic(self, reverseOpt = False):
        """
        self       - the assessment in question
        reverseOpt - a boolean deciding a descending ascending order

        returns a sorted assessment object based on the topics of each question

        this function allows for easy sorting of assessment questions by topic
        """
        self.question_list.sort(key=lambda i: i.topic_list, reverse = reverseOpt)
        return self

    # sort question list by type
    def sortByType(self, reverseOpt = False):
        """
        self       - the assessment in question
        reverseOpt - a boolean deciding a descending ascending order

        returns a sorted assessment object based on the type of each question

        this function allows for easy sorting of assessment questions by type
        """
        self.question_list.sort(key=lambda i: i.type, reverse = reverseOpt)
        return self

    def setID(self, id):
        """
        self - the assessment in question
        id   - the id for the assessment from the database

        this function allows you to assign an id to the assessment after
        inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the assessment in question

        returns a string that fully describes the assessment 'self'

        this function allows you to convert the assessment object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "         + str(self.id)         + "\n"
        string += "created: "    + str(self.created)    + "\n"
        string += "created by: " + str(self.created_by) + "\n"
        string += "type: "       +     self.type        + "\n"
        string += "section id: " + str(self.section)    + "\n"
        string += "name: "       +     self.name

        string += "\nTopics:\n"
        for i in self.topic_list:
            string += "\t"             +     i.name        + "\n"

        string += "\nQuestions:\n"
        for i in self.question_list:
            string += "\tdifficulty: " + str(i.difficulty) + "\n"
            string += "\tcontent: "    +     i.content     + "\n\n"

        return string
    def toJson(self):
        data = [{
        "id"        :     self.id,
        "created"   : str(self.created),
        "created by":     self.created_by,
        "type"      :     self.type,
        "section id":     self.section,
        "name"      :     self.name
        }]
        return json.dumps(data)
