from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from PIL import Image, ImageTk

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Course Details")
        self.root.geometry("1280x500+80+170")  # Adjusted height to accommodate buttons
        self.root.config(bg="white")
        self.root.focus_force()

        # Connect to MongoDB
        self.client = MongoClient("mongodb+srv://sahapriyanshu88:ezyCplrNUtcKPuiH@cluster0.4qyhzir.mongodb.net/")
        self.db = self.client["rms"]
        self.collection = self.db["results"]

        # === Title ===
        title = Label(self.root, text="View Student Reports", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626")
        title.place(x=10, y=15, width=1600, height=50)

        # === Search ===
        self.var_search = StringVar()
        self.var_id = None  # Initialize var_id as None
        lbl_search = Label(self.root, text="Search By Roll No.", font=("goudy old style", 20, 'bold'), bg='white')
        lbl_search.place(x=240, y=100)
        text_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20), bg='lightyellow')
        text_search.place(x=500, y=100)

        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=820, y=100, width=100, height=35)

        btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=940, y=100, width=100, height=35)

        # === Result Labels ===
        lbl_roll = Label(self.root, text="Roll No", font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        lbl_roll.place(x=140, y=230, width=150, height=50)

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        lbl_name.place(x=286, y=230, width=150, height=50)

        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        lbl_course.place(x=425, y=230, width=150, height=50)

        lbl_marks = Label(self.root, text="Marks Obtain", font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        lbl_marks.place(x=570, y=230, width=180, height=50)

        lbl_full = Label(self.root, text="Total Marks", font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        lbl_full.place(x=745, y=230, width=180, height=50)

        lbl_per = Label(self.root, text="Percent", font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        lbl_per.place(x=920, y=230, width=150, height=50)

        # === Data Display Labels ===
        self.roll = Label(self.root, font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        self.roll.place(x=140, y=280, width=150, height=50)

        self.name = Label(self.root, font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        self.name.place(x=286, y=280, width=150, height=50)

        self.course = Label(self.root, font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        self.course.place(x=425, y=280, width=150, height=50)

        self.marks = Label(self.root, font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        self.marks.place(x=570, y=280, width=180, height=50)

        self.full = Label(self.root, font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        self.full.place(x=745, y=280, width=180, height=50)

        self.per = Label(self.root, font=("goudy old style", 20, 'bold'), bg='white', bd=2, relief=GROOVE)
        self.per.place(x=920, y=280, width=150, height=50)

        # === Delete Button ===
        btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.delete_student)
        btn_delete.place(x=600, y=400, width=150, height=35)

    def search(self):
        try:
            # Fetch the student document based on the roll number
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required")
            else:

                student = self.collection.find_one({"roll": self.var_search.get()})
                
                if student:
                    # Debugging: print the student document to check the fields
                    # print("Retrieved Student Document:", student)
                    
                    self.var_id = student["_id"]
                    self.roll.config(text=student.get("roll", "N/A"))
                    self.name.config(text=student.get("name", "N/A"))
                    self.course.config(text=student.get("course", "N/A"))
                    self.marks.config(text=student.get("marks","N/A"))
                    self.full.config(text=student.get("full_marks","N/A"))
                    Ob_Mark=int(student.get("marks"))
                    Full_Mark=int(student.get("full_marks"))
                    print(Ob_Mark)
                    print(Full_Mark)
                    PERCENT=Ob_Mark*100/Full_Mark
                    self.per.config(text=str(PERCENT))


                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.var_id = None
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete_student(self):
        try:
            if self.var_id is None:
                messagebox.showerror("Error", "Search student result first", parent=self.root)
            else:
                student = self.collection.find_one({"_id": self.var_id})
                if not student:
                    messagebox.showerror("Error", "Invalid Student result", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        self.collection.delete_one({"_id": self.var_id})
                        messagebox.showinfo("Delete", "Result Deleted Successfully", parent=self.root)
                        self.clear()  # Reset fields after deletion
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()