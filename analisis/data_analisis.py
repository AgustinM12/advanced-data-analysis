import numpy as np
import pandas as pd

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def calculate_statistics(self):
        # ! Selecciona los campos y los agrupa por departamento
        grouped_by_department_score = self.df.groupby("department")["performance_score"]
        grouped_by_department_salary = self.df.groupby("department")["salary"]

        # ! Calcula las estadísticas necesarias de salario y score
        score_statistics = grouped_by_department_score.agg(["mean", "median", "std"])
        salary_statistics = grouped_by_department_salary.agg(["mean", "median", "std"])

        # ! Renombra las columnas para mayor claridad
        score_statistics.columns = ["Media", "Mediana", "Desviación Estándar"]
        salary_statistics.columns = ["Media", "Mediana", "Desviación Estándar"]

        return score_statistics, salary_statistics

    def record_counts(self):
        # ! Agrupa los datos y cuenta la cantidad de registros
        departments = self.df["department"].values
        unique_departments, counts = np.unique(departments, return_counts=True)

        # ! Crea un DataFrame con los resultados anteriores
        record_counts_df = pd.DataFrame({"department": unique_departments, "Cantidad de Registros": counts})

        return record_counts_df

    def calculate_correlations(self):
        # ! Extrae los datos necesarios
        years_with_company = self.df["years_with_company"].values
        performance_score = self.df["performance_score"].values
        salary = self.df["salary"].values

        # ! Calcula la correlación entre 'salary' y 'performance_score' 
        correlation_s_ps = np.corrcoef(salary, performance_score)[0, 1]

        # ! Calcula la correlación entre 'years_with_company' y 'performance_score' 
        correlation_y_ps = np.corrcoef(years_with_company, performance_score)[0, 1]

        return correlation_s_ps, correlation_y_ps

    def analyze(self):
        score_statistics, salary_statistics = self.calculate_statistics()
        record_counts_df = self.record_counts()
        correlation_s_ps, correlation_y_ps = self.calculate_correlations()

        return {
            "record_counts_df": record_counts_df,
            "score_statistics": score_statistics,
            "salary_statistics": salary_statistics,
            "correlation_s_ps": correlation_s_ps,
            "correlation_y_ps": correlation_y_ps,
        }
