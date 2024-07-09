import os
from docx.shared import RGBColor
from docx import Document
from typing import List


def boldifier(path: str) -> str:
    color: RGBColor = RGBColor(8, 90, 195)
    doc: Document = Document(path)
    for para in doc.paragraphs:
        lines: List[str] = para.text.split('\n')
        para.clear()
        for line in lines:
            words: List[str] = line.split(" ")
            for word in words:
                word_half1: str = ""
                word_half2: str = ""
                for index, char in enumerate(word):
                    if index < len(word) / 2:
                        word_half1 += char
                    else:
                        word_half2 += char

                run1 = para.add_run(word_half1)
                run1.bold = True
                run1.font.color.rgb = color
                run2 = para.add_run(word_half2 + " ")

    path_split = path.split("\\")
    new_path: str = ""
    for string in path_split:
        if string.__contains__(".docx"):
            new_path += string
    home_dir: str = os.path.expanduser("~")
    desktop_folder: str = os.path.join(home_dir, "Desktop")
    doc.save(desktop_folder + "\\boldified " + new_path)
    return desktop_folder + "\\boldified " + new_path