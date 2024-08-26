import mysql.connector
from mysql.connector import Error

class DataBaseManager:
    def __init__(self, host, user, password, database=None) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self, use_database=True):
        try:
            # ! Conectar sin especificar la base de datos 
            if use_database and self.database:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
            else:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password
                )

            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Conexión exitosa")
            else:
                print("Fallo al conectar")
                self.conn = None
        except Error as e:
            print(f"Error: {e}")
            self.conn = None
            self.cursor = None

    def create_database(self, db_name):
        try:
            # ! Conectar sin base de datos para poder crear una
            self.connect(use_database=False)
            if self.cursor is not None:
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"Base de datos {db_name} creada exitosamente")

                # ! Reconectar usando la base de datos recién creada
                self.database = db_name
                self.close()  # ! Cerrar la conexión anterior
                self.connect()  # ! Conectar de nuevo con la base de datos especificada
            else:
                print("No se puede crear la base de datos, la conexión no está establecida.")
        except Error as e:
            print(f"Error al crear base de datos: {e}")
        finally:
            self.close()

    def execute_query(self, query):
        try:
            if self.conn is None or not self.conn.is_connected():
                self.connect()
            if self.cursor is not None:
                self.cursor.execute(query)
                self.conn.commit()
                print("Query ejecutada exitosamente!")
            else:
                print("No se puede ejecutar la query, la conexión no está establecida.")
        except Error as e:
            print(f"Error al ejecutar query: {e}")

    def fetch_all(self, query):
        try:
            if self.conn is None or not self.conn.is_connected():
                self.connect()
            if self.cursor is not None:
                self.cursor.execute(query)
                return self.cursor.fetchall()
            else:
                print("No se puede realizar fetch, la conexión no está establecida.")
                return None
        except Error as e:
            print(f"Error al hacer fetch: {e}")
            return None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Conexión cerrada.")
