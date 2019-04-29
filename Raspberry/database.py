from pymysql import *

class Database():

    def __init__(self):

        self.host = 'localhost'
        self.port = 3306
        self.database = 'smarthome'
        self.user = 'root'
        self.password = 'tianchao'
        self.charset = 'utf8'

    def connection(self):

        conn = connect(host=self.host, port=self.port, database=self.database,
                user=self.user, password=self.password, charset=self.charset)

        cs = conn.cursor()

        return conn, cs

    def close(self, conn, cs):

        conn.close()
        cs.close()


    def insert(self,params):

        conn, cs = self.connection()
        cs.execute('insert into bedroom(tem,hum,light,ray,time) values(%s, %s, %s, %s, %s)', params)
        cs.execute('insert into livingroom(tem,hum,light,ray,time) values(%s, %s, %s, %s, %s)', params)
        conn.commit()
        self.close(conn, cs)
