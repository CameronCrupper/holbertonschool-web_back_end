#!/usr/bin/env python3
"""
List all documents in Python
"""
import pymongo


def list_all(mongo_collection) -> list:
    """
    return empty list if no documents are in the collection
    """
    documents: list = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
