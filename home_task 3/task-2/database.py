import psycopg2


class Database:
    def __init__(self, db_name, db_host, db_port, db_user, db_psw)
        self.conn = psycopg2.connect(dbname = db_name, dbhost = db_host, dbport = db_port, dbuser = db_user, dbpsw = db_psw)
        self.crusor = self.conn.crusor()

        

