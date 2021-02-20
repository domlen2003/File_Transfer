import tkinter as tk
from tkinter import filedialog
from os import walk
import shutil
import os

global src_dir
global name
global dst_dir

strings = ["", "", ""]


def select_src():
    global src_dir
    src_dir = filedialog.askdirectory()
    strings[0] = "Source: " + src_dir
    update_strings()
    print("Set source directory to %s" % src_dir)


def dst_src():
    global name
    global dst_dir
    dst_dir = filedialog.askdirectory()
    name = dst_dir.split("/")[-1]
    strings[1] = "Destination: " + dst_dir
    strings[2] = "Directory and Filename: " + name
    update_strings()
    print("Set destination_directory to %s and name to %s " % (dst_dir, name))


def copy():
    i = 0
    print("Copying from %s to %s" % (src_dir, dst_dir))
    for (dirpath, dirnames, filenames) in walk(src_dir):
        for file in filenames:
            i += 1
            copy_rename(file, name + " " + i.__str__() + ".png")
        break


def copy_rename(old_file_name, new_file_name):
    src_file = os.path.join(src_dir, old_file_name)
    shutil.copy(src_file, dst_dir)

    dst_file = os.path.join(dst_dir, old_file_name)
    new_dst_file_name = os.path.join(dst_dir, new_file_name)

    os.rename(dst_file, new_dst_file_name)


def update_strings():
    for widget in frame.winfo_children():
        widget.destroy()
    for string in strings:
        label = tk.Label(frame, text=string)
        label.pack()


root = tk.Tk()
root.title("File Copy")
root.geometry("700x180")
root.resizable(0, 0)

canvas = tk.Canvas(root, height=100, width=700, bg="#37393F")
canvas.pack()

frame = tk.Frame(root, bg="#B9BBBE")
frame.place(relwidth=0.8, height=70, relx=0.1, rely=0.07)

srcFolder = tk.Button(root, text="Source Folder", fg="white", bg="#37393F", command=select_src)
srcFolder.pack()

destFolder = tk.Button(root, text="Destination Folder", fg="white", bg="#37393F", command=dst_src)
destFolder.pack()

copy = tk.Button(root, text="Copy", fg="white", bg="#37393F", command=copy)
copy.pack()

root.mainloop()
