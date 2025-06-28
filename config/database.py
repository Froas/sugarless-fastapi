from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://frotherdrone:frotdfsa21124afSADF1@sugar.nkkiqc4.mongodb.net/?retryWrites=true&w=majority&appName=Sugar"
client = MongoClient(uri)

db = client.sugar_db

collection = db["sugar_data"]

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)