#!/usr/bin/env pyhton2.6

"""
created_by: Samuel Murray
create_date: 3/2/2015
last_modified_by: Ebube Chuba
last_modified_date: 3/3/2015
"""

#imports
import constants
import json

class Job:
    'Job object to hold attributes and functions for a job.'
    def __init__(self, id, created, created_by, section_id, type, assessment_id, assigned_to_id, content, taken_by_user_id):
        """
        self               - the job in question
        id                 - the id number of the job 'self' in the database
        created            - the date when the job 'self' was created
        created_by         - the user that created the job 'self'
        type               - the type of job 'self' is
        assignment_id      - the assignment to which the job 'self' is referring
        assigned_to_id     - the user that job 'self' was assigned to
        content            - the content of the job 'self'
        taken_by_user_id   - the id of the user taking job 'self'

        this function acts as the constructor to define a new job object
        """
        self.id               = id
        self.created          = created
        self.created_by       = created_by
        self.section_id       = section_id
        self.type             = type
        self.assessment_id    = assessment_id
        self.assigned_to_id   = assigned_to_id
        self.content          = content
        self.taken_by_user_id = taken_by_user_id

        @classmethod
        def noID(self, created, created_by, section_id, type, assessment_id, assigned_to_id, content, taken_by_user_id):
            """
            the parameters correspond with the parameters in the constructor above

            returns a new job with the id parameter set as None and the other
            parameters as they are passed in

            this function acts as a second constructor where you have created a
            job that has not yet been assigned an id from the database
            """
            return self(None, created, created_by, section_id, type, assessment_id, assigned_to_id, content, taken_by_user_id)
        def __eq__(self, other):
            """
            self  - the job in question
            other - another job that you are comparing 'self' to

            returns a boolean telling if the attributes of 'self' and 'other'
            are the same

            this function overrides the way python compares two jobs
            and decides if they are equal instead of checking if they are
            the exact same object
            """
            return (
            self.id                == other.id                and
            self.created           == other.created           and
            self.created_by        == other.created_by        and
            self.section_id        == other.section_id        and
            self.type              == other.type              and
            self.assessment_id     == other.assessment_id     and
            self.assigned_to_id    == other.assigned_to_id    and
            self.content           == other.content           and
            self.taken_by_user_id  == other.taken_by_user_id)
        def setID(self, id):
            """
            self - the job in question
            id   - the id for the job from the database

            this function allows you to assign an id to the job after
            inserting it into the database
            """
            self.id = id
        def __str__(self):
            """
            self - the job in question

            returns a string that fully describes the job 'self'

            this function allows you to convert the job object into
            a human-readable string for viewing the information in it
            """
            string = ""
            string += "id: "             + str(self.id)              + "\n"
            string += "created: "        + str(self.created)         + "\n"
            string += "created by: "     + str(self.created_by)      + "\n"
            string += "\nsection id: "   + str(self.section_id)      + "\n"
            string += "type: "           + str(self.type)            + "\n"
            string += "assessment id: "  + self.assessment_id        + "\n"
            string += "assigned to id: " + self.assigned_to_id       + "\n"
            string += "content: "        + self.content              + "\n"
            string += "taken by user:"   + self.taken_by_user_id     + "\n"

            return string
        def toJson(self):
            data = [{
            "id"                : self.id,
            "created"           : self.created,
            "created_by"        : self.created_by,
            "section_id"        : self.section_id,
            "type"              : self.type,
            "assessment id"     : self.assessment_id,
            "assigned to id"    : self.assigned_to_id,
            "content"           : self.content,
            "take by user id"   : self.take_by_user_id
            }]
            return json.dumps(data)
