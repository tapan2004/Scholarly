import tkinter as tk
from tkinter import Button, Entry, Label, ttk
from tkinter import messagebox, Frame, CENTER
from pymongo import MongoClient

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Student Details")
        self.root.geometry("1280x500+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ===
        title = tk.Label(
            self.root, text="Manage Student Details",
            font=("goudy old style", 20, "bold"), bg="#033054", fg="white"
        )
        title.place(x=10, y=15, width=1640, height=35)

        # === Variables ===
        self.var_roll = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_contact = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_a_date = tk.StringVar()
        self.var_state = tk.StringVar()
        self.var_city = tk.StringVar()
        self.var_pin = tk.StringVar()
        self.var_search = tk.StringVar()

        # === Widgets ===
        # === Column 1 ===
        lbl_roll = tk.Label(
            self.root, text="Roll Number", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_roll.place(x=10, y=60)

        lbl_name = tk.Label(
            self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_name.place(x=10, y=100)

        lbl_email = tk.Label(
            self.root, text="Email", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_email.place(x=10, y=140)

        lbl_gender = tk.Label(
            self.root, text="Gender", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_gender.place(x=10, y=180)

        lbl_state = tk.Label(
            self.root, text="State", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_state.place(x=10, y=220)
        txt_state = tk.Entry(
            self.root, textvariable=self.var_state, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        txt_state.place(x=150, y=220, width=150)

        lbl_city = tk.Label(
            self.root, text="City", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_city.place(x=320, y=220)
        txt_city = tk.Entry(
            self.root, textvariable=self.var_city, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        txt_city.place(x=380, y=220, width=100)

        lbl_pin = tk.Label(
            self.root, text="Pin", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_pin.place(x=500, y=220)
        txt_pin = tk.Entry(
            self.root, textvariable=self.var_pin, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        txt_pin.place(x=540, y=220, width=100)

        lbl_address = tk.Label(
            self.root, text="Address", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_address.place(x=10, y=260)

        # Address text box
        self.txt_address = tk.Text(
            self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow', wrap=tk.WORD
        )
        self.txt_address.place(x=150, y=270, width=540, height=100)

        # === Entry Fields ===
        self.txt_roll = tk.Entry(
            self.root, textvariable=self.var_roll, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        self.txt_roll.place(x=150, y=60, width=200)

        text_name = tk.Entry(
            self.root, textvariable=self.var_name, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        text_name.place(x=150, y=100, width=200)

        text_email = tk.Entry(
            self.root, textvariable=self.var_email, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        text_email.place(x=150, y=140, width=200)

        text_gender = ttk.Combobox(
            self.root, textvariable=self.var_gender, font=("goudy old style", 15, 'bold'),
            state='readonly', justify=CENTER
        )
        text_gender['values'] = ("Select", "Male", "Female", "Other")
        text_gender.place(x=150, y=180, width=200)
        text_gender.current(0)

        # === Column 2 ===
        lbl_dob = tk.Label(
            self.root, text="D.O.B", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_dob.place(x=370, y=60)

        lbl_contact = tk.Label(
            self.root, text="Contact", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_contact.place(x=370, y=100)

        lbl_admission = tk.Label(
            self.root, text="Admission", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_admission.place(x=370, y=140)

        lbl_course = tk.Label(
            self.root, text="Course", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_course.place(x=370, y=180)
        


        # === Entry Fields ===
        txt_dob = tk.Entry(
            self.root, textvariable=self.var_dob, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        txt_dob.place(x=480, y=60, width=200)

        text_contact = tk.Entry(
            self.root, textvariable=self.var_contact, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        text_contact.place(x=480, y=100, width=200)

        text_admission = tk.Entry(
            self.root, textvariable=self.var_a_date, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        text_admission.place(x=480, y=140, width=200)

        text_course = ttk.Combobox(
            self.root, textvariable=self.var_course, font=("goudy old style", 15, 'bold'),
            state='readonly', justify=CENTER
        )
        text_course['value'] = ("SELECT","CSE","ECE","IEE","BCA","MCA","SC","MSC","ARCHITURE","BBA","MBA","BA","MA","NURSING","LLB")
        text_course.place(x=480, y=180, width=200) 
        text_course.current(0)

        # === Buttons ===
        self.btn_add = tk.Button(
            self.root, text='Save', font=("goudy old style", 15, "bold"),
            bg="#2196f3", fg="white", cursor="hand2", command=self.save_student
        )
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = tk.Button(
            self.root, text='Update', font=("goudy old style", 15, "bold"),
            bg="#4caf50", fg="white", cursor="hand2", command=self.update_student
        )
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = tk.Button(
            self.root, text='Delete', font=("goudy old style", 15, "bold"),
            bg="#f44336", fg="white", cursor="hand2", command=self.delete_student
        )
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = tk.Button(
            self.root, text='Clear', font=("goudy old style", 15, "bold"),
            bg="#607d8b", fg="white", cursor="hand2", command=self.clear
        )
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # === Search ===

        lbl_search = Label(
            self.root, text="Search Roll Number", font=("goudy old style", 15, 'bold'), bg='white'
        )
        lbl_search.place(x=840, y=60)

        text_search = Entry(
            self.root,textvariable=self.var_search, font=("goudy old style", 15, 'bold'), bg='lightyellow'
        )
        text_search.place(x=1050, y=60, width=180)

        btn_search = Button(
            self.root, text='Search', font=("goudy old style", 15, "bold"),
            bg="#4caf50", fg="white", cursor="hand2", command=self.search
        )
        btn_search.place(x=1240, y=60, width=120, height=28)

        # === Content Frame ===
        self.c_frame = Frame(self.root, bd=2, relief=tk.RIDGE)
        self.c_frame.place(x=860, y=100, width=500, height=340)

        scrolly = tk.Scrollbar(self.c_frame, orient=tk.VERTICAL)
        scrollx = tk.Scrollbar(self.c_frame, orient=tk.HORIZONTAL)

        self.course_table = ttk.Treeview(
            self.c_frame, columns=("roll", "name", "email", "gender", "dob", "contact",
                                   "admission", "course", "state", "city", "pin", "address"),
            xscrollcommand=scrollx.set, yscrollcommand=scrolly.set
        )
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)

        self.course_table.heading("roll", text="Roll No")
        self.course_table.heading("name", text="Name")
        self.course_table.heading("email", text="Email")
        self.course_table.heading("gender", text="Gender")
        self.course_table.heading("dob", text="D.O.B")
        self.course_table.heading("contact", text="Contact")
        self.course_table.heading("admission", text="Admission")
        self.course_table.heading("course", text="Course")
        self.course_table.heading("state", text="State")
        self.course_table.heading("city", text="City")
        self.course_table.heading("pin", text="Pin")
        self.course_table.heading("address", text="Address")

        self.course_table["show"] = "headings"

        self.course_table.column("roll", width=90)
        self.course_table.column("name", width=150)
        self.course_table.column("email", width=150)
        self.course_table.column("gender", width=100)
        self.course_table.column("dob", width=100)
        self.course_table.column("contact", width=100)
        self.course_table.column("admission", width=100)
        self.course_table.column("course", width=100)
        self.course_table.column("state", width=100)
        self.course_table.column("city", width=100)
        self.course_table.column("pin", width=100)
        self.course_table.column("address", width=200)

        self.course_table.pack(fill=tk.BOTH, expand=1)
        self.course_table.bind("<ButtonRelease-1>", self.get_data)

        # === Database ===
        self.init_db()
        self.load_courses()

    def init_db(self):
        """ Initialize the MongoDB connection """
        try:
            self.client = MongoClient("mongodb+srv://sahapriyanshu88:ezyCplrNUtcKPuiH@cluster0.4qyhzir.mongodb.net/")
            self.db = self.client['rms']
            self.collection = self.db['coursetext_course']
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect to the database: {str(e)}")
            self.root.destroy()

    def save_student(self):
        """ Save student details to the database """
        if not self.validate_input():
            return

        if self.collection.find_one({"roll": self.var_roll.get()}):
            messagebox.showwarning("Duplicate Roll Number", "This roll number already exists.")
            return

        student_data = {
            "roll": self.var_roll.get(),
            "name": self.var_name.get(),
            "email": self.var_email.get(),
            "gender": self.var_gender.get(),
            "dob": self.var_dob.get(),
            "contact": self.var_contact.get(),
            "admission": self.var_a_date.get(),
            "course": self.var_course.get(),
            "state": self.var_state.get(),
            "city": self.var_city.get(),
            "pin": self.var_pin.get(),
            "address": self.txt_address.get("1.0", tk.END).strip()
        }
        self.collection.insert_one(student_data)
        messagebox.showinfo("Success", "Student details saved successfully!")
        self.clear()
        self.load_courses()

    def update_student(self):
        """ Update existing student details in the database """
        if not self.validate_input():
            return

        if not self.collection.find_one({"roll": self.var_roll.get()}):
            messagebox.showwarning("Invalid Roll Number", "No such roll number found.")
            return

        student_data = {
            "name": self.var_name.get(),
            "email": self.var_email.get(),
            "gender": self.var_gender.get(),
            "dob": self.var_dob.get(),
            "contact": self.var_contact.get(),
            "admission": self.var_a_date.get(),
            "course": self.var_course.get(),
            "state": self.var_state.get(),
            "city": self.var_city.get(),
            "pin": self.var_pin.get(),
            "address": self.txt_address.get("1.0", tk.END).strip()
        }

        self.collection.update_one({"roll": self.var_roll.get()}, {"$set": student_data})
        messagebox.showinfo("Success", "Student details updated successfully!")
        self.clear()
        self.load_courses()

    def delete_student(self):
        """ Delete a student from the database """
        if not self.var_roll.get():
            messagebox.showwarning("Validation Error", "Please enter roll number to delete.")
            return

        if not self.collection.find_one({"roll": self.var_roll.get()}):
            messagebox.showwarning("Invalid Roll Number", "No such roll number found.")
            return

        self.collection.delete_one({"roll": self.var_roll.get()})
        messagebox.showinfo("Success", "Student details deleted successfully!")
        self.clear()
        self.load_courses()

    def validate_input(self):
        """ Validate input fields """
        if not self.var_roll.get() or not self.var_name.get() or self.var_gender.get() == "Select":
            messagebox.showwarning("Validation Error", "Please fill all required fields.")
            return False
        return True

    def clear(self):
        """ Clear all input fields """
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_course.set("Select")
        self.var_a_date.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0", tk.END)
        self.var_search.set("")
        self.load_courses()

    def get_data(self, event):
        """ Get data from the selected row """
        item = self.course_table.item(self.course_table.focus())
        row = item['values']

        if row:
            self.var_roll.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_dob.set(row[4])
            self.var_contact.set(row[5])
            self.var_a_date.set(row[6])
            self.var_course.set(row[7])
            self.var_state.set(row[8])
            self.var_city.set(row[9])
            self.var_pin.set(row[10])
            self.txt_address.delete("1.0", tk.END)
            self.txt_address.insert(tk.END, row[11])

    def search(self):
        """ Search for a student by name """
        search_term = self.var_search.get()
        results= self.collection.find({"roll": {"$regex": search_term, "$options": "i"}})
        self.course_table.delete(*self.course_table.get_children())

        for result in results:
            self.course_table.insert('', tk.END, values=(
                result['roll'], result['name'], result['email'], result['gender'],
                result['dob'], result['contact'], result['admission'], result['course'],
                result['state'], result['city'], result['pin'], result['address']
            ))

    def load_courses(self):
        """ Load student details into the table """
        self.course_table.delete(*self.course_table.get_children())
        results = self.collection.find()

        for result in results:
            self.course_table.insert('', tk.END, values=(
                result['roll'], result['name'], result['email'], result['gender'],
                result['dob'], result['contact'], result['admission'], result['course'],
                result['state'], result['city'], result['pin'], result['address']
            ))

if __name__ == "__main__":
    root = tk.Tk()
    obj = studentClass(root)
    root.mainloop()