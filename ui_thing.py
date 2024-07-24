import os
import time
import json
import customtkinter
from customtkinter import CTkFrame, CTkComboBox, CTkButton, CTkLabel
from downloads_searcher import downloads_searcher
from typing import List
from file_editor import boldifier
from option_menu import option_ui_start
import sys
from pathlib import Path

combobox_main: None = None
root: None = None

def create_config():
    try:

        program_dir: str = os.getenv("APPDATA")
        full_path: str = program_dir + "\\Boldify"

        if not os.path.exists(full_path):
            os.mkdir(full_path)

        home_dir: str = os.path.expanduser("~")
        desktop_folder: str = os.path.join(home_dir, "Desktop")
        config_file_path: str = full_path + "\\config.json"
        if not os.path.exists(config_file_path):
            config_data = {
                "Theme": "Dark",
                "SavePath": os.path.join(desktop_folder),
                "BoldColor": "Black"
            }
            with open(config_file_path, "a") as config_file:
                json.dump(config_data, config_file, indent = 4)

    except Exception as e:
        print(e)

def activate_boldify():
    short_path: str = combobox_main.get()
    for path in downloads_searcher():
        if path.__contains__(short_path):
            path_to_new: str = boldifier(path)
            os.startfile(path_to_new)
            if root:
                root.destroy()


def open_options():
    global root
    try:
        root.destroy()
        option_ui_start()
    except Exception as e:
        print(e)


def ui_start():
    global combobox_main
    global root

    #Loading the appearance from config file
    appearance_mode = None
    program_dir: str = os.getenv("APPDATA")
    full_path: str = program_dir + "\\Boldify\\config.json"
    try:
        with open(full_path, "r") as config_file:
            config_data: dict = json.load(config_file)
            appearance_mode = config_data.get("Theme")
    except FileNotFoundError as e:
        print(e)

    #Setting the Appearance
    customtkinter.set_appearance_mode(appearance_mode)

    #Root initialization
    root = customtkinter.CTk()
    root.resizable(False, False)
    root.title("Boldify v1.2")

    if getattr(sys, "frozen", False):
        icon_path = Path(sys._MEIPASS) / "boldify.ico"
        root.iconbitmap(icon_path)

    title_frame: CTkFrame = CTkFrame(root, corner_radius=10, fg_color="transparent")
    title_frame.grid(row = 0, column = 0, sticky="nsew", padx = 5, pady = 0)

    title_frame.grid_columnconfigure(0, weight=1)
    title_frame.grid_columnconfigure(1, weight=1)
    title_frame.grid_columnconfigure(2, weight=1)

    lb_title: CTkLabel = CTkLabel(title_frame, text="Boldify v1.2", font = ("Helvetica", 20))
    lb_title.grid(row = 0, column = 0, sticky="w", padx = 20, pady = 5)


    #Initialization of the Options button
    bt_options: CTkButton = CTkButton(master = title_frame, text ="Options", width = 70,
                                      command = open_options, fg_color= "#71aeeb", corner_radius=10)
    bt_options.grid(row = 0, column = 2, sticky="ne",columnspan = 1, padx = 20, pady = 10)

    #Intialization of the Main Frame
    main_frame: CTkFrame = CTkFrame(master = root, corner_radius = 10)
    main_frame.grid(row = 2, column = 0, sticky = "nsew", padx = 20, pady = 20)

    #Initialization and loading of the list for the combo box
    cb_list: List[str] = []
    for path in downloads_searcher():
        split_path = path.split("\\")
        for string in split_path:
            if string.__contains__(".docx"):
                cb_list.append(string)

    #Initialization of the Lable
    label: CTkLabel = CTkLabel(text = "Select the file that you want to boldify", master = main_frame)
    label.pack(pady = 10, padx = 20, fill = "both", expand = True)

    #Initialization of the Combo Box
    combobox_main= CTkComboBox(master = main_frame, values = cb_list, width = 250, border_color="#71aeeb", button_color="#71aeeb",
                               corner_radius=10)
    combobox_main.pack(pady = 10, padx = 20, fill = "both", expand = False)

    #Initialization of the Boldify Button
    bt_boldify: CTkButton = CTkButton(master = main_frame, text = "Boldify", command = activate_boldify, fg_color="#71aeeb",
                                      corner_radius=10)
    bt_boldify.pack(padx = 20, pady = 10, fill = "both", expand = True)

    root.mainloop()

try:
    create_config()
    ui_start()
except Exception as e:
    print(e)