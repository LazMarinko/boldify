import os
import glob
from typing import List

def downloads_searcher():
    home_dir: str = os.path.expanduser("~")
    downloads_folder: str = os.path.join(home_dir, "Downloads")

    docx_files: List[str] = []

    search_pattern: str = os.path.join(downloads_folder, "*.docx")
    for file_path in glob.glob(search_pattern):
        docx_files.append(file_path)

    return docx_files

