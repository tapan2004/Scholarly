from pymongo import MongoClient
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Course Details")
        self.root.geometry("1280x500+80+170")  # Adjusted height to accommodate buttons
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ===
        title = Label(self.root, text="Manage Course Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1640, height=35)

        # === Variables ===
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()

        # === Widgets ===
        lbl_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_courseName.place(x=10, y=60)
        
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_duration.place(x=10, y=100)
        
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_charges.place(x=10, y=140)
        
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_description.place(x=10, y=180)

        # === Entry Fields ===
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_courseName.place(x=150, y=60, width=200)
        
        self.text_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.text_duration.place(x=150, y=100, width=200)
        
        self.text_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.text_charges.place(x=150, y=140, width=200)
        
        self.text_description = Text(self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.text_description.place(x=150, y=180, width=500, height=100)

        # === Buttons ===
        self.btn_add = Button(self.root, text='Save', font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.save_course)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        
        self.btn_update = Button(self.root, text='Update', font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update_course)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        
        self.btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.delete_course)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        
        self.btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear_fields)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # === Search Panel ===
        lbl_search_courseName = Label(self.root, text="Search By | Course Name", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_search_courseName.place(x=840, y=60)
        
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        txt_search_courseName.place(x=1100, y=60, width=180)

        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search_course)
        btn_search.place(x=1280, y=60, width=120, height=28)

        # === Table ===
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=980, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=90)
        self.CourseTable.column("description", width=70)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        # === MongoDB Connection ===
        try:
            self.client = MongoClient("mongodb+srv://sahapriyanshu88:ezyCplrNUtcKPuiH@cluster0.4qyhzir.mongodb.net/")  # Adjust connection string if needed
            self.db = self.client["rms"]
            self.collection = self.db["course"]
            self.show()  # Move show() here to ensure MongoDB is initialized
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to connect to MongoDB: {str(ex)}", parent=self.root)

    def clear_fields(self):
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.text_description.delete('1.0', END)
        self.txt_courseName.config(state=NORMAL)

    def save_course(self):
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                existing_course = self.collection.find_one({"name": self.var_course.get()})
                if existing_course:
                    messagebox.showerror("Error", "Course Name already present", parent=self.root)
                else:
                    self.collection.insert_one({
                        "name": self.var_course.get(),
                        "duration": self.var_duration.get(),
                        "charges": self.var_charges.get(),
                        "description": self.text_description.get("1.0", END).strip()
                    })
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def update_course(self):
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                existing_course = self.collection.find_one({"name": self.var_course.get()})
                if not existing_course:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    self.collection.update_one(
                        {"name": self.var_course.get()},
                        {"$set": {
                            "duration": self.var_duration.get(),
                            "charges": self.var_charges.get(),
                            "description": self.text_description.get("1.0", END).strip()
                        }}
                    )
                    messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def delete_course(self):
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                existing_course = self.collection.find_one({"name": self.var_course.get()})
                if not existing_course:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        self.collection.delete_one({"name": self.var_course.get()})
                        messagebox.showinfo("Success", "Course deleted successfully", parent=self.root)
                        self.clear_fields()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def search_course(self):
        search_term = self.var_search.get()
        courses = self.collection.find({"name": {"$regex": search_term, "$options": "i"}})
        self.CourseTable.delete(*self.CourseTable.get_children())
        for course in courses:
            self.CourseTable.insert("", END, values=(
                course.get("cid", ""),
                course.get("name", ""),
                course.get("duration", ""),
                course.get("charges", ""),
                course.get("description", "")
            ))

    def get_data(self, event):
        self.txt_courseName.config(state='readonly')
        selected_item = self.CourseTable.focus()
        content = self.CourseTable.item(selected_item)
        row = content["values"]
        if row:
            self.var_course.set(row[1])
            self.var_duration.set(row[2])
            self.var_charges.set(row[3])
            self.text_description.delete('1.0', END)
            self.text_description.insert('1.0', row[4])

    def show(self):
        self.CourseTable.delete(*self.CourseTable.get_children())
        courses = self.collection.find()
        for course in courses:
            self.CourseTable.insert("", END, values=(
                course.get("cid", ""),
                course.get("name", ""),
                course.get("duration", ""),
                course.get("charges", ""),
                course.get("description", "")
            ))

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
