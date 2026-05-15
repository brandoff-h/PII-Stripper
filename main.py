import csv
import re
import os

EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', re.IGNORECASE)
WINDOWS_USER_PATTERN = re.compile(r'[a-zA-Z]:\\Users\\[^\\\s"]+', re.IGNORECASE)
PHONE_PATTERN = re.compile(r'\b(\+?1[\s.\-]?)?\(?\d{3}\)?[\s.\-]?\d{3}[\s.\-]?\d{4}\b')
IP_PATTERN = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')


def contains_pii(text):
    if EMAIL_PATTERN.search(text):
        return True
    if WINDOWS_USER_PATTERN.search(text):
        return True
    if PHONE_PATTERN.search(text):
        return True
    if IP_PATTERN.search(text):
        return True
    return False


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

user_input = input("Enter file name: ").strip()
if os.path.isabs(user_input):
    input_path = user_input
else:
    input_path = os.path.join(SCRIPT_DIR, "csv_files", user_input)

filename = os.path.basename(input_path)
base, ext = os.path.splitext(filename)
output_dir = os.path.join(SCRIPT_DIR, "output")
os.makedirs(output_dir, exist_ok=True)
stripped_path = os.path.join(output_dir, f"{base}_stripped{ext}")
pii_path = os.path.join(output_dir, f"{base}_pii{ext}")

with open(input_path, "r", newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    rows_clean = []
    rows_pii = []
    for row in reader:
        content = row.get("message_content", "")
        if contains_pii(content):
            rows_pii.append(row)
        else:
            rows_clean.append(row)

with open(stripped_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_clean)

with open(pii_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_pii)

print(f"Done.")
print(f"  {len(rows_clean)} clean rows  -> {stripped_path}")
print(f"  {len(rows_pii)} PII rows    -> {pii_path}")