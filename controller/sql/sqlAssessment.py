#!/usr/bin/python

"""
created_by:
"""

"""
TODO
"""

#imports
import sys

sys.path.insert(0, "..")
import constants 

sys.path.insert(0, constants.DIR + "objects")
from assessment import Assessment

def insertAssessment(assessment):
    insertAssess = ("INSERT INTO assessment (created, created_by, type, section_id, name) VALUES ('%s', %s, '%s', %s, '%s');" % (assessment.created, assessment.created_by.id, assessment.type, assessment.section.id, assessment.name))

