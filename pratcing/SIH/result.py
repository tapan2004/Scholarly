from tkinter import *
import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from PIL import Image, ImageTk

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Details")
        self.root.geometry("1280x500+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Load Images ===
        try:
            logo_image = Image.open(r"D:\tenical_gumming\pratcing\SIH\image\result2.jpg")
            logo_image = logo_image.resize((50, 50), Image.LANCZOS)
            self.logo_dash = ImageTk.PhotoImage(logo_image)
        except FileNotFoundError:
            self.logo_dash = None
            print("Logo image not found. Proceeding without logo.")
        except Exception as e:
            print(f"Unexpected error loading logo image: {e}")
            self.logo_dash = None

        # === Title ===
        title = Label(self.root, text=" Manage Result System", compound=LEFT, image=self.logo_dash, font=("Goudy Old Style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # === Variables ===
        self.var_roll = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_marks = tk.StringVar()
        self.var_full_marks = tk.StringVar()

        # === MongoDB Connection ===
        try:
            client = MongoClient("mongodb+srv://sahapriyanshu88:ezyCplrNUtcKPuiH@cluster0.4qyhzir.mongodb.net/")
            db = client["rms"]
            self.collection1 = db["results"]
            self.collection2 = db["coursetext_course"]
        except Exception as e:
            messagebox.showerror("Error", f"Database connection error: {e}")

        # === Labels and Inputs ===
        lbl_roll = Label(self.root, text=" Roll Number", font=("Goudy Old Style", 15, "bold"), bg="white").place(x=50, y=120)
        txt_roll = Entry(self.root, textvariable=self.var_roll, font=("Goudy Old Style", 15), bg='lightyellow').place(x=190, y=120, width=200)

        lbl_name = Label(self.root, text="Student Name", font=("Goudy Old Style", 15, "bold"), bg="white").place(x=50, y=180)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("Goudy Old Style", 15), bg='lightyellow', state='readonly').place(x=200, y=180, width=200)

        lbl_select_course = Label(self.root, text=" Find Course", font=("Goudy Old Style", 15, "bold"), bg="white").place(x=50, y=240)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("Goudy Old Style", 15), bg='lightyellow', state='readonly').place(x=200, y=240, width=200)

        lbl_marks = Label(self.root, text="Marks Obtained", font=("Goudy Old Style", 15, "bold"), bg="white").place(x=50, y=300)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("Goudy Old Style", 15), bg='lightyellow').place(x=220, y=300, width=200)

        lbl_full_marks = Label(self.root, text="Full  Marks", font=("Goudy Old Style", 15, "bold"), bg="white").place(x=50, y=350)
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("Goudy Old Style", 15), bg='lightyellow').place(x=210, y=350, width=200)

        # === Search Button ===
        btn_search = Button(self.root, text='Search', command=self.search_student_details, font=("Goudy Old Style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2")
        btn_search.place(x=410, y=120, width=120, height=28)

        # === Buttons ===
        self.btn_submit = tk.Button(self.root, text='Save', font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.submit)
        self.btn_submit.place(x=200, y=400, width=110, height=40)

        self.btn_clear = tk.Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=320, y=400, width=110, height=40)

        # === Background Image ===
        try:
            bg_img = Image.open(r"D:\tenical_gumming\pratcing\SIH\image\result.jpg")
            bg_img = bg_img.resize((910, 480), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(bg_img)
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image file not found. Please check the path and try again.")
            self.root.destroy()
            return
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.root.destroy()
            return

        self.lbl_img = Label(self.root, image=self.bg_img)
        self.lbl_img.place(x=550, y=80, width=920, height=500)

    def search_student_details(self):
        roll = self.var_roll.get()
        if roll == "":
            messagebox.showerror("Error", "Please Enter Roll No", parent=self.root)
        else:
            try:
                query = {"roll": roll}
                print(f"Searching for roll number: {roll}")  # Debugging line
                row = self.collection2.find_one(query)

                if row is None:
                    messagebox.showerror("Error", "Please Enter Correct Roll No", parent=self.root)
                else:
                    self.var_name.set(row['name'])
                    self.var_course.set(row['course'])
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    def submit(self):
        # Prepare data from the form fields
        data = {
            "roll": self.var_roll.get(),
            "name": self.var_name.get(),
            "course": self.var_course.get(),
            "marks": self.var_marks.get(),
            "full_marks": self.var_full_marks.get()
        }

        # Check if any of the required fields are empty
        if "" in data.values():
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                # Insert data into MongoDB collection
                self.collection1.insert_one(data)
                messagebox.showinfo("Success", "Result added successfully!")
                self.clear()  # Clear the form after saving
            except Exception as e:
                messagebox.showerror("Error", f"Error while inserting data: {e}")

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()