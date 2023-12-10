import config

from database import Database

db = Database(config.DBNAME, config.HOST, config.PORT, config.USERNAME, config.PASSWORD)

table_query = """
    CREATE TABLE pupils (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(25) NOT NULL,
        last_name VARCHAR(25) NOT NULL     
    )
"""

print(db.create_table(table_query))