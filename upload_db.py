import psycopg2 # Libreria para comunicarse con Postgres
import pandas as pd
from datetime import datetime
import os
import numpy as np

def guardarLectura(datos):
       
        
	try:
		conn = psycopg2.connect(user="gis",password="Emt.532%",host="10.10.10.18",port="5431",database="TEM")
		cursor = conn.cursor()

		consulta = "INSERT INTO registro_prisma(prisma_id,fecha,norte,este,cota,distancia,nortediff,estediff,cotadiff) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
		cursor.execute(consulta,(datos[0], datos[1], datos[3],datos[4],datos[5],datos[2],datos[6],datos[7],datos[8],))

		conn.commit()
		conn.close()
		cursor.close()
    
		print("Lectura con fecha: "+ str(datos[1]) +" le prisma: "+ str(datos[0]) +" con formato correcto!")

	except:
		print("Error en guardar lectura en la Base de datos...")

date = datetime.now().strftime("%Y_%m_%d")
#print(date)
path_new_data = (r"C:/Users/pablo/Downloads/BASE_2022_05_25.csv")
#path_new_data = (r'X:/prismas_new/BASE_'+date+'.csv')

data_todo = pd.read_csv(path_new_data)
prismas_list = data_todo.tail(30)
#print(prismas_list)
prismas_listado = prismas_list.values.tolist()
con = psycopg2.connect(user="gis",password="Emt.532%",host="10.10.10.18",port="5431",database="TEM")
cursor = con.cursor()
query = "SELECT gid, prisma_codigo FROM prisma"
cursor.execute(query)
ids = cursor.fetchall()
#print(ids)
for raw in prismas_listado:
    prismas_list = prismas_listado.pop(1)
    prisma = prismas_list[0].split(';')
    HeightDiff = prisma[9]
    NorthingDiff = prisma[8]
    EastingDiff = prisma[7]
    Height = prisma[6]
    Northing = prisma[5]
    Easting = prisma[4]
    dist = prisma[3]
    fecha  = prisma[2]
    prisma = prisma[1]
    
    for row in ids:
        if prisma in row[1]:
            datos = [row[0],fecha,dist,Easting,Northing,Height,EastingDiff,NorthingDiff,HeightDiff]
            guardarLectura(datos)

           
  

           

         


      

 