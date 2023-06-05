from passlib.hash import bcrypt
from tkinter import *
from tkinter import messagebox
from dat import Login,Database

log_in = Login()
ps = Database()
def login():
    # Retrieve username and password from entry fields
    username = entry_username.get()
    password = entry_password.get()

    for row in log_in.fetch(username):
        # print(row[0])
        if row:
            hashed_password_from_db = row
            # Verify if the entered password matches the stored hashed password
            if bcrypt.verify(password, hashed_password_from_db):
                # Passwords match, login successful
                
                
                from tkinter import ttk
                import tkinter as tk
                from tkinter import messagebox
                from dat import Database

                # Create window object
                app = Tk()
                app.configure(bg="black",highlightthickness=7,highlightcolor="PowderBlue")
                screen_width = app.winfo_screenwidth()
                scree_height= app .winfo_screenheight()

                frame =Frame(app,width=screen_width-30,height=scree_height-40,bg="black")

                frame.grid(row=1,column=0)

                system_Name =Label(frame,padx=0, bd= 20,width=59, relief=RIDGE, text="KENYA VEHICLE REGISTRATION SYSTEM", fg= "PowderBlue", bg="black", font=("times new roman",30))
                system_Name.place(x=1,y=1)

                
                def populate_list():
                    tree.delete(*tree.get_children())
                    for row in ps.fetch():
                        tree.insert("",tk.END,value=row)    


                def add_item():
                    if number_plate.get() == '' or email.get() == '' or id.get() == '':
                        # messagebox.showerror('Required Fields', 'Please include all fields')
                        return
                    try:
                        ps.insert(number_plate.get().replace(' ', '').lower(), email.get(),id.get())
                    except:
                        messagebox.showerror('Already exist', 'The number plate already exist')
                    # parts_list.delete(0, END)
                    tree.delete(*tree.get_children())
                    tree.insert("",tk.END,(number_plate.get(), email.get(),id.get()))
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
                        email_entry.delete(0, END)
                        email_entry.insert(END, x[1])
                        id_entry.delete(0, END)
                        id_entry.insert(END, x[3])
                        print(x[0])
                        remove_btn = Button(frame, text='Remove Part', width=12, command=remove_item,bg="black",fg="blue")
                        # remove_btn.grid(row=3, column=1)
                        remove_btn.place(x=400, y=300)

                        update_btn = Button(frame, text='Update Part', width=12, command=update_item,bg="black",fg="blue")
                        # update_btn.grid(row=3, column=2)
                        update_btn.place(x=270, y=300)
                    except IndexError:
                        pass


                select_item.has_been_called =False
                # treeview
                tree = ttk.Treeview(frame, column=("c1", "c2", "c3","c4"), show='headings',height=10,selectmode='browse')
                style =ttk.Style(frame)
                style.theme_use("clam")
                style.configure("Treeview",background='black',foreground='PowderBlue',fieldbackground='black',font='bold')
                style.configure('Treeview.Heading', background="PowderBlue")

                tree.column("#1", width=300)
                tree.heading("#1",text="Number Plate")
                tree.column("#2", width=300)
                tree.heading("#2",text="email")
                tree.column("#3", width=200)
                tree.heading("#3",text="Date of registration")
                tree.column("#4", width=200)
                tree.heading("#4",text="Identification")
                tree.place(x=2,y=340)
                tree.bind('<<TreeviewSelect>>', select_item)


                #scroll in tree view
                hs = ttk.Scrollbar(frame,orient="vertical",command=tree.yview)
                # hs.place(x=270+100+100+180,y=300,height=100+20)

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
                    ps.update(number_plate.get(), email.get(),id.get(),x[0])
                    populate_list()

                def clear_text():
                    number_plate_entry.delete(0, END)
                    email_entry.delete(0, END)
                    id_entry.delete(0, END)

                # Numberplate
                number_plate = StringVar()
                part_label = Label(frame, text='NumberPlate', font=('bold', 14), pady=20,bg="black",fg="blue",)
                # part_label.grid(row=1, column=0, sticky=W)
                part_label.place(x=2, y=90)
                number_plate_entry = Entry(frame, textvariable=number_plate,bg="gray",width=30,foreground='brown',font='bold')
                # number_plate_entry.grid(row=1, column=1)
                number_plate_entry.place(x=130, y=115)

                # phone number
                email = StringVar()
                customer_label = Label(frame, text='Email', font=('bold', 14),bg="black",fg="blue")
                # customer_label.grid(row=1, column=2, sticky=W)
                customer_label.place(x=2, y=165)
                email_entry = Entry(frame, textvariable=email,bg="gray",width=30,foreground='white',font='bold')
                # email_entry.grid(row=1, column=3)
                email_entry .place(x=130, y=170)

                # Identification
                id = StringVar()
                retailer_label = Label(frame, text='Identification', font=('bold', 14),bg="black",fg="blue")
                # retailer_label.grid(row=2, column=0, sticky=W)
                retailer_label.place(x=2, y=225)

                id_entry = Entry(frame, textvariable=id,bg="gray",width=30,foreground='white',font='bold')
                # id_entry.grid(row=2, column=1)
                id_entry.place(x=130, y=232)


                # Buttons
                add_btn = Button(frame, text='Register', width=12, command=add_item,bg="black",fg="blue")
                # add_btn.grid(row=3, column=0, pady=20)
                add_btn.place(x=2, y=300)



                clear_btn = Button(frame, text='Clear Input', width=12, command=clear_text,bg="black",fg="blue")
                # clear_btn.grid(row=3, column=3)
                clear_btn.place(x=140, y=300)

                app.title('Car registration system')
                # app.attributes('-fullscreen', True)

                # app.geometry('865x600')
                window.destroy()
                # Populate data
                populate_list()

                # Start program
                app.mainloop()



                # messagebox.showinfo("Login", "Login successful!")
            else:
                # Passwords do not match
                messagebox.showerror("Login", "Incorrect password!")
        else:
            # Username not found
            messagebox.showerror("Login", "Username not found!")

        # Close the cursor and connection
        # cursor.close()
        # connection.close()

# Create the Tkinter window and components
window = Tk()

label_username = Label(window, text="Username:")
label_username.pack()
entry_username = Entry(window)
entry_username.pack()

label_password = Label(window, text="Password:")
label_password.pack()
entry_password = Entry(window, show="*")
entry_password.pack()

button_login = Button(window, text="Login", command=login)
button_login.pack()

window.mainloop()

# def register():
#     # Retrieve username and password from entry fields
#     username = entry_username.get()
#     password = entry_password.get()

#     # Hash the password
#     hashed_password = bcrypt.hash(password)

#     # Connect to the MySQL database
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="?00chin@",
#         database="mary"
#     )

#     # Insert the user information into the table
#     cursor = connection.cursor()
#     insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
#     values = (username, hashed_password)
#     cursor.execute(insert_query, values)
#     connection.commit()

#     # Close the cursor and connection
#     cursor.close()
#     connection.close()

#     messagebox.showinfo("Registration", "Registration successful!")

# # Create the Tkinter window and components for registration
# window = Tk()

# label_username = Label(window, text="Username:")
# label_username.pack()
# entry_username = Entry(window)
# entry_username.pack()

# label_password = Label(window, text="Password:")
# label_password.pack()
# entry_password = Entry(window, show="*")
# entry_password.pack()

# button_register = Button(window, text="Register", command=register)
# button_register.pack()

# window.mainloop()



