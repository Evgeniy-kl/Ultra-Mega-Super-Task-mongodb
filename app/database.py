import os
import pymongo as pm

from schema import Statistic

client = pm.MongoClient(
    f"mongodb://{os.getenv('host')}:{os.getenv('port')}",
    port=int(os.getenv('port')),
    directConnection=bool(os.getenv('directConnection')))
print(client.server_info())
database = client.static_database
collection = database.stats


async def fetch_one_statistic(email):
    document = collection.find_one({"email": email}, {'_id': 0})
    print(document)
    return document


async def fetch_all_statistic():
    stats = []
    cursor = collection.find({})
    for document in cursor:
        stats.append(Statistic(**document))
    return stats


async def create_statistic(stats):
    document = stats
    collection.insert_one(document)
    del [document['_id']]
    return document


async def update_statistic(count, email):
    collection.update_one({"email": email},
                          {"$set": {"count": count}})
    document = collection.find_one({"email": email})
    return document


async def delete_statistic(email):
    collection.delete_one({"email": email})
    return True
