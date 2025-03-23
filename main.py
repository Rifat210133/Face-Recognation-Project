from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from attendance import Attendance
from train import Train
from face_recognition import Face_Recognition
from soupport import Helpsupport
from chatbot import ChatBot
import os
from tkinter import messagebox

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Background Image
        img = Image.open(r"Face_Recog_Images\synthetic-data-scaled.jpg")
        img = img.resize((1530, 790), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790) 
        
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Student button
        img1 = Image.open(r"Face_Recog_Images\4236e8efe43ae4a6c7f42c932aa3c01b.jpg")
        img1 = img1.resize((220, 220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        b1 = Button(bg_img, image=self.photoimg1, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)
        
        # Detect face button
        img2 = Image.open(r"Face_Recog_Images\1629899601265.jpg")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        b2 = Button(bg_img, image=self.photoimg2, cursor="hand2",command=self.face_recog)
        b2.place(x=500, y=100, width=220, height=220)
        
        b2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_recog, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_2.place(x=500, y=300, width=220, height=40)
        
        # Attendance button
        img3 = Image.open(r"Face_Recog_Images\blog-–-462-1.jpg")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        b3 = Button(bg_img, image=self.photoimg3, cursor="hand2",command=self.attendance)
        b3.place(x=800, y=100, width=220, height=220)
        
        b3_3 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")   
        b3_3.place(x=800, y=300, width=220, height=40)
        
        # Train data button
        img4 = Image.open(r"Face_Recog_Images\1639367574420.jpg") 
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b4 = Button(bg_img, image=self.photoimg4, cursor="hand2",command=self.train_data)
        b4.place(x=1100, y=100, width=220, height=220)
        
        b4_4 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")   
        b4_4.place(x=1100, y=300, width=220, height=40)
        
        # Photos button
        img5 = Image.open(r"Face_Recog_Images\showimages.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b5 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.open_img)
        b5.place(x=200, y=380, width=220, height=220)
        
        b5_5 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")   
        b5_5.place(x=200, y=580, width=220, height=40)
        
        # Exit button
        img6 = Image.open(r"Face_Recog_Images\logout-exit-door-simple-icon-260nw-2536969483.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b6 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.exit)
        b6.place(x=500, y=380, width=220, height=220)
        
        b6_6 = Button(bg_img, text="Exit", cursor="hand2",command=self.exit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white") 
        b6_6.place(x=500, y=580, width=220, height=40)
        
        # Support button
        img7 = Image.open(r"Face_Recog_Images\help-desk-customer-care-team-260nw-119170255.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b7 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.support)
        b7.place(x=800, y=380, width=220, height=220)
        
        b7_7 = Button(bg_img, text="Support", cursor="hand2",command=self.support, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_7.place(x=800, y=580, width=220, height=40)
  
        
        #chatbot button
        img8 = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\Aichatbot.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b8 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.chatbot)
        b8.place(x=1100, y=380, width=220, height=220)
        
        b8_8 = Button(bg_img, text="Chatbot", cursor="hand2",command=self.chatbot, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_8.place(x=1100, y=580, width=220, height=40)
  
  
  
#=======================Functions=======================      
    
    def open_img(self):
        os.startfile("data")    
            
        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
        
    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)    
        
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)  
    
    
    def face_recog(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)     


    def exit(self):
        self.exit = messagebox.askyesno("Face Recognition", "Do you want to exit?")
        if self.exit > 0:
            self.root.destroy()
        else:
            return
    
    def support(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpsupport(self.new_window)    
        
    
    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()