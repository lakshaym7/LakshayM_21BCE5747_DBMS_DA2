#backend
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',
                            passwd='2418032716',
                            database='VehicleManagementSystem')

mycursor=con.cursor()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS vehicle(
VehicleID VARCHAR(255),Manufacturer VARCHAR(255),
Model VARCHAR(255),Year VARCHAR(255),
Type VARCHAR(255),Mileage VARCHAR(255),
EngineCapacity VARCHAR(255),Availability VARCHAR(255))""")

con.commit()

def AddVehicleRec(VehicleID,Manufacturer,Model,Year,Type,Mileage,EngineCapacity,Availability):
    cur=con.cursor()
    cur.execute("INSERT INTO vehicle VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (VehicleID,Manufacturer,Model,Year,Type,Mileage,EngineCapacity,Availability))
    con.commit()
    con.close()

def ViewVehicleData():
    cur=con.cursor()
    cur.execute("SELECT * FROM vehicle")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteVehicleRec(ID):    
    cur=con.cursor()
    cur.execute("DELETE FROM vehicle WHERE VehicleID=%s", (ID,))
    con.commit()
    con.close()  

def SearchVehicleData(VehicleID="",Manufacturer="",Model="",Year="",Type="",Mileage="",EngineCapacity="",Availability=""):  
    cur=con.cursor()
    cur.execute("SELECT * FROM vehicle WHERE VehicleID=%s OR Manufacturer=%s OR Model=%s OR Year=%s OR Type=%s OR Mileage=%s OR EngineCapacity=%s OR Availability=%s",
                (VehicleID,Manufacturer,Model,Year,Type,Mileage,EngineCapacity,Availability))
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateVehicleData(VehicleID="",Manufacturer="",Model="",Year="",Type="",Mileage="",EngineCapacity="",Availability=""):
    cur=con.cursor()
    cur.execute("UPDATE vehicle SET VehicleID=%s,Manufacturer=%s,Model=%s,Year=%s,Type=%s,Mileage=%s,EngineCapacity=%s,Availability=%s, WHERE id=%s",
                (VehicleID,Manufacturer,Model,Year,Type,Mileage,EngineCapacity,Availability))
    con.commit()
    con.close()
