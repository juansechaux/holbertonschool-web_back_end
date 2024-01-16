#!/usr/bin/env python3
'''
Python function that inserts a new document in a collection based on kwargs
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Python function that inserts a new document in a collection based on kwargs
    '''
    for key, value in kwargs.items():
        result = mongo_collection.insert_one({key: value})
    return result.inserted_id
