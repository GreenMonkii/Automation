# Python CLI program to organize files in a directory to subdirectories based on file type

from rich import print
from rich.prompt import Prompt
import os
import shutil
from pathlib import Path

EXTENSION_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".webm", ".flv", ".avi"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xlsx", ".xls"],
    "Music": [".mp3", ".wav", ".flac", ".ogg"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
}


def organize_files(input_dir, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)

        for root, _, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = Path(file).suffix

                for category, extensions in EXTENSION_MAPPING.items():
                    if file_extension in extensions:
                        category_dir = os.path.join(output_dir, category)
                        os.makedirs(category_dir, exist_ok=True)
                        shutil.move(file_path, category_dir)
                        print(f"Moved {file} to {category} directory.")
                        break
                else:
                    other_dir = os.path.join(output_dir, "Others")
                    os.makedirs(other_dir, exist_ok=True)
                    shutil.move(file_path, other_dir)
                    print(f"Moved {file} to Others directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        input_dir = Prompt.ask("Enter input directory:", default=".")
        output_dir = Prompt.ask("Enter output directory:", default=input_dir)

        organize_files(input_dir, output_dir)
        print("Files organized successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
