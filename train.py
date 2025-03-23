from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import dlib
import os
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Title label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 27, "bold"), bg="blue", fg="white")
        title_lbl.place(x=-3, y=0, width=1530, height=35)
        
        # Top image
        img_top = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_10-46-42.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1530, height=325)
        
        # Button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 27, "bold"), bg="blue", fg="white")
        b1_1.place(x=0, y=365, width=1530, height=35)
        
        # Bottom image
        img_bottom = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_10-46-33.jpg")
        img_bottom = img_bottom.resize((1530, 400), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=400, width=1530, height=400)
    
    def train_classifier(self):
        try:
            # Directory where images are stored
            data_dir = "data"
            if not os.path.exists(data_dir):
                messagebox.showerror("Error", f"Directory '{data_dir}' does not exist")
                return
            
            # Fetch all image paths
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]
            
            if not path:
                messagebox.showerror("Error", "No images found in the directory")
                return
            
            # Initialize the face detector and facial landmarks detector
            face_detector = dlib.get_frontal_face_detector()
            landmarks_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Path to landmarks predictor
            face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
            
            # Prepare training data
            faces = []
            ids = []
            
            for image in path:
                try:
                    img = Image.open(image).convert('RGB')  # Convert to RGB
                    img = np.array(img)
                    
                    # Detect faces in the image
                    faces_detected = face_detector(img)
                    
                    # For each face detected, find landmarks and extract face embeddings
                    for face in faces_detected:
                        landmarks = landmarks_detector(img, face)
                        face_descriptor = face_rec_model.compute_face_descriptor(img, landmarks)
                        
                        id = int(os.path.split(image)[1].split('.')[1])  # Extract ID from filename
                        
                        faces.append(face_descriptor)
                        ids.append(id)
                        cv2.imshow("Training in Progress", img)
                        cv2.waitKey(1)
                except Exception as e:
                    print(f"Skipping image {image} due to error: {e}")
            
            if not faces or not ids:
                messagebox.showerror("Error", "No valid data found for training")
                return
            
            # Encode the labels
            label_encoder = LabelEncoder()
            ids = label_encoder.fit_transform(ids)
            
            # Check the number of unique labels
            unique_labels = np.unique(ids)
            print(f"Unique labels: {unique_labels}")
            if len(unique_labels) <= 1:
                messagebox.showerror("Error", "The number of classes has to be greater than one")
                return
            
            # Train the classifier
            clf = SVC(kernel='linear', probability=True)
            clf.fit(faces, ids)
            print("Classifier trained successfully")
            
            # Save the trained model and label encoder
            model_path = os.path.join(os.getcwd(), "face_recognition_model.pkl")
            label_encoder_path = os.path.join(os.getcwd(), "label_encoder.pkl")
            joblib.dump(clf, model_path)
            joblib.dump(label_encoder, label_encoder_path)
            print(f"Classifier saved at {model_path}")
            print(f"Label encoder saved at {label_encoder_path}")
            
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training datasets completed successfully!!!")
        except Exception as e:
            cv2.destroyAllWindows()
            messagebox.showerror("Error", f"An error occurred during training: {str(e)}")
    
    def align_face(self, img, landmarks):
        # Using the landmarks to align the face for better recognition
        # Extract the region around eyes and nose to align face
        eye_left = (landmarks.part(36).x, landmarks.part(36).y)
        eye_right = (landmarks.part(45).x, landmarks.part(45).y)
        nose = (landmarks.part(30).x, landmarks.part(30).y)
        
        # Implement face alignment logic here (optional)
        # Use affine transformations or other methods to align the face
        # For now, this is just a placeholder function that returns the image without actual alignment
        return img


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()