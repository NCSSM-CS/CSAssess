#!/usr/bin/python3

from user import User
from course import Course
from assessment import Assessment
from section import Section
from topic import Topic
from question import Question
from job import Job
from session import Session


y = Session.get()

for i in y:
    print(i)
