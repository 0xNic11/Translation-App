from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

root=Tk()
root.title("Mini Translator")

# Window Controller
width_ = 1080
height_ = 430
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width_ / 2)
y = (screen_height / 2) - (height_ / 2)
root.geometry(f'{width_}x{height_}+{int(x)}+{int(y)}') # Window size
root.resizable(0, 0)

# Icon
image_icon = PhotoImage(file="language-square.png")
root.iconphoto (False, image_icon)

root.configure(background="white")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure (text=c1)
    root.after(1000, label_change)
    
# Translate button function
def translate_now():
    text_left = text1.get(1.0, END)
    text_right = text2.get(1.0, END)
    
    # Check if langaue is selected or not
    if combo1.get() == "Select Language" or combo2.get() == "Select Language":
        select_language_error()
        return
        
    if (len(text_right) == 1 and combo1.get() != "Select Language" and len(text_left) == 1) \
    or (len(text_left) == 1 and combo2.get() != "Select Language" and len(text_right) == 1):
        write_text_error()
        return
        
    if len(text_left) == 1 and combo1.get() != "Select Language":
        write_text_error()
        return
        
    
    t1 = Translator()
    trans_text = t1.translate(text_left, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text
    
    text2.delete(1.0, END)
    text2.insert(END, trans_text)
    
def swap():
    left_lang = combo1.get()
    right_lang = combo2.get()
    temp = combo1.get()
    
    # Swap languages to be translated
    left_lang = right_lang
    right_lang = temp
    
    combo1.set(left_lang)
    combo2.set(right_lang)
    

def select_language_error():
    messagebox.showerror("Error!", "Select a language to translate to!")
    
def write_text_error():
    messagebox.showerror("Error!", "You must type a text!")
    
    
# Images
arrow_image = PhotoImage(file="arrow-swap.png")
translate_image = PhotoImage(file="Translate.png")

# Google Translation API
language = googletrans.LANGUAGES
lang1 = language.keys()

languageV = list(language.values())
languages_cap = [lang.capitalize() for lang in languageV]
languageV = languages_cap

# Left Combobox
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English")
label1 = Label(root, text="English", font="segoe 30 bold", bg="white",width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Right combobox
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730,y=20)
combo2.set("Select Language")
label2 = Label (root, text="Select Language", font="segoe 30 bold", bg="white",width=18, 
                bd=5, relief=GROOVE, background="#EAEFF6")
label2.place(x=620, y=50)

# Left frame
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=10, y=118, width=440, height=210)
text1 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, padx=7)
text1.place(x=0, y=0, width=430, height=200)

# Left Scrollbar
scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# Second frame
f2 = Frame (root,bg="Black", bd=5, background="#1B68D5")
f2.place(x=620, y=118, width=440, height=210)
text2 = Text(f2, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, padx=7)
text2.place(x=0, y=0,width=430,height=200)

# Right Scrollbar 
scrollbar2=Scrollbar(f2)
scrollbar2.pack (side="right", fill='y')
scrollbar2.configure (command=text2.yview)
text2.configure (yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, image=translate_image, font=("Roboto", 15), activebackground="white", cursor="hand2",
bd=0, width=165, height=70, bg="white", fg="white", command=translate_now)
translate.place(x=452, y=340)

swap_languages = Button(root, image=arrow_image, background="white", activebackground="white", borderwidth=0, 
                        command=swap)
swap_languages.place(x=510, y=58)

label_change()

root.mainloop()