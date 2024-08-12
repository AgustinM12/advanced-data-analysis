import numpy as np
import pandas as pd

def data_analisis(df):
    # Selecciona los campos y los agrupa por departamento
    grouped_by_department_score = df.groupby("department")["performance_score"]
    grouped_by_department_salary = df.groupby("department")["salary"]

    # # Calcula las estadísticas necesarias de salario y score
    score_statistics = grouped_by_department_score.agg(["mean", "median", "std"])
    salary_statistics = grouped_by_department_salary.agg(["mean", "median", "std"])

    # Renombra las columnas para mayor claridad
    score_statistics.columns = ["Media", "Mediana", "Desviación Estándar"]
    salary_statistics.columns = ["Media", "Mediana", "Desviación Estándar"]

    # Agrupa los datos y cuenta la cantidad de registros
    departments = df["department"].values
    years_with_company = df["years_with_company"].values
    performance_score = df["performance_score"].values
    salary = df["salary"].values

    # Consigue los nombres de los departamentos y la cantidad de cada uno
    unique_departments, counts = np.unique(departments, return_counts=True)

    # Crea un DataFrame con los resultados anteriores
    record_counts_df = pd.DataFrame(
        {"department": unique_departments, "Cantidad de Registros": counts}
    )

    # Calcula la correlación entre 'salary' y 'performance_score' usando numpy
    correlation_s_ps = np.corrcoef(salary, performance_score)[0, 1]

    # Calcula la correlación entre 'years_with_company' y 'performance_score' usando numpy
    correlation_y_ps = np.corrcoef(years_with_company, performance_score)[0, 1]

    # Muestra el analisis de los datos.
    return {
        "record_counts_df": record_counts_df,
        "score_statistics": score_statistics,
        "salary_statistics": salary_statistics,
        "correlation_s_ps": correlation_s_ps,
        "correlation_y_ps": correlation_y_ps,
    }
