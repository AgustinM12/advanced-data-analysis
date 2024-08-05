import numpy as np
import pandas as pd
from df_pandas import read_csv as rcsv

data = rcsv("data_employee.csv")

def data_analisis(df):
    # Agrupa los datos por departamento y campo
    grouped_by_department_score = df.groupby("department")["performance_score"]
    grouped_by_department_salary = df.groupby("department")["salary"]

    # # Calcula las estadísticas necesarias
    score_statistics = grouped_by_department_score.agg(["mean", "median", "std"])
    salary_statistics = grouped_by_department_salary.agg(["mean", "median", "std"])

    # Renombra las columnas para mayor claridad
    score_statistics.columns = ["Media", "Mediana", "Desviación Estándar"]
    salary_statistics.columns = ["Media", "Mediana", "Desviación Estándar"]

    # Agrupa los datos por departamento y cuenta los registros en cada grupo
    departments = df["department"].values
    years_with_company = df["years_with_company"].values
    performance_score = df["performance_score"].values
    salary = df["salary"].values

    unique_departments, counts = np.unique(departments, return_counts=True)

    # Crea un DataFrame con los resultados
    record_counts_df = pd.DataFrame(
        {"department": unique_departments, "Cantidad de Registros": counts}
    )

    # Calcula la correlación entre 'salary' y 'performance_score' usando numpy
    correlation_s_ps = np.corrcoef(salary, performance_score)[0, 1]
    # Calcula la correlación entre 'years_with_company' y 'performance_score' usando numpy
    correlation_y_ps = np.corrcoef(years_with_company, performance_score)[0, 1]

    # Muestra el DataFrame con la cantidad de registros
    print(record_counts_df)
    print(score_statistics)
    print(salary_statistics)
    print(correlation_s_ps)
    print(correlation_y_ps)

data_analisis(data)
