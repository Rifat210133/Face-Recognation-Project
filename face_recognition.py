from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import time
import dlib
from time import strftime
from datetime import datetime
from imutils import face_utils
from scipy.spatial import distance as dist
import joblib

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 27, "bold"), bg="blue", fg="white")
        title_lbl.place(x=-3, y=0, width=1530, height=35)
        
        # Top image
        img_top = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-13_11-54-14.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=650, height=700)
        
        # Bottom image
        img_bottom = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-13_11-54-21.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=40, width=950, height=700)
        
        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("times new roman", 17, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=365, y=620, width=200, height=30)
    
    #-------attendance function-------
    def mark_attendance(self, info2, info1, info, info3):
        with open(r"Face Recognation Project\attendancesheet.csv", "a+", newline="\n") as f:
            f.seek(0)
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(",")
                nameList.append(entry[0])
            if info2 not in nameList:
                now = datetime.now()
                time = now.strftime('%I:%M:%S:%p')
                date = now.strftime('%d-%B-%Y')
                f.writelines(f"\n{info2},{info},{date},{info3},{info1},{time},Present")
        
    # Face Recognition
    def face_recog(self):
        def draw_boundary(img, face_detector, landmarks_detector, face_rec_model, label_encoder, clf, blink_count, match_time):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces_detected = face_detector(gray_image)
            matched = False

            for face in faces_detected:
                # Convert dlib.rectangle to full_object_detection using landmarks
                landmarks = landmarks_detector(img, face)  # Pass the COLOR image here
                face_descriptor = face_rec_model.compute_face_descriptor(img, landmarks) # Pass the COLOR image here
                face_descriptor = np.array(face_descriptor).reshape(1, -1)  # Reshape for prediction

                id = clf.predict(face_descriptor)[0]
                confidence = clf.predict_proba(face_descriptor)[0][id]
                confidence = int(confidence * 100)

                # Database connection
                conn = mysql.connector.connect(
                    host="localhost", user="rifat", password="rifat", database="face_recognizer")
                my_cursor = conn.cursor()

                # Fetch name
                my_cursor.execute("select Name from student where Student_id=" + str(label_encoder.inverse_transform([id])[0]))
                info = my_cursor.fetchone()
                info = "+".join(info) if info else "N/A"

                # Fetch Reg
                my_cursor.execute("select Reg from student where Student_id=" + str(label_encoder.inverse_transform([id])[0]))
                info1 = my_cursor.fetchone()
                info1 = "+".join(info1) if info1 else "N/A"
                
                # Face id
                my_cursor.execute("select Student_id from student where Student_id=" + str(label_encoder.inverse_transform([id])[0]))
                info2 = my_cursor.fetchone()
                info2 = "+".join(info2) if info2 else "N/A"
                
                #Face Department
                my_cursor.execute("select Dep from student where Student_id=" + str(label_encoder.inverse_transform([id])[0]))   
                info3 = my_cursor.fetchone()
                info3 = "+".join(info3) if info3 else "N/A"
                

                x, y = face.left(), face.top()
                w, h = face.width(), face.height()
                print(f"ID: {id}, Name: {info}, Confidence: {confidence}")

                # Draw animated boundary
                if confidence > 92 and blink_count >= 1:
                    # Change the color of the outer rectangle after a match
                    outer_rect_color = (0, 255, 0)  # Green color after match

                    # Display details on the image
                    #cv2.putText(img, f"ID: {info2}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Reg No: {info1}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Name: {info}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    self.mark_attendance(info2,info1,info,info3)

                    if match_time[0] is None:  # Capture match time once
                        match_time[0] = time.time()
                    matched = True
                else:
                    outer_rect_color = (255, 0, 0)  # Blue color before match

                    text = "Unknown Face"
                    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 0.8, 2)

                    # Calculate text background position dynamically
                    text_x = x-12  # Align with face box
                    text_y = max(y - 10, 10)  # Prevent going out of the image top border
                    bg_width = text_size[0] + 10
                    bg_height = text_size[1] + 10

                    # Draw the blue rectangle background
                    cv2.rectangle(img, (text_x, text_y - bg_height), (text_x + bg_width, text_y), (255, 0, 0), -1)
                    cv2.putText(img, text, (text_x + 5, text_y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                # Draw the outer rectangle (always visible)
                cv2.rectangle(img, (x-10, y-10), (x+w+10, y+h+10), outer_rect_color, 2)

            return matched
        
        def recognize(img, face_detector, landmarks_detector, face_rec_model, label_encoder, clf, blink_count, match_time):
            return draw_boundary(img, face_detector, landmarks_detector, face_rec_model, label_encoder, clf, blink_count, match_time)
        
        # Load the trained model and label encoder
        try:
            clf = joblib.load("face_recognition_model.pkl")
            label_encoder = joblib.load("label_encoder.pkl")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading model and label encoder: {str(e)}")
            return
        
        # Load face detection and landmark models
        face_detector = dlib.get_frontal_face_detector()
        landmarks_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
        
        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            print("Error: Could not open video device")
            return
        
        # Blink detection variables
        blink_thres = 0.21
        consecutive_frames = 2
        blink_counter = 0
        total_blinks = 0
        detector = dlib.get_frontal_face_detector()
        lm_model = dlib.shape_predictor(
            r'E:\Face Recognation Project\shape_predictor_68_face_landmarks.dat')
        (L_start, L_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (R_start, R_end) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']
        
        def EAR_cal(eye):
            v1 = dist.euclidean(eye[1], eye[5])
            v2 = dist.euclidean(eye[2], eye[4])
            h1 = dist.euclidean(eye[0], eye[3])
            return (v1 + v2) / (2.0 * h1)
        
        ptime = 0
        match_time = [None]  # Store first match timestamp
        
        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image")
                break
            
            ctime = time.time()
            fps = 1 / (ctime - ptime)
            ptime = ctime
            cv2.putText(img, f"FPS: {int(fps)}", (10, 30),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 100), 2)
            
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector(img_gray)
            
            for face in faces:
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                shapes = lm_model(img_gray, face)
                shapes = face_utils.shape_to_np(shapes)
                left_eye = shapes[L_start:L_end]
                right_eye = shapes[R_start:R_end]
                left_ear = EAR_cal(left_eye)
                right_ear = EAR_cal(right_eye)
                avg_ear = (left_ear + right_ear) / 2
                
                # Eye landmarks with straight lines
                for pt in left_eye:
                    cv2.circle(img, pt, 1, (0, 255, 0), 1)
                for pt in right_eye:
                    cv2.circle(img, pt, 1, (0, 255, 0), 1)
                    
                # Face landmarks
                for (x, y) in shapes:
                    cv2.circle(img, (x, y), 1, (0, 255, 0), 1)  # Changed color to green
                
                # Check for blink
                if avg_ear < blink_thres:
                    blink_counter += 1
                else:
                    if blink_counter >= consecutive_frames:
                        total_blinks += 1
                    blink_counter = 0
                
                cv2.putText(img, f"Blinks: {total_blinks}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            matched = recognize(img, face_detector, landmarks_detector, face_rec_model, label_encoder, clf, total_blinks, match_time)
            
            if match_time[0] is not None and time.time() - match_time[0] > 50:
                break  # Close window 1 second after match
            
            img = cv2.resize(img, (720, 640))
            cv2.imshow("vedio", img)
            
            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()