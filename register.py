from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        
        # ================== Variables ==================
        self.var_uname = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_cpass = StringVar()
        
        # Background Image
        self.image = ImageTk.PhotoImage(file="E:\Face Recognation Project\Face_Recog_Images\synthetic-data-scaled.jpg")
        bg_img = Label(self.root, image=self.image)
        bg_img.place(x=0, y=0, width=1530, height=790)
        
        # Left image
        self.left = ImageTk.PhotoImage(file="E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_13-15-26.jpg")
        left = Label(self.root, image=self.left)
        left.place(x=430, y=100, width=290, height=550)
        
        # Main frame
        frame = Frame(self.root, bg="Darkblue")
        frame.place(x=695, y=100, width=400, height=550)
        
        title = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="Darkblue", fg="yellow")
        title.place(x=20, y=20)
        
        # Label and entry
        f_name = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="Darkblue", fg="white")
        f_name.place(x=50, y=100)
        
        self.txt_fname = Entry(frame, textvariable=self.var_uname, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=300)
        
        l_name = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="Darkblue", fg="white")    
        l_name.place(x=50, y=170)
        
        self.txt_lname = Entry(frame, textvariable=self.var_email, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=50, y=200, width=300)
        
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="Darkblue", fg="white")
        password.place(x=50, y=240)
        
        self.txt_password = Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=270, width=300)
        
        cpassword = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="Darkblue", fg="white")
        cpassword.place(x=50, y=310)
        
        self.txt_cpassword = Entry(frame, textvariable=self.var_cpass, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_cpassword.place(x=50, y=340, width=300)
        
        # Toggle password visibility
        self.show_password = IntVar()
        toggle_password = Checkbutton(frame, text="Show Password", variable=self.show_password, onvalue=1, offvalue=0, bg="Darkblue", font=("times new roman", 12), fg="white", command=self.toggle_password_visibility)
        toggle_password.place(x=50, y=380)
        
        # Register button
        login = Button(self.root, text="Register", command=self.register_data, font=("times new roman", 12), bg="green", fg="white", cursor="hand2")
        login.place(x=800, y=520, width=180)
        
        # Login button
        login_btn = Button(self.root, text="Login Now", font=("times new roman", 12), bg="green", fg="white", cursor="hand2")
        login_btn.place(x=800, y=560, width=180)
        
    # Function to toggle password visibility
    def toggle_password_visibility(self):
        if self.show_password.get():
            self.txt_password.config(show="")
            self.txt_cpassword.config(show="")
        else:
            self.txt_password.config(show="*")
            self.txt_cpassword.config(show="*")
            
    # Function to register data
    def register_data(self):
        print("Register button clicked")
        if self.var_uname.get() == "" or self.var_email.get() == "" or self.var_pass.get() == "" or self.var_cpass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Password do not match", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", user="rifat", password="rifat", database="face_recognizer")
                my_cursor = conn.cursor()
                query = ("select * from register where email=%s")
                value = (self.var_email.get(),)    
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exists, try another email", parent=self.root)
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s)", (self.var_uname.get(), self.var_email.get(), self.var_pass.get(),self.var_cpass.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Register successful", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()