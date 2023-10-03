import pandas as pd

# Definir la fila a partir de la cual deseas comparar (por ejemplo, fila 5)
fila_inicio = 10

# Carga los dos archivos de Excel en DataFrames
df1 = pd.read_excel('REPORTE_FINAL_ACTUALIZACION.xlsx', skiprows=range(1, fila_inicio))
df2 = pd.read_excel('REPORTE_FIN_ACT.xlsx', skiprows=range(1, fila_inicio))

# Compara los DataFrames y obtén las diferencias
diferencias = df1.compare(df2)


# Muestra las diferencias
print(diferencias)

if not diferencias.empty:
    # Guarda las diferencias en un archivo de texto
    diferencias.to_csv('diferencias.txt', index=False, sep='\t')
    print("Se encontraron diferencias. Las diferencias se han guardado en 'diferencias.txt'.")
else:
    print("No se encontraron diferencias entre los archivos.")

