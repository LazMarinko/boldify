import os

import customtkinter
from customtkinter import CTkFrame, CTkComboBox, CTkButton, CTkLabel
from downloads_searcher import downloads_searcher
from typing import List
from file_editor import boldifier

combobox_main: None = None
root: None = None

def activate_boldify():
    short_path: str = combobox_main.get()
    print(short_path)
    for path in downloads_searcher():
        if path.__contains__(short_path):
            path_to_new: str = boldifier(path)
            print(path_to_new)
            os.startfile(path_to_new)
            root.destroy()




def ui_start():
    global combobox_main
    global root
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    root = customtkinter.CTk()
    root.title("Boldify")
    main_frame: CTkFrame = CTkFrame(master = root)
    main_frame.pack(pady = 50, padx = 50, fill = "both", expand = True)
    cb_list: List[str] = []
    for path in downloads_searcher():
        split_path = path.split("\\")
        for string in split_path:
            if string.__contains__(".docx"):
                cb_list.append(string)
    label: CTkLabel = CTkLabel(text = "Select the file that you want to boldify", master = main_frame)
    label.pack(pady = 10, padx = 20, fill = "both", expand = True)
    combobox_main= CTkComboBox(master = main_frame, values = cb_list, width = 250)
    combobox_main.pack(pady = 10, padx = 20, fill = "both", expand = True)
    bt_boldify: CTkButton = CTkButton(master = main_frame, text = "Make ADHD readible", command = activate_boldify)
    bt_boldify.pack(padx = 20, pady = 10, fill = "both", expand = True)
    root.mainloop()

try:
    ui_start()
except Exception as e:
    print(e)