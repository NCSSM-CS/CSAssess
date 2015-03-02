#!/usr/bin/python2.7

import constants
import sys

import viewAssessment
import viewQuestion
import viewTopic
import viewSection
import viewCourse
import viewUser
import viewComment

import editAssessment
import editQuestion
import editTopic
import editSection
import editCourse

from assessment import Assessment
from question import Question
from topic import Topic
from section import Section
from course import Course
from user import User

print(viewComment.byID(1))
