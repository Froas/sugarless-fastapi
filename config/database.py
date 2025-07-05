from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

# uri = os.getenv("URL")
user = quote_plus(os.getenv("MONGO_USER"))
passWord = quote_plus(os.getenv("MONGO_PASSWORD"))
cluster = os.getenv("MONGO_CLUSTER")
db =os.getenv("MONGO_DB")

url = f'mongodb+srv://{user}:{passWord}@{cluster}/?retryWrites=true&w=majority&appName={db}'
print(url)
client = MongoClient(url)

db = client.sugar_db

collection = db["sugar_data"]

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)