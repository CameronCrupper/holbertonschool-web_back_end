#!/usr/bin/env python3
"""
Change school topics
"""
import pymongo
from typing import List


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of school document based on the name
    """
    query: dict = { "name": name }
    mongo_collection.update_many(query, { "$set": { "topics": topics }})
