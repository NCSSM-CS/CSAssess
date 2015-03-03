#!/usr/bin/env pyhton2.6

"""
created_by: Samuel Murray
create_date: 3/2/2015
last_modified_by: John Fang
last_modified_date: 3/2/2015
"""

#imports
import constants
import json

class Job:
    'Job object to hold attributes and functions for a job.'
    def __init__(self, id, created, created_by, section_id, type, assessment_id, assigned_to_id, content, taken_by_user_id, active):
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
	active             - bit specifying whether job is active or inactive

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
	self.active           = active

        @classmethod
        def noID(self, created, created_by, section_id, type, assessment_id, assigned_to_id, content, taken_by_user_id, active):
            """
            the parameters correspond with the parameters in the constructor above

            returns a new job with the id parameter set as None and the other
            parameters as they are passed in

            this function acts as a second constructor where you have created a
            job that has not yet been assigned an id from the database
            """
            return self(None, created, created_by, section_id, type, assessment_id, assigned_to_id, content, taken_by_user_id, active)
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
            self.taken_by_user_id  == other.taken_by_user_id  and
	    self.active            == other.active)

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
	    string += "active: "         + str(self.active)          + "\n"

	    return string

	def add(self):

	    if self.id is not None:
	        return

	    cnx = mysql.connector.connect(**getConfig())
	    cursor = cnx.cursor()

	    insert = ("INSERT INTO job (id, created, created_by, type, assignment_id, assigned_to_id, content, taken_by_user_id, active) VALUES (%s, '%s', %s, '%s', %s, %s, '%s', %s, %s); SELECT LAST_INSERT_ID();" % (self.id, self.created, self.created_by.id, self.type, self.assessment_id, self.assigned_to_id, self.content, self.taken_by_user_id, self.active))

	    cursor.execute(insert)

	    for(id) in cursor:
	        self.id=id

	    cnx.commit()
	    cursor.close()
	    cnx.close()

	def update(self):
	    cnx = mysql.connector.connect(**getConfig())
	    cursor = cnx.cursor()

	    if self.id is not None:
	    	update = ("UPDATE job SET type = '%s', assignment_id = %s, assigned_to_id = %s, content = '%s', taken_by_user_id = %s, active = %s;" % (self.type, self.assignment_id, self.assigned_to_id, self.content, self.taken_by_user_id, self.active))
		cursor.execute(update)

	    cnx.commit()
	    cursor.close()
	    cnx.close()

	def activate(self, bool):
	    cnx = mysql.connector.connect(**getConfig())
	    cursor = cnx.cursor()

	    if self.active is not None:

	        self.active = int(bool)
	        active = ("UPDATE job SET active=%s WHERE id=%s;" % (int(bool), self.id))

	        cursor.execute()

	    cnx.commit()
	    cursor.close()
	    cnx.close()

	@classmethod
	def get(self, search="all", searchAssignedTo=None, searchTakenBy="None", testActive="1"):
	    """

	    """
	    cnx = mysql.connector.connect(**getConfig())
	    cursor = cnx.cursor()

	    returnList = []
	    query = ""
	    if search == "all" and searchAssignedTo is None and searchTakenBy is None:
	    	query = "SELECT * FROM job"
	    elif searchAssignedTo is not None:
	        query = ("SELECT * FROM job WHERE assigned_to_id = %s" % (searchAssignedTo))
	    elif searchTakenBy is not None:
	        query = ("SELECT * FROM job WHERE taken_by_user_id = %s" % (searchTakenBy))
	    elif type(search) is int:
	    	query = ("SELECT * FROM job WHERE id=%s" % (search))
	    elif type(search) is user:
	    	query = ("SELECT * FROM job WHERE created_by=%s" % (search.id))
	    elif type(search) is section:
	        query = ("SELECT * FROM job WHERE section_id=%s" % (search.id))
	    elif type(search) is str:
	        query = ("SELECT * FROM job WHERE type='%s'" % (search))

	    query += "AND active=%s;" % (testActive)
	    cursor.execute(query)

	    for (id, created, created_by, section_id, type, assessment_id, assigned_to_id, content, taken_by_user_id, active) in cursor:

		user = User.get(created_by)[0]
		newJob = Job(id, created, user, section_id, type, assessment_id, assigned_to_id, content, taken_by_user_id, active)

		if newJob not in returnList:
		    returnList.append(newJob)

	    cnx.commit()
	    cursor.close()
	    cnx.close()

	    return returnList


        def toJson(self):
            data = [{
            "id"                :     self.id,
            "created"           : str(self.created),
            "created_by"        :     self.created_by,
            "section_id"        :     self.section_id,
	    "type"              :     self.type,
            "assessment id"     :     self.assessment_id,
            "assigned to id"    :     self.assigned_to_id,
            "content"           :     self.content,
            "taken by user id"  :     self.taken_by_user_id
            }]
            return json.dumps(data)
