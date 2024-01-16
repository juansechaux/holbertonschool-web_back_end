#!/usr/bin/env python3
'''
Python function that inserts a new document in a collection based on kwargs
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Python function that inserts a new document in a collection based on kwargs
    '''
    results = mongo_collection.insert_many([kwargs])
    return results.inserted_ids
