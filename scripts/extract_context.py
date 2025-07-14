import csv

infile = 'cumplenatita - Personajes.csv'
outfile = 'context'

with open(infile, encoding='utf-8') as inf, open(outfile, 'w', encoding='utf-8') as outf:
    reader = csv.DictReader(inf)
    outf.write('# Character Context for Final Scene\n\n')
    for row in reader:
        outf.write(f'- name: {row["name"]}\n')
        outf.write(f'  title: {row["title"]}\n')
        outf.write(f'  actor: {row["actor"]}\n')
        outf.write(f'  bio: {row["bio"]}\n')
        outf.write(f'  secreto: {row["secreto"]}\n\n') 