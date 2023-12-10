import psycopg2


class Database:
    def __init__(self, db_name, db_host, db_port, db_user, db_psw):
        self.conn = psycopg2.connect(dbname=db_name, dbhost=db_host, dbport=db_port, dbuser=db_user, dbpsw=db_psw)
        self.crusor = self.conn.crusor()


    def __del__(self):
        self.conn.close()
        self.crusor.close()


    def create_table(self, table_query):
        try:
            self.crusor.execute(table_query)
            return 'Table successfully created'
        except Exception as e:
            return f'Error {e}'


        

