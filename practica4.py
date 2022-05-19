# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

#Group by 
# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/user_modify.csv')

df = df[['gender', 'role']]
#print(df.head(6))

#Agrupar gender y role del dataframe
group = df.groupby(['gender', 'role'])
print(group.size().reset_index(name='counts')) 
