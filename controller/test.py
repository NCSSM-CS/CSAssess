#!/usr/local/bin/python3

from sql.answer import Answer
from sql.assessment import Assessment
from sql.comment import Comment
from sql.course import Course
from sql.job import Job
from sql.question import Question
from sql.section import Section
from sql.session import Session
from sql.test_case import Test_Case
from sql.topic import Topic
from sql.user import User

user = User.get(6)[0]

section = Section.get(None, None, None, user)

print(section)
