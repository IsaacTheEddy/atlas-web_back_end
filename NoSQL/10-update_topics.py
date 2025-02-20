#!/usr/bin/env python3
"""Updates the topics of school documents"""

def update_topics(mongo_collection:str, name:str, topics:str) -> None:
    """
    Changes the topics of the school document

    Args:
        mongo_collection: pymongo collection object.
        name: The school name to update.
        topics : List of topics approached in the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}})
