#!/usr/local/bin/python3

"""
created_by:         Micah Halter
created_date:       3/3/2015
last_modified_by:   John Fang
last_modified date: 3/5/2015
"""

# imports
import constants
import json
import mysql.connector
from sql.user import User
from sql.mysql_connect_config import getConfig

# classes
class Session(object):

    def __init__(self, id, timestamp, token, ip, user, active):
        """
        self        - the session in question
        id          - the id number of the session 'self' in the database
        timestamp   - the time at which the session 'self' started
        token       - a unique 64-bit string for a session 'self'
        user        - the user partaking in the session 'self'
        active      - a bit specifying whether the session is active

        this function acts as the constructor to define a new session object
        """
        self.id         = id
        self.timestamp  = timestamp
        self.token      = token
        self.ip         = ip
        self.user       = user
        self.active     = active

    @classmethod
    def noID(self, token, ip, user, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new assessment with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        topic that has not yet been assigned an id from the database
        """
        return self(None, None, token, ip, user, active)

    @classmethod
    def get(self, searchToken, searchIP, testActive=1):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        returnList = []
        query = "SELECT * FROM session WHERE token='%s' AND ip='%s' AND active=%s;" % (searchToken, searchIP, testActive)
        cursor.execute(query)

        for (id, timestamp, token, ip, user_id, active) in cursor:
            user = User.get(user_id)[0]
            returnList.append(Session(id, timestamp, token, ip, user, active))

        cnx.commit()
        cursor.close()
        cnx.close()

        return returnList

    def add(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is None:
            insert = ("INSERT INTO session (token, ip, user_id, active) VALUES ('%s', '%s', %s, %s);" % (self.token, self.ip, self.user.id, self.active))
            cursor.execute(insert)

            select = "SELECT LAST_INSERT_ID();"
            cursor.execute(select)

            for (id) in cursor:
                    self.id = id[0]

            select = ("SELECT timestamp FROM session WHERE id=%s;" % (self.id))

            cursor.execute(select)
            for (timestamp) in cursor:
                self.timestamp = timestamp[0]

        cnx.commit()
        cursor.close()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            self.active = int(bool)
            update = ("UPDATE session SET active=%s WHERE id=%s" % (int(bool), self.id))
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def __eq__(self, other):
        """
        self  - the topic in question
        other - other topic that you are comparing 'self' to

        returns a boolean telling if the attributes of 'self'
        and 'other' are the same

        this function overrides the way python compares two topics
        and decides if they are equal instead of checking if they
        are the exact same object
        """
        return (
        self.id         == other.id         and
        self.timestamp  == other.timestamp  and
        self.token      == other.token      and
        self.ip         == other.ip         and
        self.user       == other.user       and
        self.active     == other.active
        ) if type(other) is Session else False

    def __str__(self):
        """
        self - the topic in question

        returns a string that fully describes the assessment 'self'

        this function allows you to convert the topic object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "        + str(self.id)        + "\n"
        string += "timestamp: " + str(self.timestamp) + "\n"
        string += "token: "     + str(self.token)     + "\n"
        string += "ip: "        +     self.ip         + "\n"
        string += "user: "      + str(self.user)      + "\n"
        string += "active: "    + str(self.active)    + "\n"
        return string
    def toJson(self):
        data = {
                "id"        : self.id,
                "timestamp" : str(self.timestamp),
                "token"     : self.token,
                "ip"        : self.ip,
                "user"      : self.user,
                "active"    : self.active
                }
        return json.dumps(data)

