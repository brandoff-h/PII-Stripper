# PII Stripper

Scans a CSV file's `message_content` column for PII and splits it into two output files: one with PII rows removed and one containing only PII rows.

## Usage

```bash
python3 main.py
# Enter file name: myfile.csv          (looks in csv_files/)
# Enter file name: /full/path/to/file  (absolute path also works)
```

Input files go in `csv_files/`. Output files are written to `output/`.

## Detected PII

- Emails
- Windows usernames (`C:\Users\...`)
- Phone numbers (US formats)
- IP addresses (IPv4)

## TODO: Name Detection

Names are not currently detected. Options to implement this:

- **Hardcoded list** — maintain a list of known names in the script; fast and precise but requires manual upkeep
- **NLP / NER (spaCy)** — use `spacy` with `en_core_web_sm` to auto-detect person names; broader coverage but may produce false positives and requires installing the library
- **External name list** — load names from a `.txt` file at runtime; easier to update than hardcoding but still requires manual curation
