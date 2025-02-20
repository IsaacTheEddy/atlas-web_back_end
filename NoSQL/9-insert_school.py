#!/usr/bin/env python3
"""
Inserts a new documentation in a collection
"""
from pymongo import mongo_client
from typing import List


def insert_school(mongo_collection:str, **kwargs:str) -> str:
    """
    Inserts a new document thats passed to this function

    Args:
    mongo_collection: the target collection
    **kwargs: the new document to be added

    Returns:
    A string representation of the inserted document id
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
