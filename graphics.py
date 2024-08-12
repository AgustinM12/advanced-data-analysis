import matplotlib.pyplot as plt

def graphic_data1(df):
    # Crear el gráfico de dispersión de salary vs performance_score
    plt.figure(figsize=(10, 6))
    plt.scatter(df['performance_score'], df['salary'], color='b', alpha=0.7)

    # Añadir títulos y etiquetas
    plt.title('Salario vs. Puntuación de Rendimiento')
    plt.xlabel('Puntuación de Rendimiento')
    plt.ylabel('Salario')

    # Mostrar el gráfico
    plt.show()

def graphic_data2(df):
    # Crear el gráfico de dispersión de years_with_company vs. performance_score.
    plt.figure(figsize=(10, 6))
    plt.scatter(df['performance_score'], df['years_with_company'], color='r', alpha=0.7)

    # Añadir títulos y etiquetas
    plt.title('Salario vs. Puntuación de Rendimiento')
    plt.xlabel('Puntuación de Rendimiento')
    plt.ylabel('Salario')

    # Mostrar el gráfico
    plt.show()

def graphic_data3(df):
    departments = df['department'].unique()
    # Crear subplots
    fig, axs = plt.subplots(len(departments), figsize=(10, 20))

    # Generar un histograma para cada departamento
    for ax, department in zip(axs, departments):
        department_data = df[df['department'] == department]
        ax.hist(department_data['performance_score'], bins=10, alpha=0.7, color='b')
        ax.set_title(f'Histograma de Puntuación de Rendimiento para {department}')
        ax.set_xlabel('Puntuación de Rendimiento')
        ax.set_ylabel('Frecuencia')

    # Ajustar el layout
    plt.tight_layout()
    plt.show()