# Nicholas Norman March 2026

from tkinter import *
from tkinter import ttk, filedialog
import gradeview

root = Tk()
frm = ttk.Frame(root, padding=10)

root.title("Gradeview")

inputURL = "./in/4/"

def open_in_folder():
    global inputURL
    inputURL = filedialog.askdirectory()
    output.config(text=f"Folder selected: {inputURL}")

def run_gradeview():
    
    if (inputURL == ""):
        output.config(text="Please select input folder.")
    
    else:
        root.destroy()
        gradeview.generate_files(inputURL)
        gradeview.setupServer()

root.minsize(300,0)
frm.pack()
ttk.Button(frm, text="Select Input Folder", command=open_in_folder).pack()
ttk.Button(frm, text="Run Gradeview", command=run_gradeview).pack()
output = ttk.Label(frm, text="")
output.pack()

root.mainloop()