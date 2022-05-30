import os
import csv
import pyodbc
from datetime import datetime

conn = pyodbc.connect('DSN=GEOMOS;Trusted_Connection=yes;')
c = conn.cursor()
#date = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
date = datetime.now().strftime("%Y_%m_%d")
print(f"filename_{date}")

#dd2= input("Ingrese Dia: ")
#mm2= input("Ingrese Mes: ")
#nn2= input("Ingrese Año: ")

#test2= nn2+"-"+mm2+"-"+dd2
#select = ("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLES' AND TABLE_CATALOG='dbName'")# script SQL que se va a ejecutar
#select = ("SELECT * FROM INFORMATION_SCHEMA.TABLES")# script SQL que se va a ejecutar
#select = ("SELECT * FROM View_Results_6304")# script SQL que se va a ejecutar
#select = ("SELECT * FROM PointReportView")
#select = ("SELECT * FROM View_Results_6304 WHERE Epoch > (select dateadd(hour, -1, getdate()))")# script SQL que se va a ejecutar
#select = ("SELECT * FROM information_schema.columns WHERE table_name = 'View_Results_6304' ")# script SQL information_schema
#select = ("SELECT * FROM information_schema.columns WHERE table_name = 'PointReportView' ")
#select = ("SELECT * FROM PointReportView WHERE Time > (select dateadd(hour, -1, getdate())) and PointNo = 'P06ET2'   ")
select = ("SELECT top 17 ID, POINTno, Time, D, TargetEasting, TargetNorthing,TargetHeight, EastingDiff, NorthingDiff, HeightDiff FROM PointReportView order by id desc  ")

#c.execute(select,{'test2':test2})
c.execute(select)
print ("Consulta realizada")

print(c)
PATH_CUR  = os.getcwd()
#PATH_FILE= PATH_CUR+"\\prismas_new\\BASE.csv"
PATH_FILE= "z:\\prismas_new\\BASE_"+date+".csv"

#titulo= [['ID','POINTno','ProfileName','TIME','H','V','D','PPMType','PPM','Pressure','Temperature','AddConst','TargetEasting','TargetNorthing','TargetHeight','ReflectorHeight','InstrumentHeight','StationEasting','StationNorthing','StationHeight','NullMeasurement','DiffFromNullMeas','ShortTimeDiff','LongTimeDiff','VelLimitDiff','DistProfileDirect','HorzDistance','DifferenceOutlier','State','TransverseDisplace','TargetPT','CUSTOMTEXT','ANALIZER','TYPE','EASTINGDIFF','NORHTDIFF','HEIGHTDIFF']]
titulo= [['id','POINTno','TIME','D','TargetEasting','TargetNorthing','TargetHeight','EASTINGDIFF','NORHTDIFF','HEIGHTDIFF']]


myFile = open(PATH_FILE, 'a',newline='')

with myFile:
    writer = csv.writer(myFile, delimiter=';') 
#    writer.writerows(titulo)
    writer.writerows(c)
conn.close()#cierra la conexion    
print("Datos Almacenados")




