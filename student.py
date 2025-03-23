from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import dlib
import os
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =====================Variables======================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_reg = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        # Search variables
        self.var_search_combo = StringVar()
        self.var_search_entry = StringVar()

        # first image
        img = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_03-29-52.jpg")
        img = img.resize((500, 135), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=135)

        # second image
        img1 = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_03-30-07.jpg")
        img1 = img1.resize((515, 135), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=527, y=0, width=500, height=135)

        # third image
        img2 = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_03-30-14.jpg")
        img2 = img2.resize((500, 135), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1027, y=0, width=500, height=135)

        # bg image
        img3 = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\synthetic-data-scaled.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=-3, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=580)

        img_left = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_03-30-22.jpg")
        img_left = img_left.resize((655, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=655, height=130)

        # Current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=645, height=120)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science and Engineering", "Electrical and Electronics Engineering", "Textile Engineering", "Chemical Engineering", "Civil Engineering", "Mechanical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Course", "OOP", "DSA", "DBMS", "C++", "Python", "EEE", "Machine Learning", "AI", "Data Science", "Web Development", "App Development")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"), width=17, state="readonly")
        semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=260, width=645, height=290)

        # Student ID
        studentId_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"))
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        StudentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_id, width=20, font=("times new roman", 12, "bold"))
        StudentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studentName_label = Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class division
        class_div_label = Label(class_student_frame, text="Class Division", font=("times new roman", 12, "bold"))
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Regi no
        roll_no_label = Label(class_student_frame, text="Regi No", font=("times new roman", 12, "bold"))
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_reg, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_entry = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"))
        gender_entry["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_entry.current(0)
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="DOB", font=("times new roman", 12, "bold"))
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no
        phone_label = Label(class_student_frame, text="Phone No", font=("times new roman", 12, "bold"))
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        teacher_label = Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"))
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio buttons
        radio1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radio1.grid(row=5, column=0)

        radio2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radio2.grid(row=5, column=1)

        # Buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=640, height=30)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 10, "bold"), bg="blue", fg="white", width=22)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 10, "bold"), bg="blue", fg="white", width=22)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 10, "bold"), bg="blue", fg="white", width=22)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 10, "bold"), bg="blue", fg="white", width=22)
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=231, width=640, height=30)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, font=("times new roman", 10, "bold"), bg="blue", fg="white", width=45)
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", font=("times new roman", 10, "bold"), bg="blue", fg="white", width=45)
        update_photo_btn.grid(row=1, column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=790, height=580)

        image_right = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_03-30-27.jpg")
        image_right = image_right.resize((785, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(image_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=2, y=0, width=782, height=130)

        # Search system
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=2, y=135, width=785, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_combo, font=("times new roman", 12, "bold"), width=17, state="readonly")
        search_combo["values"] = ("Select", "Regi No", "Phone No", "Student ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, textvariable=self.var_search_entry, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, command=self.search_data, text="Search", font=("times new roman", 10, "bold"), bg="blue", fg="white", width=10)
        search_btn.grid(row=0, column=3, padx=4)

        showall_btn = Button(search_frame, text="Show All", command=self.fetch_data, font=("times new roman", 10, "bold"), bg="blue", fg="white", width=10)
        showall_btn.grid(row=0, column=4, padx=4)

        # Table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=2, y=210, width=785, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "regi",  "gender","dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("regi", text="Regi No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # =====================Function Declaration======================
    def add_data(self):
        if self.var_dep.get() == "" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_reg.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif "@" not in self.var_email.get() or "." not in self.var_email.get():
            messagebox.showerror("Error", "Invalid email format", parent=self.root)    
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_reg.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    # Fetching data
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content["values"]

        self.var_dep.set(row[0])
        self.var_course.set(row[1])
        self.var_year.set(row[2])
        self.var_sem.set(row[3])
        self.var_id.set(row[4])
        self.var_name.set(row[5])
        self.var_div.set(row[6])
        self.var_reg.set(row[7])
        self.var_gender.set(row[8])
        self.var_dob.set(row[9])
        self.var_email.set(row[10])
        self.var_phone.set(row[11])
        self.var_address.set(row[12])
        self.var_teacher.set(row[13])
        self.var_radio1.set(row[14])

    # Update function
    def update_data(self):
        if self.var_dep.get() == "" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_reg.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif "@" not in self.var_email.get() or "." not in self.var_email.get():
            messagebox.showerror("Error", "Invalid email format", parent=self.root)        
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student 
                        SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Reg=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                        WHERE Student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_reg.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    # Delete function
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Student details successfully deleted", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    # Reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_reg.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # Search function
    def search_data(self):
        if self.var_search_combo.get() == "Select" or self.var_search_combo.get() == "":
            messagebox.showerror("Error", "Select search by option", parent=self.root)
        else:
            search_column = ""
            if self.var_search_combo.get() == "Regi No":
                search_column = "Reg"
            elif self.var_search_combo.get() == "Phone No":
                search_column = "Phone"
            elif self.var_search_combo.get() == "Student ID":
                search_column = "Student_id"

            try:
                conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
                my_cursor = conn.cursor()
                sql_query = f"SELECT * FROM student WHERE {search_column} LIKE %s"
                my_cursor.execute(sql_query, ("%" + self.var_search_entry.get() + "%",))
                rows = my_cursor.fetchall()
                
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                else:
                    messagebox.showinfo("Info", "No records found", parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)
                
                
                


                
                
#=============================================
  
  
    def generate_dataset(self):
        if self.var_dep.get() == "" or self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="rifat", password="rifat", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1

                my_cursor.execute("""
                        UPDATE student 
                        SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Reg=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                        WHERE Student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_reg.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get() == id + 1
                    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ==================== Part of OpenCV with dlib =======================

                # Initialize dlib's face detector
                detector = dlib.get_frontal_face_detector()

                def face_cropped(img):
                    # Convert to grayscale (dlib works on grayscale images)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # Detect faces using dlib
                    faces = detector(gray)
                    for face in faces:
                        # Get the coordinates of the face rectangle
                        x, y, w, h = face.left(), face.top(), face.width(), face.height()
                        # Crop the face region
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (400, 400))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root) 
                    
                
                
                
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()