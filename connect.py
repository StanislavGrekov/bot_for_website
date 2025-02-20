import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('user')
DB_PASSWORD = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')


conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host='127.0.0.1', port="5432")
cursor = conn.cursor()