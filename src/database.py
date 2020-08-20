import mysql.connector
import sys

try:
    conn = mysql.connector.connect(
        user="quizUser",
        password="Brote94",
        host="localhost",
        database="quiz"
    )
    print("MariaDB is connected...")
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
mydb = conn
# return conn.cursor()
