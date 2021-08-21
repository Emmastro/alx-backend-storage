#!/usr/bin/env python3
"""
find by topic
"""
import pymongo


def log_stats(a: dict) -> int:
    """log"""
    # connect to default host (localhost)
    connection = pymongo.MongoClient()
    logs = connection.logs.nginx
    return logs.count_documents(a)


def main_function():
    """
    Entry point
    """
    print(f"{log_stats({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {log_stats({'method': 'GET'})}")
    print(f"\tmethod POST: {log_stats({'method': 'POST'})}")
    print(f"\tmethod PUT: {log_stats({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {log_stats({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {log_stats({'method': 'DELETE'})}")
    print(f"{log_stats({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main_function()
