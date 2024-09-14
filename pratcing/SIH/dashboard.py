from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # === icons ===
        try:
            logo_image = Image.open(r"D:\tenical_gumming\pratcing\SIH\image\img1.jpg")
            logo_image = logo_image.resize((50, 50), Image.LANCZOS)
            self.logo_dash = ImageTk.PhotoImage(logo_image)
        except IOError:
            print("Error loading image1.jpg. Please check the file path.")
            self.logo_dash = None

        # === title ===
        if self.logo_dash:
            title = Label(self.root, text="Student Management System", compound=LEFT, image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        else:
            title = Label(self.root, text="Student Management System", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # === Menu ===
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1480, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=50, y=5, width=200, height=40)

        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student)
        btn_student.place(x=280, y=5, width=200, height=40)

        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result)
        btn_result.place(x=520, y=5, width=200, height=40)

        btn_view = Button(M_Frame, text="View", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report)
        btn_view.place(x=760, y=5, width=200, height=40)

        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=1000, y=5, width=200, height=40)

        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit)
        btn_exit.place(x=1240, y=5, width=200, height=40)

        # === content_window ===
        try:
            self.bg_img = Image.open(r"D:\tenical_gumming\pratcing\SIH\image\img2.jpg")
            self.bg_img = self.bg_img.resize((1080, 580), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
        except IOError:
            print("Error loading img2.jpg. Please check the file path.")
            self.bg_img = None

        self.lbl_img = Label(self.root, image=self.bg_img)
        self.lbl_img.place(x=280, y=180, width=1080, height=580)

        # === update_details ===
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        # === footer ===
        footer = Label(self.root, text="Student Result Management System\nContact us for any Technical Issue: 98XXXX23", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)
    
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    
    def logout(self):
        # Placeholder for logout functionality
        print("Logout button clicked")

    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
