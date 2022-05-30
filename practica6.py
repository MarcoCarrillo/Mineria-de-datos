# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

#crosstab 
# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/usuarios_completo.csv')


# #Grafica 1
# df = df[['gender', 'department']]
# print(df.head(6))

# ct = pd.crosstab(df['gender'],df['department']).plot(kind='bar')
# plt.legend(title = "Departamento") 
# plt.title("Grafica 1. Cruce de Genero y Departamento")
# plt.xlabel("Genero")
# plt.show()

# #Grafica 2
# df = df[['gender', 'active']]
# print(df.head(6))

# ct = pd.crosstab(df['gender'],df['active']).plot(kind='bar')
# plt.legend(title = "Es activo") 
# plt.title("Grafica 2. Cruce de Genero y Es activo")
# plt.xlabel("Genero")
# plt.show()

#Grafica 3
# df = df[['is_admin', 'department']]
# print(df.head(6))

# ct = pd.crosstab(df['is_admin'],df['department']).plot(kind='bar')
# plt.legend(title = "Departamento") 
# plt.title("Grafica 3. Cruce de Usuario administrador y Departamento")
# plt.xlabel("Es administrador")
# plt.show()

#Grafica 4
df = df[['gender', 'is_admin']]
print(df.head(6))
print(len(df['is_admin']))
print(df['gender'][0])

ct = pd.crosstab(df['gender'],df['is_admin']).plot(kind='bar')
for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')


plt.legend(title = "Es administrador") 
plt.title("Grafica 4. Cruce de Genero y Usuario administrador")
plt.xlabel("Genero")

plt.savefig("img/Grafica5.png")
plt.show()