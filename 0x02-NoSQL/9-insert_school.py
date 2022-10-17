#!/usr/bin/env python3
"""
insert the document in python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert new document in collection based on kwargs
    """
    new_school = mongo_collection.insert_one(kwargs)
    return (new_school.inserted_id)
