from db.db import DataBaseManager
from analisis.data_analisis import DataAnalyzer 
from graphics.graphics import DataVisualizer
from df_pandas import read_csv
import pandas as pd

# * Configuración de la conexión
host = 'localhost'
user = 'root'
password = ''
database = 'test_db'

# * Crear instancia del gestor de base de datos
db_manager = DataBaseManager(host, user, password, database)

# * Crear base de datos
db_manager.create_database('test_db')

# * Ejecutar una consulta para crear una tabla
create_table_query = """
CREATE TABLE IF NOT EXISTS EmployeePerformance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    department VARCHAR(255) NOT NULL,
    performance_score FLOAT NOT NULL,
    years_with_company INT NOT NULL,
    salary FLOAT NOT NULL
)
"""
db_manager.execute_query(create_table_query)

# * lectura del archivo csv 
csv = read_csv("data_employee.csv")

# * Verificar que ya no existan datos
check_count_query = "SELECT COUNT(*) FROM EmployeePerformance"
row_count = db_manager.fetch_all(check_count_query)[0][0]

# * Insertar datos si no hay registros aun
if row_count == 0:
    insert_query = """
        INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary)
        VALUES (%s, %s, %s, %s, %s)
        """
    # ! Iterar sobre el DataFrame e insertar los registros

    for i, row in csv.iterrows():
        # !  Extraer solo las columnas relevantes
        data = (
            row['employee_id'],
            row['department'],
            row['performance_score'],
            row['years_with_company'],
            row['salary']
        )
        db_manager.cursor.execute(insert_query, data)
        
     # * Confirmar los cambios
    db_manager.conn.commit()
    print("Se insertaron los registros de manera exitosa")
else: 
    print("Ya hay registros")

select_query = "SELECT * FROM EmployeePerformance"
all_users = db_manager.fetch_all(select_query)


# ! Crear un DataFrame a partir de los registros obtenidos
column_names = ["id", "employee_id", "department", "performance_score", "years_with_company", "salary"]

df = pd.DataFrame(all_users, columns=column_names)


#  * Uso del analisis de datos
analyzer = DataAnalyzer(df)
analysis_results = analyzer.analyze()
print("Resultado del analisis de los datos:", analysis_results)


# * Visualizacion de graficos
visualizer = DataVisualizer(df)
visualizer.graphic_data1()
visualizer.graphic_data2()
visualizer.graphic_data3()