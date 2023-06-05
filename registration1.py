from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from dat import Database

ps = Database()
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Car registration system')
        master.geometry('865x600')
        master.configure(bg="black",highlightthickness=7,highlightcolor="PowderBlue") 
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()
        
    def create_widgets(self):
        self.frame =Frame(self.master,width=850,height=500,bg="black")
        self.frame.grid(row=1,column=0)
        self.system_Name =Label(self.frame,padx=0, bd= 20,width=37, relief=RIDGE, text="KENYA VEHICLE REGISTRATION SYSTEM", fg= "PowderBlue", bg="black", font=("times new roman",30))
        self.system_Name.place(x=1,y=1)
                
        # Numberplate
        self.number_plate = StringVar()
        self.part_label = Label(self.frame, text='NumberPlate', font=('bold', 14), pady=20,bg="black",fg="blue")
        # part_label.grid(row=1, column=0, sticky=W)
        self.part_label.place(x=2, y=90)
        self.number_plate_entry = Entry(self.frame, textvariable=self.number_plate,bg="gray",width=30)
        # number_plate_entry.grid(row=1, column=1)
        self.number_plate_entry.place(x=130, y=115)
        # phone number
        self.phone_number = StringVar()
        self.customer_label = Label(self.frame, text='PhoneNUmber', font=('bold', 14),bg="black",fg="blue")
        # customer_label.grid(row=1, column=2, sticky=W)
        self.customer_label.place(x=400, y=110)
        self.phone_number_entry = Entry(self.frame, textvariable=self.phone_number,bg="gray",width=30)
        # phone_number_entry.grid(row=1, column=3)
        self.phone_number_entry .place(x=550, y=114)

        # Identification
        self.id = StringVar()
        self.retailer_label = Label(self.frame, text='Identification', font=('bold', 14),bg="black",fg="blue")
        # retailer_label.grid(row=2, column=0, sticky=W)
        self.retailer_label.place(x=2, y=185)

        self.id_entry = Entry(self.frame, textvariable=self.id,bg="gray",width=30)
        # id_entry.grid(row=2, column=1)
        self.id_entry.place(x=130, y=192)


        # Buttons
        self.add_btn = Button(self.frame, text='Register', width=12, command=self.add_item,bg="black",fg="blue")
        # add_btn.grid(row=3, column=0, pady=20)
        self.add_btn.place(x=2, y=250)

        self.remove_btn = Button(self.frame, text='Remove Part', width=12, command=self.remove_item,bg="black",fg="blue")
        # remove_btn.grid(row=3, column=1)
        self.remove_btn.place(x=140, y=250)

        self.update_btn = Button(self.frame, text='Update Part', width=12, command=self.update_item,bg="black",fg="blue")
        # update_btn.grid(row=3, column=2)
        self.update_btn.place(x=270, y=250)
        
        self.clear_btn = Button(self.frame, text='Clear Input', width=12, command=self.clear_text,bg="black",fg="blue")
        # clear_btn.grid(row=3, column=3)
        self.clear_btn.place(x=400, y=250)
        # treeview
        self.tree = ttk.Treeview(self.frame, column=("c1", "c2", "c3"), show='headings',height=5,selectmode='browse')
        self.style =ttk.Style(self.frame)
        self.style.theme_use("clam")
        self.style.configure("Treeview",background='black',foreground='PowderBlue',fieldbackground='black',font='bold')
        self.style.configure('Treeview.Heading', background="PowderBlue")

        self.tree.column("#1", width=160)
        self.tree.heading("#1",text="Number Plate")
        self.tree.column("#2", width=160)
        self.tree.heading("#2",text="Phone Number")
        self.tree.column("#3", width=160)
        self.tree.heading("#3",text="Identification")
        self.tree.place(x=4,y=300)
        self.tree.bind('<<TreeviewSelect>>', self.select_item)
                
        #scroll in tree view
        self.hs = ttk.Scrollbar(self.frame,orient="vertical",command=self.tree.yview)
        self.hs.place(x=300+100+100,y=300,height=100+20)

        # hs.configure(command=tree.yview)
        self.tree.configure(yscrollcommand=self.hs.set)
        # self.select_item.has_been_called =False

    def populate_list(self):
        self.tree.delete(self.*ttk.Treeview.get_children())
        for row in ps.fetch():
            self.tree.insert("",tk.END,value=row)    


    def add_item(self):
        if self.number_plate.get() == '' or self.phone_number.get() == '' or self.id.get() == '':
            messagebox.showerror('Required Fields', 'Please include all fields')
            return
        try:
            self.ps.insert(self.number_plate.get(), self.phone_number.get(),self.id.get())
        except:
            messagebox.showerror('Already exist', 'The number plate already exist')
        # parts_list.delete(0, END)
        self.tree.delete(*ttk.Treeview.get_children())
        self.tree.insert("",tk.END,(self.number_plate.get(), self.phone_number.get(),self.id.get()))
        self.clear_text()
        self.populate_list()
        
    def remove_item(self):
        if self.select_item.has_been_called:
            try:
                self.ps.remove(x[0])
                self.clear_text()
                self.populate_list()
            except:
                messagebox.showerror('Has charges', 'The number plate has committed crimes')
        else:
            messagebox.showerror('Select item', 'select the numberplate to remove')

    def update_item(self):
        self.ps.update(self.number_plate.get(), self.phone_number.get(),self.id.get(),self.x[0])
        self.populate_list()

    def clear_text(self):
        self.number_plate_entry.delete(0, END)
        self.phone_number_entry.delete(0, END)
        self.id_entry.delete(0, END)


    def select_item(self,event):
        self.select_item.has_been_called= True
        try:
            global x
            self.index = self.tree.selection()[0]
            self.x = self.tree.item(self.index)['values']
            # selected_item = tree.get(index)
            print(self.index)

            self.number_plate_entry.delete(0, END)
            self.number_plate_entry.insert(END, x[0])
            self.phone_number_entry.delete(0, END)
            self.phone_number_entry.insert(END, x[1])
            self.id_entry.delete(0, END)
            self.id_entry.insert(END, x[2])
            print(x[0])
        except IndexError:
            pass
root = tk.Tk()
app = Application(master=root)
app.mainloop()