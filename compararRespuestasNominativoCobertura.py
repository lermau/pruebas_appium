import pandas as pd

fila_inicio = 8
# Carga los dos archivos de Excel en DataFrames
df1 = pd.read_excel('REPORTE_FINAL_ACTUALIZACION.xlsx', skiprows=range(1, fila_inicio))
df2 = pd.read_excel('REPORTE_FIN_ACT.xlsx', skiprows=range(1, fila_inicio))

# Compara los DataFrames y obtén las diferencias
diferencias = df1.compare(df2)

# Muestra las diferencias
print(diferencias)

diferencias2 = df1 != df2
num_diferencias = diferencias2.sum().sum()

if not diferencias.empty:
    # Guarda las diferencias en un archivo de texto
    diferencias.to_csv('diferencias.txt', index=False, sep='\t')
    print(f"\nSe encontraron {num_diferencias} diferencias. \nLas diferencias se han guardado en 'diferencias.txt'.")
else:
    print("No se encontraron diferencias entre los archivos.")

