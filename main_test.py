from dotenv import load_dotenv
import os
from pymongo import MongoClient
import pandas as pd

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

cursor = feb_db.FEB3_players_statistics.find()

df_stats = pd.DataFrame(list(cursor))

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


df_stats[df_stats["player_feb_id"] == "1025355"]
