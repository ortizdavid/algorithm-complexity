import sqlite3

conn = sqlite3.connect('db_customers.db')

class SQLite:
    
    @classmethod
    def create_table(cls):
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS customers;")
        cursor.execute("CREATE TABLE customers(id INTEGER AUTO INCREMENT PRIMARY KEY, name varchar(50), age INTEGER, gender VARCHAR(12), created_at DATE);")
        conn.commit()

    @classmethod
    def insert(cls, name, age, gender, created_at):
        cursor = conn.cursor()
        params = (name, age, gender, created_at)
        cursor.execute(f"INSERT INTO customers(name, age, gender, created_at) VALUES (?, ?, ?, ?)", params)
        conn.commit()
