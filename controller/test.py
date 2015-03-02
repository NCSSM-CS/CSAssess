#!/usr/bin/python2.7
"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified_date: 3/2/2015
"""

#imports
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

# functions
def main():
    print(viewAssessment.byID(1).sortByTopic())

# running code
if __name__ == "__main__":
    main()
