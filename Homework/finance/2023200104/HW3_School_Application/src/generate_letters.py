from pathlib import Path
import pandas as pd
import json
from datetime import date
from docxtpl import DocxTemplate
import os

# Try to import docx2pdf; skip PDF if not available or Word not installed
try:
    from docx2pdf import convert as docx2pdf_convert
    DOCX2PDF_AVAILABLE = True
except Exception:
    DOCX2PDF_AVAILABLE = False

base = Path(__file__).resolve().parents[1]
output_dir = base / 'output' / 'letters'
output_dir.mkdir(parents=True, exist_ok=True)

# Load config
with open(base / 'personal_info.json', 'r', encoding='utf-8-sig') as f:
    personal = json.load(f)

# Load lists
uni_df = pd.read_excel(base / 'data' / 'universities.xlsx')
area_df = pd.read_excel(base / 'data' / 'research_areas.xlsx')
journals_df = pd.read_excel(base / 'data' / 'top_journals.xlsx')
skills_df = pd.read_excel(base / 'data' / 'skills.xlsx')

skills_str = ', '.join(skills_df['skill'].tolist())

# Template
tpl_path = base / 'template' / 'application_template.docx'
tpl = DocxTemplate(str(tpl_path))

count = 0
first_docx = None
for _, uni_row in uni_df.iterrows():
    for _, area_row in area_df.iterrows():
        uni = uni_row['university_name']
        area = area_row['research_area']
        top_journals = journals_df[journals_df['research_area'] == area]['journal_name'].tolist()
        top_journals_str = ', '.join(top_journals)
        context = {
            'today': date.today().isoformat(),
            'applicant_name': personal['applicant_name'],
            'email': personal['email'],
            'phone': personal['phone'],
            'current_university': personal['current_university'],
            'degree': personal['degree'],
            'gpa': personal['gpa'],
            'university_name': uni,
            'research_area': area,
            'top_journals_str': top_journals_str,
            'skills_str': skills_str,
            'background_summary': personal['background_summary'],
        }
        tpl.render(context)
        safe_uni = uni.replace(' ', '_').replace('/', '-')
        safe_area = area.replace(' ', '_')
        out_path = output_dir / f"SOP_{safe_uni}_{safe_area}.docx"
        tpl.save(str(out_path))
        if first_docx is None:
            first_docx = out_path
        count += 1

print(f"Generated {count} Word documents at: {output_dir}")

# Convert first docx to PDF as sample
if DOCX2PDF_AVAILABLE and first_docx is not None:
    pdf_path = output_dir / (first_docx.stem + '.pdf')
    try:
        docx2pdf_convert(str(first_docx), str(pdf_path))
        print(f"Sample PDF generated: {pdf_path}")
    except Exception as e:
        print(f"docx2pdf conversion skipped due to error: {e}")
else:
    print("docx2pdf not available or Word not installed; skipping PDF generation.")

