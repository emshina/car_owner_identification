import mysql.connector
class Database:#registration working
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',user='root',password='?00chin@',database='mary')
        self.cur = self.conn.cursor()
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM car_owner")
        rows = self.cur.fetchall()
        return rows

    def insert(self,Number_plate ,Phone_number, ID):
        self.cur.execute("INSERT INTO car_owner VALUES(%s,%s,%s)",(Number_plate ,Phone_number, ID))
        self.conn.commit() 

    def remove(self, Number_plate):
        self.cur.execute("DELETE FROM car_owner WHERE Number_plate = %s ",(Number_plate,))
        self.conn.commit()


    def update(self,Number_plate ,Phone_number, ID,count):
        self.cur.execute("UPDATE car_owner SET Number_plate =%s, Phone_number= %s, ID =%s,WHERE Number_plate = %s  ", (Number_plate, Phone_number, ID,count))
        self.conn.commit()  

    # def __del__(self):

        
    #     self.conn.close()     

class PoliceStaion:# police station side
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',user='root',password='?00chin@',database='mary')
        self.cur = self.conn.cursor()
        # self.cur.execute("CREATE TABLE IF NOT EXISTS pk(ID INTEGER PRIMARY KEY, part text, customer text,retailer text,price INTEGER)")
        self.conn.commit()#setup connection and quaries to create tables

    def fetch(self):
        self.cur.execute("SELECT * FROM Police_station")
        rows = self.cur.fetchall()
        return rows

    def insert(self, Number_plate, Charges, date_of, County,Sub_location,Police_satation):#tab 2 working
        self.cur.execute("INSERT INTO Police_station VALUES(%s,%s,%s,%s,%s,%s,NULL)",(Number_plate, Charges, date_of, County,Sub_location,Police_satation))
        self.conn.commit() 

    # def remove(self,ID):# tab one working
    #     self.cur.execute("DELETE FROM Police_station WHERE ID = %s",(ID,))
    #     self.conn.commit()
    def remove(self,ID,x):# tab one working
        self.cur.execute("DELETE FROM police_station WHERE Police_station = %s AND ID = %s",(x,ID))
        self.conn.commit()

    def update(self, Number_plate, Charges, date_of, County,Sub_location,Police_satation,ID):# tab 2 working
        self.cur.execute("UPDATE Police_station SET Number_plate =%s, Charges= %s, date_of =%s, County =%s,Sub_location=%s,Police_satation=%s WHERE ID =%s", (Number_plate, Charges, date_of, County,Sub_location,Police_satation, ID))
        self.conn.commit()  

    def details(self,id):# getting details in tab 1
        self.cur.execute("SELECT * FROM car_owner WHERE Number_plate="+id)
        rows = self.cur.fetchone()
        return rows

    def Remove(self,id):# the remove tab 3 working
        self.cur.execute("SELECT * FROM Police_station WHERE Number_plate="+id)
        rows = self.cur.fetchall()
        return rows

    def __del__(self):   
        self.conn.close()     

class Government:
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',user='root',password='?00chin@',database='mary')
        self.cur = self.conn.cursor()
        # self.cur.execute("CREATE TABLE IF NOT EXISTS pk(ID INTEGER PRIMARY KEY, part text, customer text,retailer text,price INTEGER)")
        self.conn.commit()#setup connection and quaries to create tables

    def fetch(self):
        self.cur.execute ('''SELECT car_owner.Number_plate,
                            police_station.Number_plate,
                            Police_station.charges,
                            Police_station.date_of,
                            Police_station.County,
                            Police_station.Sub_location,
                            Police_station.police_station
                            FROM car_owner 
                            LEFT JOIN
                            police_station ON 
                            car_owner.Number_plate=police_station.Number_plate
                            ''')
        rows = self.cur.fetchall()
        return rows


class records:
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',user='root',password='?00chin@',database='mary')
        self.cur = self.conn.cursor()
        # self.cur.execute("CREATE TABLE IF NOT EXISTS pk(ID INTEGER PRIMARY KEY, part text, customer text,retailer text,price INTEGER)")
        self.conn.commit()#setup connection and quaries to create tables

    def fetch(self):
        self.cur.execute("SELECT * FROM Police_station")
        rows = self.cur.fetchall()
        return rows
