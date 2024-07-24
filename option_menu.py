import os
import json
import sys
import tkinter
from pathlib import Path

import customtkinter
from customtkinter import CTkFrame, CTkComboBox, CTkButton, CTkLabel, CTkEntry
from typing import List
from options_function import dir_getter

root = None
cb_theme = None
current_appearance = None
current_path = None
e_path = None
current_bold_color = None
cb_color = None
def browse_function():
    global e_path
    current_path = dir_getter()
    e_path.delete(0, tkinter.END)
    e_path.insert(0, current_path)

def apply_function():
    global current_appearance, current_path, e_path, current_bold_color
    current_appearance = cb_theme.get()
    current_bold_color = cb_color.get()
    if e_path.get():
        current_path = e_path.get()
    else:
        try:
            program_dir: str = os.getenv("APPDATA")
            full_path = program_dir + "\\Boldify\\config.json"
            with open(full_path, "r") as config_file:
                config = json.load(config_file)
                current_path = config.get("SavePath")
        except Exception as e:
            print(e)
    new_config = {
        "Theme" : current_appearance,
        "SavePath": current_path,
        "BoldColor": current_bold_color
    }
    try:
        program_dir: str = os.getenv("APPDATA")
        full_path = program_dir + "\\Boldify\\config.json"
        with open(full_path, "w") as config_file:
            json.dump(new_config, config_file, indent=4)
        root.destroy()
        from ui_thing import ui_start
        ui_start()
    except Exception as e:
        print(e)

def option_ui_start():
    global current_appearance
    global current_path
    global e_path, cb_theme, root, current_bold_color, cb_color

    try:
        program_dir: str = os.getenv("APPDATA")
        full_path = program_dir + "\\Boldify\\config.json"
        with open(full_path, "r") as config_file:
            config = json.load(config_file)
            current_appearance = config.get("Theme")
            current_path = config.get("SavePath")
            current_bold_color = config.get("BoldColor")
    except Exception as e:
        print(e)

    customtkinter.set_appearance_mode(current_appearance)


    root = customtkinter.CTk()
    root.resizable(False, False)
    root.title("Options")
    if getattr(sys, "frozen", False):
        icon_path = Path(sys._MEIPASS) / "boldify.ico"
        root.iconbitmap(icon_path)

    theming_frame = CTkFrame(root, fg_color = "transparent")
    theming_frame.grid(row = 0, column = 0, sticky = "nsew", padx = 10, pady = 5)

    lb_theming: CTkLabel = CTkLabel(theming_frame, text="Theming", font = ("Helvetica", 17))
    lb_theming.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 0)

    top_grid: CTkFrame = CTkFrame(master = root, corner_radius = 10)
    top_grid.grid(row = 1, column = 0, sticky = "nsew", padx = 10, pady = 5)

    location_frame: CTkFrame = CTkFrame(master = root, fg_color = "transparent")
    location_frame.grid(row = 2, column = 0, sticky = "nsew", padx = 10, pady = 5)

    lb_location: CTkLabel = CTkLabel(master = location_frame, text ="Save location", font = ("Helvetica", 17))
    lb_location.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 0)

    grid_main: CTkFrame = CTkFrame(master=root, corner_radius=15)
    grid_main.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

    lb_theme: CTkLabel = CTkLabel(master = top_grid, text = "Theme: ")
    lb_theme.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)

    cb_theme_list: List[str] = ["Light", "Dark"]
    cb_theme = CTkComboBox(master = top_grid,values = cb_theme_list, corner_radius = 10,
                                    button_color= "#71aeeb", border_color="#71aeeb")
    cb_theme.set(current_appearance)
    cb_theme.grid(row = 0, column = 1, sticky = "e", padx = 5, pady = 5)

    lb_path: CTkLabel = CTkLabel(master = grid_main, text = "The Location of the saved .docx files")
    lb_path.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 5)

    e_path= CTkEntry(master = grid_main, placeholder_text = current_path, width = 200)
    e_path.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 5)

    bt_browse: CTkButton = CTkButton(master = grid_main, text = "Browse", fg_color="#71aeeb", command=browse_function)
    bt_browse.grid(row = 1, column = 1, sticky = "w", padx = 10, pady = 5)

    bottom_frame: CTkFrame = CTkFrame(root, fg_color= "transparent", corner_radius= 10)
    bottom_frame.grid(row = 6, column = 0, sticky = "s", padx = 10, pady = 20)

    bt_apply: CTkButton = CTkButton(master = bottom_frame, text = "Apply", fg_color="#71aeeb", command=apply_function)
    bt_apply.grid(row = 0, column = 1,columnspan = 5 ,sticky = "ew", padx = 10, pady = 5)

    bold_color_title_frame: CTkFrame = CTkFrame(root, fg_color= "transparent")
    bold_color_title_frame.grid(row = 4, column = 0, sticky = "nsew", padx = 10, pady =5)

    lb_color_title: CTkLabel = CTkLabel(bold_color_title_frame, text = "Bold Letter Color",
                                        font = ("Helvetica", 17))
    lb_color_title.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 5)

    bold_color_frame: CTkFrame = CTkFrame(root, corner_radius = 15)
    bold_color_frame.grid(row = 5, column =0, sticky = "nsew", padx = 10, pady = 5)

    lb_color: CTkLabel = CTkLabel(bold_color_frame, text = "The color of the bolded letters: ")
    lb_color.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 5)

    cb_color_list: List[str] = ["Black", "Dark Blue"]

    cb_color = CTkComboBox(bold_color_frame, values =cb_color_list, corner_radius = 10,
                                    button_color= "#71aeeb", border_color="#71aeeb")
    cb_color.set(current_bold_color)
    cb_color.grid(row = 0, column = 1, sticky = "w", padx = 10, pady = 5)

    try:
        root.mainloop()
    except Exception as e:
        print(e)
