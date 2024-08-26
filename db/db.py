from ast import Try
import mysql.connector
from mysql.connector import Error

# ! CLASE DE LA BASE DE DATOS
class DataBaseManager:
    def __init__(self, host, user, password, database=None) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
    
    
# ! METODO DE CONEXION
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host ,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Conexion exitosa")
        except Error as e:
            print(f"Error: {e}")
            
# ! METODO DE CREACION DE DB
    def create_database(self, db_name):
        try:
            self.connect()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Base de datos {db_name} creada exitosamente")
        except Error as e:
            print(f"Error al crear base de datos: {e}")
        finally:
            self.close()

# ! Ejecutar query
    def execute_query(self, query):
        try:
            if self.conn is None or self.conn.is_closed():
                self.connect()
            self.cursor.execute(query)
            self.conn.commit()
            print("Query ejecutada exitosamente!")
                
        except Error as e:
            print(f"Error al ejecutar query: {e}")
            
# ! Fetch all
    def fetch_all(self, query):
        try:
            if self.conn is None or self.conn.is_closed():
                self.connect()
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error al hacer fetch: {e}")
            return None
        
# ! Cerrar la conexion 
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Conexion cerrada.")