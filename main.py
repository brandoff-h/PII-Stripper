import csv
import re

EMAIL_PATTERN = re.compile(r"\"?[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}\"?")
WINDOWS_FILE_PATTERN = re.compile(r"\"?[a-zA-Z]:\\Users\\[^\\]+\\?\"?")



file_path = input("Enter file name: ")
with open(f"csv_files/{file_path}", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        pass

