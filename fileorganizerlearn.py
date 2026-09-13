import os
from pathlib import Path
categories = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".psd": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",

    ".mp3": "Music",
    ".wav": "Music",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pptx": "Documents",
    ".xlsx": "Documents",
    ".txt": "Documents",

    ".py": "Python",

    ".ai": "Design",
    ".htm" : "Web",
    ".html": "Web"
}
folder_location=r"C:\Users\khare\OneDrive\Pictures"
folder=Path(folder_location)
files=os.listdir(folder)
for file in files:
    extension=Path(file).suffix
    category=categories.get(extension)
    #print(file,"----",category)
    if category:
        destination_folder=folder/category
        destination_folder.mkdir(exist_ok=True)
        source_file=folder/file
        destination_file=destination_folder/file
        #source_file.rename(destination_file)
        path=Path(file)
        name=Path.stem
        counter=1
        while destination_file.exists():
            new_name=f"{name}({counter}){extension}"
            destination_file=destination_folder/new_name
            counter+=counter
        source_file.rename(destination_file)
    else:
        print(file,"----","Skipped")    