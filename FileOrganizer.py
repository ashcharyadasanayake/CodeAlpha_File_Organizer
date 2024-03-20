import os
from customtkinter import *
import shutil

app = CTk()
app.geometry("600x400")
pat = CTkEntry(app, font=("Inter-SemiBold", 30), width=300)
pat.place(relx=0.5, rely=0.47, anchor=CENTER)
app.title("File Organizer")


def organize():
    path = pat.get()
    files = os.listdir(path)

    for files in files:
        name, extension = os.path.splitext(files)
        print(name, extension)
        extension = extension[1:]

        if os.path.exists(path + "/" + extension):
            shutil.move(path + "/" + files, path + "/" + extension + "/" + files)

        else:
            os.makedirs(path + "/" + extension)
            shutil.move(path + "/" + files, path + "/" + extension + "/" + files)


CTkLabel(
    app,
    text="File Organizer",
    font=("Inter-SemiBold", 35),
).place(relx=0.5, rely=0.3, anchor=CENTER)

organize_btn = CTkButton(
    app,
    text="Organize",
    font=("Inter-SemiBold", 30),
    width=200,
    height=80,
    command=organize,
)
organize_btn.place(relx=0.5, rely=0.7, anchor=CENTER)


app.resizable(False, False)
app.mainloop()
