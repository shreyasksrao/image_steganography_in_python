import tkinter as tk
from tkfilebrowser import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image
import cv2
import main_app
import Encrypt

MIN_WIDTH = 400
MIN_HIEGHT = 400


class Steganography:
    root = tk.Tk()
    flag = 0

    def __init__(self, **kwargs):
        try:
            MIN_WIDTH = kwargs["width"]
        except KeyError:
            pass
        try:
            MIN_HIEGHT = kwargs['height']
        except KeyError:
            pass

        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        left = (self.screenWidth / 2) - (MIN_WIDTH / 2)
        top = (self.screenHeight / 2) - (MIN_HIEGHT / 2)
        self.root.geometry('%dx%d+%d+%d' % (MIN_WIDTH, MIN_HIEGHT, left, top))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.title("Steganography")
        icon = tk.PhotoImage(file='<Replace with any .ico file>')
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon)

        self.text1_var = tk.StringVar()
        self.text2_var = tk.StringVar()
        self.text3_var = tk.StringVar()
        self.save_file_var = tk.StringVar()
        self.decode_label_var = tk.StringVar()
        self.encode_label_var = tk.StringVar()
        self.encrypt_var = tk.StringVar()
        self.encrypt_var1 = tk.StringVar()

        self.upper_frame = tk.Frame(self.root, bg='green', bd=10)
        self.upper_frame.pack(side='top', expand=True, fill=tk.BOTH)

        self.lower_frame = tk.Frame(self.root, bg='green', bd=10)
        self.lower_frame.pack(side='top', expand=True, fill=tk.BOTH)

        self.text_label = tk.Label(self.upper_frame, text="Text to Encrypt :", fg='black', bg="white")
        self.text_label.grid(row=0, column=0, sticky=tk.E)
        self.entry = tk.Entry(self.upper_frame, width=50, textvariable=self.text1_var)
        self.entry.grid(row=0, column=1)

        self.text2_label = tk.Label(self.upper_frame, text="Choose the File name :", fg="black", bg="white")
        self.text2_label.grid(row=1, column=0, sticky=tk.E)
        self.file_name_entry = tk.Entry(self.upper_frame, width=50, textvariable=self.text2_var)
        self.file_name_entry.grid(row=1, column=1)
        self.choose_btn = tk.Button(self.upper_frame, text="...", command=self.take_file)
        self.choose_btn.grid(row=1, column=2)

        self.save_label = tk.Label(self.upper_frame, text='Save file name :', fg='black', bg='white')
        self.save_label.grid(row=3, column=0, sticky=tk.E)
        self.save_file_name_entry = tk.Entry(self.upper_frame, width=50, textvariable=self.save_file_var, state=tk.DISABLED)
        self.save_file_name_entry.grid(row=3, column=1)

        label1 = tk.Label(self.upper_frame, text='Caeser cipher details   :')
        label1.grid(row=4)
        self.encrypt_label = tk.Label(self.upper_frame, text='Encryption Algorithm Level :', fg='black', bg='white')
        self.encrypt_label.grid(row=5, column=0, sticky=tk.E)
        self.encrypt_name_entry = tk.Entry(self.upper_frame, width=50, textvariable=self.encrypt_var)
        self.encrypt_name_entry.grid(row=5, column=1)

        self.encrypt_label1 = tk.Label(self.upper_frame, text='Encryption Algorithm Key :', fg='black', bg='white')
        self.encrypt_label1.grid(row=6, column=0, sticky=tk.E)
        self.encrypt_name_entry1 = tk.Entry(self.upper_frame, width=50, textvariable=self.encrypt_var1)
        self.encrypt_name_entry1.grid(row=6, column=1)

        self.save_check_btn = tk.Checkbutton(self.upper_frame, text='Save encrypted file', command=self.checked)
        self.save_check_btn.grid(row=7)
        
        self.encrypt_btn = tk.Button(self.upper_frame, text="Encrypt/Decrypt", bg="yellow", command=self.encrypt)
        self.encrypt_btn.grid(row=8, column=2)

        self.show_btn = tk.Button(self.upper_frame, text="Show image", bg="red", command=self.show_img)
        self.show_btn.grid(row=8, column=0)

        self.grey_scale_btn = tk.Button(self.upper_frame, text="Grey scale", bg='magenta', command=self.show_grey)
        self.grey_scale_btn.grid(row=8, column=1)

        self.lower_frame1 = tk.Frame(self.lower_frame, bg='orange', bd=10)
        self.lower_frame1.pack(side='top', expand=True, fill=tk.BOTH)
        self.show_res = tk.Label(self.lower_frame1, textvariable=self.text3_var, bg='orange')
        self.show_res.grid(row=0)
        self.text3_var.set("Information about the image\nDisplayed after encryption")

        self.lower_frame3 = tk.Frame(self.lower_frame, bg='orange', bd=10)
        self.lower_frame3.pack(side='top', expand=True, fill=tk.BOTH)
        self.enc_res = tk.Label(self.lower_frame3, text="Encoded string : ", textvariable=self.encode_label_var, bg='orange')
        self.enc_res.grid(row=1)
        self.encode_label_var.set("Encoded string : ")

        self.lower_frame2 = tk.Frame(self.lower_frame, bg='orange', bd=10)
        self.lower_frame2.pack(side='top', expand=True, fill=tk.BOTH)
        self.dec_res = tk.Label(self.lower_frame2, text="Decoded string : ", textvariable=self.decode_label_var, bg='orange')
        self.dec_res.grid(row=2)
        self.decode_label_var.set("Decoded string : ")

        self.enter_choice()

    def enter_choice(self):
        self.encode_var = tk.StringVar().set('Encode')
        self.decode_var = tk.StringVar().set('Decode')
        self.encode_btn = tk.Button(self.upper_frame, text='Encode', bg='violet', textvariable=self.encode_var, command=self.encode)
        self.encode_btn.grid(row=9, column=0)
        self.decode_btn = tk.Button(self.upper_frame, text='Decode', bg='violet', textvariable=self.decode_var, command=self.decode_img)
        self.decode_btn.grid(row=9, column=1)

    def take_file(self):
        self.file_name = askopenfilename(defaultextension=".png",
                                      filetypes=[("All Files", "*.*"),
                                                 ("PNG", "*.png"),
                                                 ("JPEG", "*.jpg")])
                                                 
        print(self.file_name)
        self.text2_var.set(self.file_name)

    def checked(self):
        self.save_file_name_entry.config(state=tk.NORMAL)
        self.flag = 1

    def show_img(self):
        self.scaling_percent = 70
        image = cv2.imread(self.file_name, cv2.IMREAD_UNCHANGED)
        self.width = int(image.shape[1] * self.scaling_percent /100)
        self.height = int(image.shape[0] * self.scaling_percent /100)
        self.dimension = (self.width, self.height)
        resized = cv2.resize(image, self.dimension, interpolation=cv2.INTER_AREA)
        self.total_digit_size = int(int(image.shape[1]) * int(image.shape[0]) * 3 / 8)
        self.digit_entered1 = str(self.text1_var.get())
        self.digit_entered = len(self.digit_entered1)
        self.message = [self.file_name, image.shape[1], image.shape[0], self.width, self.height, self.total_digit_size, self.digit_entered]
        self.text3_var.set("File name : {}\nOriginal width : {}\nOriginal height : {}\nResized Width : {}\nResized Height : {}\nTotal number of letters can be written : {}\nLetters enterd :{}\nRemaining : {}"
                            .format(self.message[0], self.message[1], self.message[2], self.message[3], self.message[4], self.message[5], self.message[6], (self.message[5] - self.message[6])))
        cv2.imshow("Resized image", resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

    def show_grey(self):
        image = cv2.imread(self.file_name, cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(image, self.dimension, interpolation=cv2.INTER_AREA)
        cv2.imshow("Gray scaled image", resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  

    def encode(self):
        self.data_temp = self.text1_var.get()
        self.data = self.encrypted_text
        image = self.text2_var.get()
        print(str(self.data))
        print(str(image))
        new_file = self.save_file_var.get()
        data_ret = main_app.encode(image, self.data, new_file, flag=self.flag)
        string = "Actual Data : {}\nEncoded String : {}".format(self.data_temp, data_ret)
        self.encode_label_var.set(string)
        self.decode_label_var.set('')


    def decode_img(self):
        self.key = self.encrypt_var1.get()
        img = self.text2_var.get()
        decoded_out = main_app.decode(img)
        decrypt_out = Encrypt.encrypt(str(decoded_out), -int(self.key))
        string = "Decrypted String : {}\nDecoded String : {}".format(decrypt_out, decoded_out)
        self.decode_label_var.set(string)
        print(decoded_out)
        self.encode_label_var.set('')

    def encrypt(self):
        self.key = self.encrypt_var1.get()
        level = self.encrypt_var.get()
        if ',' not in self.key:
            self.encrypted_text = Encrypt.encrypt(str(self.text1_var.get()), int(self.key))
        else :
            keys = list(self.key.split(','))
            for i in range(0, len(keys)):
                keys[i] = int(keys[i])
            self.encrypted_text = Encrypt.encrypt_multilevel(str(self.text1_var.get()), int(level), keys) 
        print(self.encrypted_text)


    def run(self):
        self.root.mainloop()

app = Steganography(width=800, height=600)
app.run()
