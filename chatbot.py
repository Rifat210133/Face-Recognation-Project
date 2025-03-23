from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, bd=3, bg='powder blue', width=610)
        main_frame.pack()

        img_chat = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\Aichatbot.jpg")
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT, image=self.photoimg, text='CHAT ME', font=('times new roman', 30, 'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('times new roman', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text="Type Something", font=('times new roman', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send, font=('times new roman', 16, 'bold'), width=8, bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data", command=self.clear_data, font=('times new roman', 16, 'bold'), width=8, bg='red', fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_2 = Label(btn_frame, text=self.msg, font=('times new roman', 14, 'bold'), fg='red', bg='white')
        self.label_2.grid(row=1, column=1, padx=5, sticky=W)

    #============Send Function======

    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')

    def clear_data(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        send = '\t\t\t' + 'You: ' + self.entry.get()
        self.text.insert(END, '\n' + send)
        self.text.yview(END)

        if self.entry.get() == '':
            self.msg = 'Please enter some input'
            self.label_2.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_2.config(text=self.msg, fg='red')

#================conversation=================
        if self.entry.get().lower() == 'hello':
            self.text.insert(END, "\n\n" + "Bot: Hi! How can I assist you today?")
        elif self.entry.get().lower() == 'hi':
            self.text.insert(END, "\n\n" + "Bot: Hello! Do you have any questions?")
        elif self.entry.get().lower() == 'how are you?':
            self.text.insert(END, "\n\n" + "Bot: I'm just a bot, but I'm always ready to help! How about you?")
        elif self.entry.get().lower() == 'fantastic':
            self.text.insert(END, "\n\n" + "Bot: That's great to hear! Keep up the positive energy!")
        elif self.entry.get().lower() == 'who created you?':
            self.text.insert(END, "\n\n" + "Bot: I was created to assist in the Face Recognition Attendance System project.")
        elif self.entry.get().lower() == 'what is your name?':
            self.text.insert(END, "\n\n" + "Bot: I am an AI-powered Face Recognition System.")
        elif self.entry.get().lower() == 'bye':
            self.text.insert(END, "\n\n" + "Bot: Thank you for chatting! Have a great day!")
        elif self.entry.get().lower() == 'thank you':
            self.text.insert(END, "\n\n" + "Bot: You're welcome! Let me know if you need anything else.")

        # Adding Face Recognition and Technology-based Responses
        elif self.entry.get().lower() == 'what is face recognition?':
            self.text.insert(END, "\n\n" + "Bot: Face recognition is a biometric technology that identifies or verifies a person using facial features. It is widely used in security, authentication, and attendance systems.")

        elif self.entry.get().lower() == 'how does face recognition work?':
            self.text.insert(END, "\n\n" + "Bot: Face recognition works by analyzing key facial landmarks, such as eyes, nose, and jawline, and comparing them with stored facial data. It uses machine learning models like OpenCV, dlib, and deep learning for high accuracy.")

        elif self.entry.get().lower() == 'what is dlib?':
            self.text.insert(END, "\n\n" + "Bot: Dlib is a powerful C++ library with machine learning tools. It includes facial landmark detection models, like shape_predictor_68_face_landmarks, which help identify facial points for better recognition.")

        elif self.entry.get().lower() == 'what is opencv?':
            self.text.insert(END, "\n\n" + "Bot: OpenCV is an open-source computer vision library that helps process images and videos. It is widely used in face detection, recognition, and real-time AI applications.")

        elif self.entry.get().lower() == 'is face recognition secure?':
            self.text.insert(END, "\n\n" + "Bot: Face recognition is secure when implemented correctly with encryption and anti-spoofing measures. However, some systems can be vulnerable to attacks like deepfake spoofing.")

        elif self.entry.get().lower() == 'where is face recognition used?':
            self.text.insert(END, "\n\n" + "Bot: Face recognition is used in security, law enforcement, banking, mobile unlocking, and attendance systems. Airports and smart surveillance also use it for enhanced security.")

        elif self.entry.get().lower() == 'what are the latest trends in AI?':
            self.text.insert(END, "\n\n" + "Bot: AI is evolving rapidly! Some trends include Generative AI (like ChatGPT), AI-powered robotics, edge AI, and advanced deep learning for computer vision and natural language processing.")

        elif self.entry.get().lower() == 'what is deep learning?':
            self.text.insert(END, "\n\n" + "Bot: Deep learning is a subset of machine learning that uses neural networks to process and analyze large amounts of data. It powers modern AI applications like face recognition, self-driving cars, and voice assistants.")

        else:
            self.text.insert(END, "\n\n" + "Bot: I am not trained to answer this question, but I am learning every day!")

            
                
        


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()