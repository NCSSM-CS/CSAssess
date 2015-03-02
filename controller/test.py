#!/usr/bin/python2.7

import constants
import sys

sys.path.insert(0, "./view/")
import viewAssessment
import viewQuestion
import viewTopic
import viewSection
import viewCourse
import viewUser

sys.path.insert(0, "./edit/")
import editAssessment
import editQuestion
import editTopic
import editSection
import editCourse

sys.path.insert(0, "./objects/")
from assessment import Assessment
from question import Question
from topic import Topic
from section import Section
from course import Course
from user import User

print(viewAssessment.byID(1).sortByTopic())
