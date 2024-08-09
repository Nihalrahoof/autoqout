import os
import mysql.connector

__cnx = None

def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(
            host=os.getenv('mysql.railway.internal'),
            user=os.getenv('root'),
            password=os.getenv('kuQGNpXVYhtiVnEFPSEnjXaLFDjouXLG'),
            database=os.getenv('railway'),
            port=os.getenv('DB_PORT', 3306)  # Default to 3306 if not set
        )

    return __cnx
