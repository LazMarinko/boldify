import tkinter
from tkinter import filedialog


def dir_getter() -> str:
    root = tkinter.Tk()
    root.withdraw()
    new_save_path = filedialog.askdirectory(title=("Select new save path"))
    return new_save_path