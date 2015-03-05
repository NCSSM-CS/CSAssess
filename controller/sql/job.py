#!/usr/local/bin/python3

"""
created_by: Samuel Murray
create_date: 3/2/2015
last_modified_by: LZ
last_modified_date: 3/4/2015
"""

#imports
import constants
from user import User
from section import Section
from assessment import Assessment
import json
import mysql.connector
from mysql_connect_config import getConfig

class Job(object):
    'Job object to hold attributes and functions for a job.'
    def __init__(self, id, created, created_by, section, atype, assessment, assigned_to, content, taken_by_user, active):
        """
        self               - the job in question
        id                 - the id number of the job 'self' in the database
        created            - the date when the job 'self' was created
        created_by         - the user that created the job 'self'
        type               - the type of job 'self' is
        assignment         - the assignment to which the job 'self' is referring
        assigned_to        - the user that job 'self' was assigned to
        content            - the content of the job 'self'
        taken_by_user      - the id of the user taking job 'self'
        active             - bit specifying whether job is active or inactive

        this function acts as the constructor to define a new job object
        """
        self.id            = id
        self.created       = created
        self.created_by    = created_by
        self.section       = section
        self.atype         = atype
        self.assessment    = assessment
        self.assigned_to   = assigned_to
        self.content       = content
        self.taken_by_user = taken_by_user
        self.active        = active

    @classmethod
    def noID(self, created, created_by, section, atype, assessment, assigned_to, content, taken_by_user, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new job with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        job that has not yet been assigned an id from the database
        """
        return self(None, created, created_by, section, atype, assessment, assigned_to, content, taken_by_user, active)

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
        self.section           == other.section           and
        self.atype             == other.atype             and
        self.assessment        == other.assessment        and
        self.assigned_to       == other.assigned_to       and
        self.content           == other.content           and
        self.taken_by_user     == other.taken_by_user     and
        self.active            == other.active
        ) if type(other) is Job else False

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
        string += "active: "         + str(self.active)          + "\n"
        string += "section: "        + str(self.section)         + "\n"
        string += "type: "           + str(self.atype)           + "\n"
        string += "assessment: "     + self.assessment           + "\n"
        string += "assigned to: "    + self.assigned             + "\n"
        string += "content: "        + self.content              + "\n"
        string += "taken by user:"   + self.taken_by_user        + "\n"

        return string

    def add(self):

        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is None:
            insert = ("INSERT INTO job (created_by, type, assignment_id, assigned_to_id, content, taken_by_user_id, active) VALUES (%s, '%s', %s, %s, '%s', %s, %s);" % (self.created_by.id, self.atype, self.assessment.id, self.assigned_to.id, self.content, self.taken_by_user.id, self.active))
            cursor.execute(insert)

            select = "SELECT LAST_INSERT_ID();"

            cursor.execute(select)

            for(id) in cursor:
                self.id=id

        cnx.commit()
        cursor.close()
        cnx.close()

    def update(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = ("UPDATE job SET type = '%s', assignment_id = %s, assigned_to_id = %s, content = '%s', taken_by_user_id = %s, active = %s;" % (self.atype, self.assignment_id, self.assigned_to_id, self.content, self.taken_by_user_id, self.active))
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.active is not None:

            self.active = int(bool)
            update = ("UPDATE job SET active=%s WHERE id=%s;" % (int(bool), self.id))

            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    @classmethod
    def get(self, search="all", searchAssignedTo=None, searchTakenBy=None, testActive="1"):
        """

        """
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        returnList = []
        query = ""
        if search == "all":
            query = "SELECT * FROM job"
        elif searchAssignedTo is not None:
            query = ("SELECT * FROM job WHERE assigned_to_id = %s" % (searchAssignedTo.id))
        elif searchTakenBy is not None:
            query = ("SELECT * FROM job WHERE taken_by_user_id = %s" % (searchTakenBy.id))
        elif type(search) is int:
            query = ("SELECT * FROM job WHERE id = %s" % (search))
        elif type(search) is User:
            query = ("SELECT * FROM job WHERE created_by = %s" % (search.id))
        elif type(search) is Section:
            query = ("SELECT * FROM job WHERE section_id = %s" % (search.id))
        elif type(search) is str:
            query = ("SELECT * FROM job WHERE type = '%s'" % (search))

        query += (" WHERE active=%s;" if search == "all" else " AND active=%s;") % (testActive)
        cursor.execute(query)

        for (id, created, created_by, section_id, atype, assessment_id, assigned_to, content, taken_by, active) in cursor:

            user = User.get(created_by)[0]
            section = Section.get(section_id)[0]
            assessment = Assessment.get(assessment_id)[0]
            assignedTo = User.get(assigned_to)[0]
            takenBy = User.get(taken_by)[0]
            returnList.append(Job(id, created, user, section, atype, assessment, assignedTo, content, takenBy, active))

        cnx.commit()
        cursor.close()
        cnx.close()

        return returnList


    def toJson(self):
        data = {
        "id"          :     self.id,
        "created"     : str(self.created),
        "createdBy"  :     self.created_by,
        "active"      :     self.active,
        "section"     :     self.section,
        "type"        :     self.atype,
        "assessment"  :     self.assessment,
        "assignedTo" :     self.assigned_to,
        "content"     :     self.content,
        "takenBy"    :     self.taken_by_user
        }
        return json.dumps(data)
