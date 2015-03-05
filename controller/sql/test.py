#!/usr/bin/python3

from user import User
from course import Course
from assessment import Assessment
from section import Section
from topic import Topic
from question import Question
from job import Job
from session import Session

x = User.get(1)[0]

y = Question.get(1)[0]

z = Topic.get(y)
