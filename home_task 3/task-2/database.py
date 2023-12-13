import psycopg2


class Database:
    def __init__(self, db_name, db_host, db_port, db_user, db_psw):
        self.conn = psycopg2.connect(dbname=db_name, dbhost=db_host, dbport=db_port, dbuser=db_user, dbpsw=db_psw)
        self.cursor = self.conn.cursor()


    def create_table(self, table_query):
        try:
            self.cursor.execute(table_query)
            return 'Table successfully created'
        except Exception as e:
            return f'Error {e}'

    def insert_rows(self, table_name, col_name, row_name):


    def __del__(self):
        self.conn.close()
        self.cursor.close()