import csv
import re

infile = 'cumplenatita - Personajes.csv'
outfile = 'cumplenatita - Personajes_clean.csv'

def clean_text(text):
    if not text:
        return text
    # Replace Unicode line/paragraph separators with \n
    text = re.sub(r'[\u2028\u2029\u0085]', '\n', text)
    # Replace multiple consecutive newlines with just two (markdown paragraph)
    text = re.sub(r'\n{2,}', '\n\n', text)
    # Optionally, remove other invisible characters (not recommended for Spanish)
    return text

with open(infile, newline='', encoding='utf-8') as inf, \
     open(outfile, 'w', newline='', encoding='utf-8') as outf:
    reader = csv.DictReader(inf)
    writer = csv.DictWriter(outf, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
        row['secreto'] = clean_text(row['secreto'])
        writer.writerow(row) 