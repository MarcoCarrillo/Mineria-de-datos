#AGRUPAR COLUMNAS
# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

#Group by 
# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/user_modify.csv')
df1 = pd.read_csv('mineriadatos/user_modify.csv')
df2 = pd.read_csv('mineriadatos/user_modify.csv')
df3 = pd.read_csv('mineriadatos/user_modify.csv')

#Tabla 1
df = df[['first_name', 'country', 'company']]
#Agrupar
group = df.groupby(['first_name', 'country', 'company'])
print('Tabla 1')
print(group.size().reset_index(name='counts')) 

#Tabla 2
df1 = df1[['role', 'country']]
#Agrupar
group1 = df1.groupby(['role', 'country'])
print('Tabla 2')
print(group1.size().reset_index(name='counts')) 

#Tabla 3
df2 = df2[['lenguage', 'gender']]
#Agrupar
group2 = df2.groupby(['lenguage', 'gender'])
print('Tabla 3')
print(group2.size().reset_index(name='counts')) 

#Tabla 4
df3 = df3[['company', 'role']]
#Agrupar
group3 = df3.groupby(['company', 'role'])
print('Tabla 4')
print(group3.size().reset_index(name='counts')) 