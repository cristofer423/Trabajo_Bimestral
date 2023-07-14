#para usar las funciones primero se debe hacer el archivo csv e importarlo con pandas
import pandas as pd

def cargar_datos(archivo_csv):
    data = pd.read_csv(archivo_csv)
    return data

def calcular_altura_promedio(data):
    altura_promedio = data['Altura (m)'].mean()
    return altura_promedio

def calcular_altura_mediana(data):
    altura_mediana = data['Altura (m)'].median()
    return altura_mediana

def calcular_desviacion_estandar(data):
    desviacion_estandar = data['Altura (m)'].std()
    return desviacion_estandar
