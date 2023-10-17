#!/usr/bin/env python3
"""
Task 15: a python function
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    logs_collection = client.logs.nginx

    # Count total logs
    total_logs = logs_collection.count_documents({})

    print(f"{total_logs} logs")

    # Count methods
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    # Count status check
    status_check = logs_collection.count_documents({"status_code": "200"})
    print(f"{status_check} status check")

    # Count top IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    top_ips = list(logs_collection.aggregate(pipeline))

    print("IPs:")
    for ip in top_ips:
        print(f"    {ip['_id']}: {ip['count']}")
