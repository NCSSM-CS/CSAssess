#!/usr/bin/python

"""
created_by:         Keshav Patel
created_date:       3/2/2015
last_modified_by:   Keshav Patel
last_modified date: 3/2/2015
"""

# imports
import constants

# classes
class Test_Case:
    'test_case object to hold attributes and functions for a test_case'

    def __init__(self, id, created, created_by, question_id, weight, content):
        """
        self          - the test_case in question
        id            - the id number of the test_case 'self' in the database
        created       - the date when the test_case 'self' was created
        created_by    - the user that created the test_case 'self'
        question_id   - the question associated with 'self'
        weight        - the weight given to this test_case
        content       - the code for this test_case

        this function acts as the constructor to define a new test_case object
        """
        self.id            = id
        self.created       = created
        self.created_by    = created_by
        self.question_id   = question_id
        self.weight        = weight
        self.content       = content

    @classmethod
    def noID(self, id, created, created_by, question_id, weight, content):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new test_case with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        test_case that has not yet been assigned an id from the database
        """
        return self(self, id, created, created_by, question_id, weight, content):

    def __eq__(self, other):
        """
        self  - the test_case in question
        other - another test_case that you are comparing 'self' to

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
        self.question_id   == other.question_id   and
        self.weight        == other.weight        and
        self.content       == other.content)

    def setID(self, id):
        """
        self - the test_case in question
        id   - the id for the test_case from the database

        this function allows you to assign an id to the test_case after
        inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the test_case in question

        returns a string that fully describes the test_case 'self'

        this function allows you to convert the test_case object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "         + str(self.id)         + "\n"
        string += "created: "    + str(self.created)    + "\n"
        string += "created by: " + str(self.created_by) + "\n"
        string += "question_id " + str(self.question_id)+ "\n"
        string += "weight "      + str(self.weight)     + "\n"
        string += "content "     + self.content         + "\n"
        return string
