import psycopg2
from config import Config

def get_db_connection():
    connection = psycopg2.connect(
        host=Config.DB_HOST,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    return connection
