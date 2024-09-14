from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime
from math import radians, sin, cos
from tkinter import messagebox
from pymongo import MongoClient
import pymongo

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("SCHOLARLY")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        self.lbl = Label(self.root, text="\nWelcome", font=("Book Antiqua", 25, "bold"),
                         fg="white", compound=BOTTOM, bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        self.working()

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"),
                      bg="white", fg="#08A3D2").place(x=250, y=50)

        email = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"),
                      bg="white", fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"),
                      bg="white", fg="gray").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("times new roman", 15), bg="lightgray", show='*')
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, text="Register new Account?", command=self.register_window, font=("times new roman", 14),
                         bg="white", bd=0, fg="#B00857", cursor="hand2").place(x=250, y=320)
        
        btn_forgot = Button(login_frame, text="Forgot password?", font=("times new roman", 14),
                         bg="white", bd=0, fg="#B00857", cursor="hand2").place(x=250, y=355)


        btn_login = Button(login_frame, text="Login", command=self.login,
                           font=("times new roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2")
        btn_login.place(x=340, y=400, width=180, height=40)

    def register_window(self):
        self.root.destroy()
        import register
        root = Tk()  # Create a new Tkinter root window
        obj = register.Register(root)  # Pass the root window to the Register class
        root.mainloop()

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                self.client = MongoClient("mongodb+srv://sahapriyanshu88:ezyCplrNUtcKPuiH@cluster0.4qyhzir.mongodb.net/")
                self.db = self.client["rms"]
                self.collection = self.db["users"]

                # Fetch the document from MongoDB
                query = {
                    "email": self.txt_email.get(),
                    "password": self.txt_pass_.get()
                }
                row = self.collection.find_one(query)

                # Check if the document exists
                if row is None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)
                    self.client.close()
                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.client.close()
                    self.root.destroy()

                    import dashboard
                    root = Tk()
                    obj = dashboard.RMS(root)
                    root.mainloop()

            except pymongo.errors.PyMongoError as e:
                # Catch MongoDB-specific errors
                messagebox.showerror("Database Error", f"Error due to: {str(e)}", parent=self.root)
            except Exception as es:
                # Catch all other exceptions
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    def clock_image(self, hr_, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        # Corrected path using raw string
        bg = Image.open(r"D:\tenical_gumming\pratcing\SIH\image\clockImageForLogin.png")
        bg = bg.resize((300, 300), Image.Resampling.LANCZOS)
        clock.paste(bg, (50, 50))

        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr_)), 200 - 50 * cos(radians(hr_))), fill="#DF005E", width=4)
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)

        draw.ellipse((195, 195, 210, 210), fill="darkslategray")
        clock.save("clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        hr_ = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360
        self.clock_image(hr_, min_, sec_)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

root = Tk()
obj = Login_window(root)
root.mainloop()
