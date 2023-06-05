import mysql.connector


class Login:
    
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',user='root',password='?00chin@',database='mary')
        self.cur = self.conn.cursor()
        self.conn.commit()
    def fetch(self,username):  
    #    cursor = connection.cursor()
        self.cur.execute("SELECT password FROM users WHERE username = %s",(username,))
        # cursor.execute(select_query, (username,))
        rows = self.cur.fetchone()
        return rows

class Database:#registration working
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',user='root',password='?00chin@',database='policestationa')
        self.cur = self.conn.cursor()
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM carownerapp_registration")
        rows = self.cur.fetchall()
        return rows

    def insert(self,Number_Plate ,email, ID_id):
        self.cur.execute("INSERT INTO carownerapp_registration(Number_Plate,email,ID_id) VALUES(%s,%s,%s)",(Number_Plate ,email, ID_id))
        self.conn.commit() 

    def remove(self, Number_Plate):
        self.cur.execute("DELETE FROM carownerapp_registration WHERE Number_plate = %s ",(Number_Plate,))
        self.conn.commit()


    def update(self,Number_Plate ,email, ID_id,Number_Plate_2):
        self.cur.execute("UPDATE carownerapp_registration SET Number_Plate =%s, email= %s, ID_id =%s WHERE Number_Plate = %s  ", (Number_Plate, email,ID_id,Number_Plate_2))
        self.conn.commit()  

    # def __del__(self):

        
    #     self.conn.close()     

class PoliceStaion:# police station side
    def __init__(self):
        self.conn =mysql.connector.connect(host='localhost',user='root',password='?00chin@',database='policestationa')
        self.cur = self.conn.cursor()
        # self.cur.execute("CREATE TABLE IF NOT EXISTS pk(ID INTEGER PRIMARY KEY, part text, customer text,retailer text,price INTEGER)")
        self.conn.commit()#setup connection and quaries to create tables

    def fetch(self,code):
        self.cur.execute("SELECT * FROM carownerapp_charges WHERE Police_station_code_id =%s",(code,))
        rows = self.cur.fetchall()
        return rows
    def police_station_name(self,code):
        self.cur.execute("SELECT station_name,Police_station_code FROM carownerapp_police_station WHERE POlice_station_code =%s",(code,))
        rows = self.cur.fetchall()
        return rows
        

    def insert(self, Number_plate, Charges,Police_station_code_id):#tab 2 working
        self.cur.execute("INSERT INTO carownerapp_charges(Number_Plate_id, Charges,Police_station_code_id) VALUES(%s,%s,%s)",(Number_plate, Charges,Police_station_code_id ))
        self.conn.commit() 
        # ALTER TABLE carownerapp_charges MODIFY COLUMN date DATETIME DEFAULT CURRENT_TIMESTAMP;
    # def remove(self,ID):# tab one working
    #     self.cur.execute("DELETE FROM Police_station WHERE ID = %s",(ID,))
    #     self.conn.commit()
    def remove(self,ID,police_code):# tab one working
        self.cur.execute("DELETE FROM carownerapp_charges WHERE Police_station_code_id = %s AND id = %s",(police_code,ID))
        self.conn.commit()

    # def update(self, Number_plate, Charges, date_of, County,Sub_location,Police_satation,ID):# tab 2 working
    #     self.cur.execute("UPDATE Police_station SET Number_plate =%s, Charges= %s, date_of =%s, County =%s,Sub_location=%s,Police_satation=%s WHERE ID =%s", (Number_plate, Charges, date_of, County,Sub_location,Police_satation, ID))
    #     self.conn.commit()  

    def details(self,id):# getting details in tab 1
        self.cur.execute("SELECT * FROM carownerapp_registration WHERE Number_plate="+id)
        rows = self.cur.fetchone()
        return rows

    # def Remove(self,id):# the remove tab 3 working
    #     self.cur.execute("SELECT * FROM Police_station WHERE Number_plate="+id)
    #     rows = self.cur.fetchall()
        # return rows

    # def __del__(self):   
    #     self.conn.close()     

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
