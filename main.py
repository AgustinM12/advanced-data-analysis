import mysql.connector
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

# Importar los datos de un archivo csv
csv = rcsv("data_employee.csv")

# Query para la insercion de dataframe en la db
insert_query = """
INSERT INTO EmployeePerformance (id, employee_id, department, performance_score, years_with_company, salary)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Iterar sobre el df para crear los registros
for i, row in csv.iterrows():
    my_db_cursor.execute(insert_query, tuple(row))

# Confirma los cambios
my_db_conn.commit()

# Cerramos la conexión
my_db_cursor.close()
my_db_conn.close()
