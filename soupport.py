from tkinter import *
from PIL import Image, ImageTk
import webbrowser


class Helpsupport:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x650+100+50")
        self.root.title("Help & Support")

        # This part is image labels setting start 
        # first header image  
        img = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\banner1.jpg")
        img = img.resize((1300, 120), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1300, height=120)

        # background image 
        bg1 = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\synthetic-data-scaled.jpg")
        bg1 = bg1.resize((1300, 530), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=120, width=1300, height=530)

        # title section
        title_lb1 = Label(bg_img, text="Help & Support", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        title_lb1.place(x=0, y=0, width=1300, height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\web.png")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.website, image=self.std_img1, cursor="hand2")
        std_b1.place(x=250, y=100, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.website, text="Website", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=250, y=280, width=180, height=45)

        # Detect Face button 2
        det_img_btn = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\fb.png")
        det_img_btn = det_img_btn.resize((180, 180), Image.LANCZOS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.facebook, image=self.det_img1, cursor="hand2")
        det_b1.place(x=480, y=100, width=180, height=180)

        det_b1_1 = Button(bg_img, command=self.facebook, text="Facebook", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        det_b1_1.place(x=480, y=280, width=180, height=45)

        # Attendance System button 3
        att_img_btn = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\yt-removebg-preview.png")
        att_img_btn = att_img_btn.resize((180, 180), Image.LANCZOS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.youtube, image=self.att_img1, cursor="hand2")
        att_b1.place(x=710, y=100, width=180, height=180)

        att_b1_1 = Button(bg_img, command=self.youtube, text="Youtube", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        att_b1_1.place(x=710, y=280, width=180, height=45)

        # Help Support button 4
        hlp_img_btn = Image.open(r"E:\Face Recognation Project\Face_Recog_Images\hlp.jpg")
        hlp_img_btn = hlp_img_btn.resize((180, 180), Image.LANCZOS)
        self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img, command=self.gmail, image=self.hlp_img1, cursor="hand2")
        hlp_b1.place(x=940, y=100, width=180, height=180)

        hlp_b1_1 = Button(bg_img, command=self.send_email, text="Send Mail", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        hlp_b1_1.place(x=940, y=280, width=180, height=45)

        

        # create function for button 

    def website(self):
        self.new = 1
        self.url = "https://www.google.com/"
        webbrowser.open(self.url, new=self.new)

    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/p/Adnan-Zaman-100064609411921/"
        webbrowser.open(self.url, new=self.new)

    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/channel/UCU7NDcR_A_9B_wuFgfoJyng"
        webbrowser.open(self.url, new=self.new)

    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url, new=self.new)

    def send_email(self):
        self.new = 1
        self.url = "mailto:adnanzaman215@gmail.com?subject=Saying%20hello%20from%20GFG"
        webbrowser.open(self.url, new=self.new)


if __name__ == "__main__":
    root = Tk()
    obj = Helpsupport(root)
    root.mainloop()