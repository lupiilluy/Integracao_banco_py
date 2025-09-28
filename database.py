import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host='127.0.0.1', user='root', password='', database='db_pedidos', port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexão com MySQL estabelecida")
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    def execute_query(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            print("Erro: conexão com o banco não estabelecida")
            return None

        cursor = self.connection.cursor(buffered=True)
        try:
            if params is None:
                cursor.execute(query)
            else:
                if not isinstance(params, (tuple, list)):
                    params = (params,)
                cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Erro ao executar query: {e}")
            return None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com MySQL fechada")
