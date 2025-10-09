import pandas as pd
import os
from docxtpl import DocxTemplate

univ_file = "经济学系排名30所大学名单.xlsx"
fields_file = "感兴趣的领域.xlsx"
template_file = "申请信模版.docx"
output_dir = "HW_School_Application"

os.makedirs(output_dir, exist_ok=True)

univ_df = pd.read_excel(univ_file)
universities = univ_df.iloc[:, 0].tolist()

fields_df = pd.read_excel(fields_file)
fields = fields_df.iloc[:, 0].tolist()
journals = fields_df.iloc[:, 1:4].values.tolist()
skills = fields_df.iloc[:, 4].tolist()
docx_template = DocxTemplate(template_file)
count = 0
for school in universities:
    for field_idx, field in enumerate(fields):
        journal_list = journals[field_idx]
        skill_list = skills[field_idx].split("、")
        context = {
            "SchoolName": school,
            "ProgramName": "Master's Program",
            "researchfield": field,
            "Papera": journal_list[0],
            "Paperb": journal_list[1],
            "Paperc": journal_list[2],
            "skills": ", ".join(skill_list),
        }
        docx_template.render(context)
        outfile = f"{output_dir}/Application_{school.replace(' ', '_')}_{field}.docx"
        docx_template.save(outfile)
        count += 1

print(f"成功生成{count}份申请信Word文件。")
