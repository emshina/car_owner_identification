import csv
from tkinter import RIDGE, Button, Frame, Label, Scrollbar, ttk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
from dat import records
rec = records()

root = tk.Tk()
root.configure(highlightthickness=7,highlightcolor='PowderBlue',highlightbackground='gray',bg='black')
root.geometry('800x500')
root.resizable(False,False)
frame =Frame(root,width=785,height=450,bg="black")
frame.grid(row=1,column=0)
system_Name =Label(frame,padx=0, bd= 20,width=34, relief=RIDGE, text="KENYA CHARGES RECORDS SYSTEM", fg= "PowderBlue", bg="black", font=("times new roman",30))
system_Name.place(x=1,y=1)

    
def populate_list():
    tree.delete(*tree.get_children())
    for row in rec.fetch():
        tree.insert("",tk.END,value=row)    
      
def excel(result):
    with open('customer.csv', 'a') as f:
        w= csv.writer(f, dialect='excel')
        
        for records in result:
            w.writerow(records)
            
            messagebox.showerror('Saved', 'The record have been saved successfully')                
# save button
but = Button(frame,text="save to excel", command=lambda:excel(result),bg="black",fg="PowderBlue",bd=6,width=12,font='bold')
but.place(x=170,y=100)

con1 =mysql.connector.connect(host='localhost',user='root',password='?00chin@',database='mary')
cur1 = con1.cursor()
cur1.execute("SELECT * FROM Police_station")  
result =cur1.fetchall()

# treeview
tree = ttk.Treeview(frame, column=("c1", "c2", "c3","c4", "c5", "c6"), show='headings',height=11)
style =ttk.Style(frame)
style.theme_use("clam")
style.configure("Treeview",background='black',foreground='PowderBlue',fieldbackground='black',font='bold')
style.configure('Treeview.Heading', background="PowderBlue")
tree.column("#1", width=100)
tree.heading("#1",text="Number Plate")
tree.column("#2", width=100)
tree.heading("#2",text="Phone Number")
tree.column("#3", width=100)
tree.heading("#3",text="DATE")
tree.column("#4", width=100)
tree.heading("#4",text=" COUNTY")
tree.column("#5", width=100)
tree.heading("#5",text="SUB COUNTY")
tree.column("#6", width=100)
tree.heading("#6",text="POLICESTATION")
tree.place(x=1,y=147)

#scroll in tree view
hs = ttk.Scrollbar(frame,orient="vertical",command=tree.yview)
hs.place(x=300+200+107,y=149,height=150+100)
tree.configure(yscrollcommand=hs.set)


button1 = tk.Button(frame,text="Display data", command=populate_list,bg="black",fg="PowderBlue",bd=7,width=12,font='bold')
button1.place(x=1,y=100)

root.mainloop()
