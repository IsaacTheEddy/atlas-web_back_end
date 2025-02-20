#!/usr/bin/env python3
from typing import List
from pymongo import mongo_client
"""
Lists all the documents in a collection
"""


def list_all(mongo_collection: str) -> List[str]:
    """
    List all the documents in a collection

    Args:
    mongo_collection: THe collection name to returned
    """
    return mongo_collection.find()
