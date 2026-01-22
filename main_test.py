from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")

conn = f"mongodb+srv://{db_user}:{db_password}@cluster0.lv4geon.mongodb.net/"

client = MongoClient(conn)

databases = client.list_database_names()

print("Bases de datos disponibles:")
for db in databases:
    print("-", db)
    
    
feb_db = client['feb_db']

# collections = feb_db.list_collection_names()

# for i in range(len(collections)):
    # print("-", collections[i])

# print(collections)

shots = feb_db.get_collection('FEB3_players_shots').find_one("{player_number: 9}")

print(shots)