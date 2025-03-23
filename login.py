from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
from main import Face_Recognition_System


def mainn():
    root = Tk()
    obj = Login_System(root)
    root.mainloop()

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1350x700+100+50")
        
        img = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\synthetic-data-scaled.jpg")
        img = img.resize((1530, 790), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=800)
        
        frame=Frame(self.root, bg="Darkblue")
        frame.place(x=500, y=100, width=340, height=500)
        
        img1 = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\profile_6914786.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        lblimg = Label(image=self.photoimg1, bg="Darkblue", borderwidth=0)
        lblimg.place(x=620, y=110, width=100, height=100)
        
        get_str = Label(frame, text="Wellcome", font=("times new roman", 20, "bold"), fg="Yellow", bg="Darkblue")
        get_str.place(x=105, y=110)
        
        # Username
        username = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="Darkblue")
        username.place(x=86, y=170)
        self.txtuser = Entry(frame, font=("times new roman", 15), bg="lightgray")
        self.txtuser.place(x=60, y=200, width=220)
        
        img3 = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_17-12-28-removebg-preview.png")
        img3 = img3.resize((28, 28), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg2 = Label(image=self.photoimg3, bg="Darkblue", borderwidth=0)
        lblimg2.place(x=559, y=270, width=28, height=28) 
        
        # Password
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="Darkblue")
        password.place(x=86, y=238)
        self.txtpass = Entry(frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.txtpass.place(x=60, y=266, width=220)
        
        img2 = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\key_11410394.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimg2, bg="Darkblue", borderwidth=0)
        lblimg1.place(x=559, y=336, width=25, height=25)   
        
        # Toggle Password Visibility
        self.var = IntVar()  # Variable to store the state of the checkbox (show/hide password)
        self.toggle_check = Checkbutton(frame, text="Show Password", variable=self.var, font=("times new roman", 12), fg="white", bg="Darkblue", command=self.toggle)
        self.toggle_check.place(x=60, y=296)
        
        # Login Button
        login_btn = Button(frame, command=self.login, cursor="hand2", text="Login", font=("times new roman", 15), fg="white", bg="green")   
        login_btn.place(x=90, y=330, width=160)
        
        # Register Button
        register_btn = Button(frame,command=self.register_window, text="New User Register", font=("times new roman", 13,"bold"),borderwidth=0,fg="red", bg="Darkblue",activebackground="Darkblue")  
        register_btn.place(x=10, y=390, width=160)
        
        # Forget Password
        forget_btn = Button(frame,command=self.forgot_password_window, text="Forget Password", font=("times new roman", 13,"bold"),borderwidth=0,fg="red", bg="Darkblue",activebackground="Darkblue")
        forget_btn.place(x=4, y=420, width=160)
        
        
        #Toogle Password
        
    def toggle(self):
        if self.var.get() == 1:
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")
    
    
    def register_window(self):
          self.root.destroy()  # Close the current window
          self.new_window = Tk()
          self.app = Register(self.new_window)
    
         
            
        # Login Function===========================================================
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        # elif self.txtuser.get()=="admin" or self.txtpass.get()=="1234":
        #     self.new_window = Toplevel(self.root)
        #     self.app = Face_Recognition_System(self.new_window)
        else:
            conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
             
            row=my_cursor.fetchone()
            if row==None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root)
            else: 
                    
                   self.root.destroy()  # Close the current window
                   self.new_window = Tk()
                   self.app = Face_Recognition_System(self.new_window)
        
  
  
  #========================================Forgot Password================================================        
    def forgot_password_window(self):
        
            try:
                conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where email=%s", (self.txtuser.get(),))
                row = my_cursor.fetchone()
   
                conn.close()
                self.roo2 = Toplevel()
                self.roo2.title("Forget Password")
                self.roo2.geometry("350x400+480+100",)
                
                
                lb=Label(self.roo2,text="Forget Password",font=("times new roman",20,"bold"),bg="red",fg="white")   
                lb.place(x=0,y=10,relwidth=1)
                
                self.var_email = StringVar()
                self.var_pass = StringVar()
                self.var_cpass = StringVar()
                
                
                l_name = Label(self.roo2, text="Enter Email", font=("times new roman", 15, "bold"), bg="Darkblue", fg="white")    
                l_name.place(x=40, y=70)
                
                self.txt_lname = Entry(self.roo2, textvariable=self.var_email, font=("times new roman", 15), bg="lightgray")    
                self.txt_lname.place(x=40, y=100, width=250)
                
                
                
                password = Label(self.roo2, text="New Password", font=("times new roman", 15, "bold"), bg="Darkblue", fg="white")   
                password.place(x=40, y=140)
                
                self.txt_password = Entry(self.roo2, textvariable=self.var_pass, font=("times new roman", 15), bg="lightgray", show="*")    
                self.txt_password.place(x=40, y=170, width=250)
                
                
                
                cpassword = Label(self.roo2, text="Confirm Password", font=("times new roman", 15, "bold"), bg="Darkblue", fg="white")  
                cpassword.place(x=40, y=200)
                
                self.txt_cpassword = Entry(self.roo2, textvariable=self.var_cpass, font=("times new roman", 15), bg="lightgray", show="*")  
                self.txt_cpassword.place(x=40, y=240, width=250) 
                
                # Toggle password visibility
                self.show_password = IntVar()
                toggle_password = Checkbutton(self.roo2, text="Show Password", variable=self.show_password, onvalue=1, offvalue=0, bg="Darkblue", font=("times new roman", 12), fg="white", command=self.toggle_password_visibility)
                toggle_password.place(x=40, y=270)
                
                
               
                
                btn = Button(self.roo2,command=self.update, text="Update", font=("times new roman", 12), bg="green", fg="white")   
                btn.place(x=90, y=310, width=150)
                
                
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)     
                
               
                
    def update(self):
        if self.var_email.get()=="" or self.var_pass.get()=="" or self.var_cpass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.roo2)
        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Password do not match", parent=self.roo2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
                my_cursor = conn.cursor()
                query = ("select * from register where email=%s")
                value = (self.var_email.get(),)    
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "User does not exist", parent=self.roo2)
                else:
                    my_cursor.execute("update register set password=%s,confirmpass=%s where email=%s", (self.var_pass.get(),self.var_cpass.get(), self.var_email.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Password updated successfully", parent=self.roo2)
                    
                    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.roo2)
                        
                                
                    
    #Toggle password function
    def toggle_password_visibility(self):
        if self.show_password.get():
            self.txt_password.config(show="")
            self.txt_cpassword.config(show="")
        else:
            self.txt_password.config(show="*")
            self.txt_cpassword.config(show="*")            
                    
                    
                        
                   
               
 
 
 #register class==============================================================
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
        login_btn = Button(self.root,command=self.return_login, text="Login Now", font=("times new roman", 12), bg="green", fg="white", cursor="hand2")
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
        elif "@" not in self.var_email.get() or "." not in self.var_email.get():
            messagebox.showerror("Error", "Invalid email format", parent=self.root)    
        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Password do not match", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
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
           
    def return_login(self):
         self.root.destroy()
         self.new_window = Tk()
         self.app = Login_System(self.new_window)
         
        
          
          
          
          

if __name__ == "__main__":
    mainn()