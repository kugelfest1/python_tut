# excerpz from pymongo tut, https://www.mongodb.com/docs/drivers/pymongo/
# 2023-04-13

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Replace the placeholder with your Atlas connection string
# hint: running mongodb locally (mongodb atlas)
uri = "mongodb://localhost:27017"
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
                          
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)