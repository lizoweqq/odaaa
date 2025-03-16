from pymongo import MongoClient
import sys

try:
    MONGO_URI = "mongodb+srv://liziasadffr:mKaBZ0D0BmXwYuvM@cluster0.oey8m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # підключення
    client.server_info()
    print("Successfully connected to MongoDB Atlas")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    sys.exit(1)

db = client["group"]
tours_collection = db["tours"]