import csv
import os
import re
from pathlib import Path

CSV_PATH = "cumplenatita - Personajes.csv"  # Nombre exacto del fichero CSV
OUTPUT_DIR = Path("_reparto")
OUTPUT_DIR.mkdir(exist_ok=True)

# Eliminar todos los archivos .md existentes antes de regenerar
for md_file in OUTPUT_DIR.glob("*.md"):
    md_file.unlink()

# Clean function from clean_csv_secreto.py

def clean_text(text):
    if not text:
        return text
    # Replace Unicode line/paragraph separators with \n
    text = re.sub(r'[\u2028\u2029\u0085]', '\n', text)
    # Replace multiple consecutive newlines with just two (markdown paragraph)
    text = re.sub(r'\n{2,}', '\n\n', text)
    # Optionally, remove other invisible characters (not recommended for Spanish)
    return text

# Campos esperados en el CSV y su orden en el front-matter
yaml_fields = [
    ("layout", lambda row, slug: "character"),
    ("permalink", lambda row, slug: f"/amigasalbordedeunataquedenervios/reparto/{slug}/"),
    ("name", lambda row, slug: row.get("name", "")),
    ("title", lambda row, slug: row.get("title", "")),
    ("actor", lambda row, slug: row.get("actor", "")),
    ("image", lambda row, slug: f"/assets/portraits/{slug}.png"),
    ("frase", lambda row, slug: row.get("frase", "")),
    ("color", lambda row, slug: row.get("color", "")),
    ("bio", lambda row, slug: row.get("bio", "")),
    ("secreto", lambda row, slug: row.get("secreto", "")),
    # Add icons field from 'final' column if present
    ("icons", lambda row, slug: ",".join(row.get("final", "").split()) if row.get("final", "").strip() else None)
]

def generate_frontmatter(row: dict) -> str:
    slug = row.get("file")
    lines = ["---"]
    for key, fn in yaml_fields:
        value = fn(row, slug)
        if value is None or value == "":
            continue
        # Aseguramos que los strings van entre comillas si contienen ':' o comienzan con #
        if isinstance(value, str) and (":" in value or value.startswith("#")):
            value = f'"{value}"'
        lines.append(f"{key}: {value}")
    lines.append("---\n")
    return "\n".join(lines)

def process_csv(csv_path: str):
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Ignorar filas vacías o separadores sin 'name'
            if not row.get("file"):
                continue
            # Clean the secreto field before writing
            if "secreto" in row:
                row["secreto"] = clean_text(row["secreto"])

            slug = row.get("file")
            md_path = OUTPUT_DIR / f"{slug}.md"

            frontmatter = generate_frontmatter(row)
            # No body, all main content in front matter
            with md_path.open("w", encoding="utf-8") as f:
                f.write(frontmatter)
            print(f"Generated {md_path}")

if __name__ == "__main__":
    process_csv(CSV_PATH) 