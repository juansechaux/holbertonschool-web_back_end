#!/usr/bin/env python3
'''
Python function that lists all documents in a collection
'''


def list_all(mongo_collection):
    '''
    Python function that lists all documents in a collection
    '''
    list_of_data = [data for data in mongo_collection.find()]
    return list_of_data
