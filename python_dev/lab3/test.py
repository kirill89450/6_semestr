import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INT PRIMARY KEY,
   last_name STRING,
   first_name STRING,
   email STRING,
   profession STRING,
   gender STRING,
   motivation STRING,
   in_mars STRING);
   
""")
conn.commit()