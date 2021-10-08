import tkinter
from PIL import Image, ImageTk
import json
from difflib import get_close_matches

data_load = json.load('data.json')


def search_word(word):
    if word in date_load:
         meaning_word.delete(1.0, END)
         meaning_word.config(fg='red')
         meaning_word.insert(END, data_load[word])

    elif len(get_close_matches(word, data_load.keys())) > 0:
         meaning_word.config(fg='red')
         meaning_word.delete(1.0, END)
         meaning_word.insert(END, 'Were you finding{} and meaning is: {} '.format(
            get_close_matches(word, data_load.keys()[0])
         final=get_close_matches(word, data_load.keys)

root=tkinter.Tk()
root.title('Mi propio diccionario')

image=Image.open('dict.png')
image_picture=ImageTk.PhotoImage(image)
dest_pic=tkinter.Label(root, image=image_picture)
dest_pic.pack()

a=tkinter.StringVar()
word_1=tkinter.Entry(
    root, textvariable=a, background='blue', fg='white', font=('arial', 40, 'bold'))
word_1.place(relx=.185, rely=0.70, relwidht=.63, relheight=.082)

button_1=tkinter.Button(root, text='Search the word', command=lambda: search_word(
    a.get()), background='red', fg='white', font=('arial', 40, 'bold'))
button_1.place(relx=.25, rely=.85, relwidht=.50, relheight=.052)

meaning_word=tkinter.Text(root, background='white',
                            font=('arial', 20, 'bold'))
meaning_word.place(relx=.200, rely=.05, relwidth=.63, relheight=.16)

root.mainloop()
