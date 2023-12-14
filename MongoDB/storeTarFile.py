import bson
from pymongo import MongoClient
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, '20230629203222\\20230629203222\\evallo')

with open(file_path, 'rb') as file:
    binary_data = bson.Binary(file.read())

 
# Connect to MongoDB
client = MongoClient('${process.env.MONGODB}')
db = client['evalloDB']
collection = db['evallo']

# Insert the binary data
document = {'file_data': binary_data}
collection.insert_one(document)
