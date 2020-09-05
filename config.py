import os
from dotenv import load_dotenv


MONGO_HOST = os.getenv("MONGO_HOST")
print(MONGO_HOST)
DB = os.getenv('MONGO_DB')
PORT = os.getenv('MONGO_PORT')
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')