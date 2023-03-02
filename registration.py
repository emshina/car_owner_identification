from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from dat import Database

# Create window object
app = Tk()
app.configure(bg="black",highlightthickness=7,highlightcolor="PowderBlue")

frame =Frame(app,width=850,height=500,bg="black")
frame.grid(row=1,column=0)

system_Name =Label(frame,padx=0, bd= 20,width=37, relief=RIDGE, text="KENYA VEHICLE REGISTRATION SYSTEM", fg= "PowderBlue", bg="black", font=("times new roman",30))
system_Name.place(x=1,y=1)

ps = Database()
def populate_list():
    tree.delete(*tree.get_children())
    for row in ps.fetch():
        tree.insert("",tk.END,value=row)    


def add_item():
    if number_plate.get() == '' or phone_number.get() == '' or id.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    try:
        ps.insert(number_plate.get(), phone_number.get(),id.get())
    except:
        messagebox.showerror('Already exist', 'The number plate already exist')
    # parts_list.delete(0, END)
    tree.delete(*tree.get_children())
    tree.insert("",tk.END,(number_plate.get(), phone_number.get(),id.get()))
    clear_text()
    populate_list()

def select_item(event):
    select_item.has_been_called= True
    try:
        global x
        index = tree.selection()[0]
        x = tree.item(index)['values']
        # selected_item = tree.get(index)
        print(index)

        number_plate_entry.delete(0, END)
        number_plate_entry.insert(END, x[0])
        phone_number_entry.delete(0, END)
        phone_number_entry.insert(END, x[1])
        id_entry.delete(0, END)
        id_entry.insert(END, x[2])
        print(x[0])
    except IndexError:
        pass


select_item.has_been_called =False
# treeview
tree = ttk.Treeview(frame, column=("c1", "c2", "c3"), show='headings',height=5,selectmode='browse')
style =ttk.Style(frame)
style.theme_use("clam")
style.configure("Treeview",background='black',foreground='PowderBlue',fieldbackground='black',font='bold')
style.configure('Treeview.Heading', background="PowderBlue")

tree.column("#1", width=160)
tree.heading("#1",text="Number Plate")
tree.column("#2", width=160)
tree.heading("#2",text="Phone Number")
tree.column("#3", width=160)
tree.heading("#3",text="Identification")
tree.place(x=4,y=300)
tree.bind('<<TreeviewSelect>>', select_item)


#scroll in tree view
hs = ttk.Scrollbar(frame,orient="vertical",command=tree.yview)
hs.place(x=300+100+100,y=300,height=100+20)

# hs.configure(command=tree.yview)
tree.configure(yscrollcommand=hs.set)


def remove_item():
    if select_item.has_been_called:
        try:
            ps.remove(x[0])
            clear_text()
            populate_list()
        except:
            messagebox.showerror('Has charges', 'The number plate has committed crimes')
    else:
        messagebox.showerror('Select item', 'select the numberplate to remove')

def update_item():
    ps.update(number_plate.get(), phone_number.get(),id.get(),x[0])
    populate_list()

def clear_text():
    number_plate_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    id_entry.delete(0, END)

# Numberplate
number_plate = StringVar()
part_label = Label(frame, text='NumberPlate', font=('bold', 14), pady=20,bg="black",fg="blue")
# part_label.grid(row=1, column=0, sticky=W)
part_label.place(x=2, y=90)
number_plate_entry = Entry(frame, textvariable=number_plate,bg="gray",width=30)
# number_plate_entry.grid(row=1, column=1)
number_plate_entry.place(x=130, y=115)

# phone number
phone_number = StringVar()
customer_label = Label(frame, text='PhoneNUmber', font=('bold', 14),bg="black",fg="blue")
# customer_label.grid(row=1, column=2, sticky=W)
customer_label.place(x=400, y=110)
phone_number_entry = Entry(frame, textvariable=phone_number,bg="gray",width=30)
# phone_number_entry.grid(row=1, column=3)
phone_number_entry .place(x=550, y=114)

# Identification
id = StringVar()
retailer_label = Label(frame, text='Identification', font=('bold', 14),bg="black",fg="blue")
# retailer_label.grid(row=2, column=0, sticky=W)
retailer_label.place(x=2, y=185)

id_entry = Entry(frame, textvariable=id,bg="gray",width=30)
# id_entry.grid(row=2, column=1)
id_entry.place(x=130, y=192)


# Buttons
add_btn = Button(frame, text='Register', width=12, command=add_item,bg="black",fg="blue")
# add_btn.grid(row=3, column=0, pady=20)
add_btn.place(x=2, y=250)

remove_btn = Button(frame, text='Remove Part', width=12, command=remove_item,bg="black",fg="blue")
# remove_btn.grid(row=3, column=1)
remove_btn.place(x=140, y=250)

update_btn = Button(frame, text='Update Part', width=12, command=update_item,bg="black",fg="blue")
# update_btn.grid(row=3, column=2)
update_btn.place(x=270, y=250)

clear_btn = Button(frame, text='Clear Input', width=12, command=clear_text,bg="black",fg="blue")
# clear_btn.grid(row=3, column=3)
clear_btn.place(x=400, y=250)

app.title('Car registration system')
app.geometry('865x600')

# Populate data
populate_list()

# Start program
app.mainloop()

