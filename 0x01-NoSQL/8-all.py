#!/usr/bin/env python3
"""
Task 8: a Python function
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    """
    all_docs = []
    for doc in mongo_collection.find():
        all_docs.append(doc)
    return all_docs
