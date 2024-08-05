import mysql.connector
import pandas as pd
from df_pandas import  read_csv as rcsv

# Conexion a mysql
conn = mysql.connector.connect(host="localhost", user="root", password="")

# Creacion del cursor
cursor = conn.cursor()

# Creación de la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS CompanyData")
cursor.close()
conn.close()

# Conexion a la base de datos.
my_db_conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="CompanyData"
)

my_db_cursor = my_db_conn.cursor()

# Creación de una tabla
my_db_cursor.execute("""
CREATE TABLE IF NOT EXISTS EmployeePerformance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    department VARCHAR(255) NOT NULL,
    performance_score FLOAT NOT NULL,
    years_with_company INT NOT NULL,
    salary FLOAT NOT NULL
)
""")

# # Importar los datos de un archivo csv
csv = rcsv("data_employee.csv")


my_db_cursor.execute("SELECT COUNT(*) FROM EmployeePerformance")
row_count = my_db_cursor.fetchone()[0]

if(row_count == 0):
# # Query para la insercion de dataframe en la db
    insert_query = """
    INSERT INTO EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

# # Iterar sobre el df para crear los registros
    for i, row in csv.iterrows():
        my_db_cursor.execute(insert_query, tuple(row))

# Confirma los cambios
    my_db_conn.commit()
    print("Se incertaron los registros de manera exitosa")

# Ejecuta la consulta SQL para obtener todos los registros
my_db_cursor.execute("SELECT * FROM EmployeePerformance")
# Recupera todos los registros como una lista de tuplas
records = my_db_cursor.fetchall()
# Obtiene los nombres de las columnas
column_names = [desc[0] for desc in my_db_cursor.description]

# Cerramos la conexión
my_db_cursor.close()
my_db_conn.close()

# Crea un DataFrame de pandas a partir de los registros y nombres de columnas
db_df = pd.DataFrame(records, columns=column_names)

# Muestra el DataFrame
print(db_df)
