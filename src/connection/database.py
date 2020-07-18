import mariadb
import sys

try:
    conn = mariadb.connect(
        user="quiz",
        password="Brote94",
        host="localhost",
        port=3306,
        database="quiz"
    )
    print("MariaDB is connected...")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
# return conn.cursor()
