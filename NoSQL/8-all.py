#!/usr/bin/env python3
"""
Lists all the documents in a collection
"""
from typing import List
from pymongo import mongo_client


def list_all(mongo_collection: str) -> List[str]:
    """
    List all the documents in a collection

    Args:
    mongo_collection: THe collection name to returned

    Returns:
    A string representation of the availible databases:
    """
    return mongo_collection.find()
