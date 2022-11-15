from tkinter import *
import random

window = Tk()
window.title = "Random Password Generator"
window.geometry("450x400")

#box number for char
label_frame = LabelFrame(window, text="Berapa karakter yang diperlukan (6 - 8) :")
label_frame.pack(pady=20)
len_numbox = Entry(label_frame, width=25)
len_numbox.pack(padx = 20, pady = 20)

#box for password
pass_box = Entry(window, text = "", width=25)
pass_box.pack(pady=15)

#frame for button
button_fr = Frame(window)
button_fr.pack(pady = 25)

def generate():
    try:
        pass_length = int(len_numbox.get())
        finals = ''
        for i in range(0,pass_length):
            point = random.randint(1,3)
            if point == 1:
                finals = finals + chr(random.randint(65,90)).lower()
            elif point == 2:
                finals = finals + chr(random.randint(65,90)).upper()
            else:
                finals = finals + str(random.randint(0,9))
        pass_box.insert(0,finals)
    except  ValueError:
        msg_error = Label(window, fg="red", text="Masukkan angka untuk karakter yang diinginkan")
        msg_error.place(x = 130, y = 100)
        
generate_btn = Button(button_fr, text="Generate Random Password", command=generate)
generate_btn.grid(row = 0, column = 0, padx=10)

def copy_pass():
    window.clipboard_clear()
    window.clipboard_append(pass_box.get())
    
window.mainloop()