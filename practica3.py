# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/usuarios_incompleto.csv')

# Dimension del dataset/ dataframe
print(df.shape)

col_names =df.columns.tolist()
#print(col_names)

# Nombre de tipo o dictado de columna
print(df.dtypes)

# Conocer la cantidad de datos faltantes por cada columna
print(df.count())

# Conocer si hay datos duplicados
print(df.duplicated().sum())

# Iterar sobre la listas
for column in col_names :
    # Conocer valores nulos
    print( "Valores nulos en  <"+ column + ">: "  + str (df[column].isnull().sum()))

# Llenar columnas
df['company'] = df['company'].fillna('unknown')
df['car'] = df['car'].fillna('unknown')
df['favorite_app'] = df['favorite_app'].fillna('unknown')
df['avatar'] = df['avatar'].fillna('default.png')
df['active'] = df['active'].fillna('undefined')
df['is_admin'] = df['is_admin'].fillna('False')
df['department'] = df['department'].fillna('undefined')
df['gender'] = df['gender'].fillna('U')

#df.to_csv('mineriadatos/usuarios_completo.csv', index=False)

#Comprobacion
df_completo = df = pd.read_csv('mineriadatos/usuarios_completo.csv')
# Conocer la cantidad de datos faltantes por cada columna
print(df.count())

#df_completo_gender = df['gender'].value_counts().plot(kind='bar',  color = 'red')
df_completo_company = df['active'].value_counts().plot()

plt.show()

