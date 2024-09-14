from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from pymongo import MongoClient

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1480x800+0+0")
        self.root.config(bg="white")

        # === MongoDB Connection ===
        try:
            self.client = MongoClient("mongodb+srv://sahapriyanshu88:ezyCplrNUtcKPuiH@cluster0.4qyhzir.mongodb.net/")
            self.db = self.client["rms"]
            self.collection = self.db["users"]
        except Exception as e:
            messagebox.showerror("Error", f"Database connection error: {e}")
            self.root.destroy()
            return

        # === Background Image ===
        try:
            bg_image = Image.open(r"D:\tenical_gumming\pratcing\SIH\image\register.jpg")
            self.bg = ImageTk.PhotoImage(bg_image)
            bg_label = Label(self.root, image=self.bg)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image file not found. Please check the path and try again.")
            self.root.destroy()
            return
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.root.destroy()
            return

        # === LEFT Image ===
        try:
            left_image = Image.open(r"D:\tenical_gumming\pratcing\SIH\image\register1.jpg")
            self.left = ImageTk.PhotoImage(left_image)
            left_label = Label(self.root, image=self.left)
            left_label.place(x=60, y=100, width=400, height=500)
        except FileNotFoundError:
            messagebox.showerror("Error", "Left image file not found. Please check the path and try again.")
            self.root.destroy()
            return
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.root.destroy()
            return

        # === Register Frame ===
        self.frame1 = Frame(self.root, bg="white")
        self.frame1.place(x=480, y=100, width=700, height=500)

        title = Label(self.frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)

        # ------------------Row1
        self.f_name_label = Label(self.frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.f_name_label.place(x=50, y=100)
        self.f_name = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.f_name.place(x=50, y=130, width=250)

        self.l_name_label = Label(self.frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.l_name_label.place(x=370, y=100)
        self.l_name = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.l_name.place(x=370, y=130, width=250)

        # ------------------Row2
        self.contact_label = Label(self.frame1, text="Contact Number", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.contact_label.place(x=50, y=170)
        self.contact = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.contact.place(x=50, y=200, width=250)

        self.email_label = Label(self.frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.email_label.place(x=370, y=170)
        self.email = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.email.place(x=370, y=200, width=250)

        # ------------------Row3
        self.question_label = Label(self.frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.question_label.place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(self.frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)
        
        self.answer_label = Label(self.frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.answer_label.place(x=370, y=240)
        self.txt_answer = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # ------------------Row4
        self.password_label = Label(self.frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.password_label.place(x=50, y=310)
        self.txt_password = Entry(self.frame1, font=("times new roman", 15), bg="lightgray", show='*')
        self.txt_password.place(x=50, y=340, width=250)

        self.cpassword_label = Label(self.frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.cpassword_label.place(x=370, y=310)
        self.txt_cpassword = Entry(self.frame1, font=("times new roman", 15), bg="lightgray", show='*')
        self.txt_cpassword.place(x=370, y=340, width=250)

        # ------------------Terms
        self.var_chk=IntVar()
        self.chk = Checkbutton(self.frame1, text="I Agree To The Terms & Conditions",variable=self.var_chk ,onvalue=1, offvalue=0, bg="white", font=("times new roman", 12))
        self.chk.place(x=50, y=380)

        # ------------------Buttons
        try:
            self.btn_img = Image.open(r"D:\tenical_gumming\pratcing\SIH\image\register_logo.jpg")
            self.btn_img = ImageTk.PhotoImage(self.btn_img)
            self.register_btn = Button(self.frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_action)
            self.register_btn.place(x=250, y=430)
        except FileNotFoundError:
            messagebox.showerror("Error", "Register button image file not found. Please check the path and try again.")
            self.root.destroy()
            return
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.root.destroy()
            return

        self.sign_in_btn = Button(self.root, text="Sign In", font=("times new roman", 20), bd=0,bg="lightblue", cursor="hand2", command=self.login_window)
        self.sign_in_btn.place(x=165, y=547, width=180)

    def register_action(self):
        if self.f_name.get() == "" or self.l_name.get() == "" or self.contact.get() == "" or self.email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
        elif self.var_chk.get()==0:
                messagebox.showerror("Error","Please Agree our terms & condition",parent=self.root)
        else:
            try:
                query = {
                    "email": self.email.get()
                }
                row = self.collection.find_one(query)

                # Check if the document exists
                if row is not None:
                    messagebox.showerror("Error", "User Already Exist", parent=self.root)
                else:
                    user_data = {
                        "first_name": self.f_name.get(),
                        "last_name": self.l_name.get(),
                        "contact": self.contact.get(),
                        "email": self.email.get(),
                        "security_question": self.cmb_quest.get(),
                        "answer": self.txt_answer.get(),
                        "password": self.txt_password.get()
                    }
                    self.collection.insert_one(user_data)
                    self.client.close()
                    messagebox.showinfo("Success", "Registration successful", parent=self.root)
                    self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=self.root)

    def login_window(self):
        self.root.destroy()
        import login
        root = Tk()  # Create a new Tkinter root window
        obj = login.Login_window(root)  # Pass the root window to the Login class
        root.mainloop()
        
    def clear_fields(self):
        self.f_name.delete(0, END)
        self.l_name.delete(0, END)
        self.contact.delete(0, END)
        self.email.delete(0, END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()