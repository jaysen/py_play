from pymongo import MongoClient
from base64 import b64decode
from bson.binary import Binary, UUID_SUBTYPE


def base64_to_bindata(base64_string):
    # Decode the base64 string to bytes
    decoded_bytes = b64decode(base64_string)

    # Convert bytes to MongoDB Binary with UUID subtype (which is usually 3 or 4)
    return Binary(decoded_bytes, UUID_SUBTYPE)  # Use the appropriate subtype


# Your base64 string
base64_string = 'AVvGlmbL7kWRZnUNc6rXkg=='

# Convert the base64 string to Binary
bindata = base64_to_bindata(base64_string)
print(bindata)




## Connect to your MongoDB
#client = MongoClient('localhost', 27017)  # Adjust connection info as needed

## Select your database and collection
#db = client['your_database']
#collection = db['your_collection']

## Query using the Binary data
#results = collection.find({"projectId": bindata})

## Print out the results
#for document in results:
#    print(document)
