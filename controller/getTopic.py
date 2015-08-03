#!/usr/local/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/6/2015
"""

# imports
import utils
import json
from sql.topic import Topic
from sql.session import Session

# Format of JSON -KP
# requestType: getTopic


def iChooseU(form):
    
    topics = Topic.get()
    out = []

    for topic in topics:
        out.append(topic.toJson())

    return json.dumps({"topicList":out})
