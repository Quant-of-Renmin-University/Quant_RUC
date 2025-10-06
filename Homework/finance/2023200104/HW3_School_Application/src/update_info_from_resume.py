import re, json, os
from pdfminer.high_level import extract_text

resume_path = r"C:\Users\32854\Desktop\quant课\吴昭毅简历2025更新（25暑假）Latest.pdf"
base = r"C:\Users\32854\Desktop\quant课\HW_School_Application"
json_path = os.path.join(base, "personal_info.json")

# Safe load existing info
info = {}
try:
    with open(json_path, 'r', encoding='utf-8-sig') as f:
        info = json.load(f)
except Exception:
    info = {}

# Defaults from user message
name_cn_default = "吴昭毅"
name_en_default = "Wuzhaoyi (Jeffri) Wu"
email_default = "3285448436@qq.com"
phone_default = "16688308888"
gpa_default = "3.99(24-25 ACADEMIC YEAR)"
major_default = "Financial Engineering"

text = ""
try:
    text = extract_text(resume_path) or ""
except Exception:
    text = ""

# Helpers
def find_one(pattern, text):
    m = re.search(pattern, text, flags=re.IGNORECASE)
    return m.group(1) if m else None

email = find_one(r"([\w\.-]+@[\w\.-]+\.[A-Za-z]{2,})", text) or info.get('email') or email_default
phone = find_one(r"(1[3-9]\d{9})", text) or info.get('phone') or phone_default
# GPA patterns: GPA x.xx or Chinese 绩点 x.xx
gpa = None
m = re.search(r"(?:GPA|绩点)[^\d]*(\d(?:\.\d{1,2})?)", text, flags=re.IGNORECASE)
if m:
    gpa = m.group(1)
if not gpa:
    gpa = str(info.get('gpa') or gpa_default)

# Major detection
major = None
if re.search(r"金融工程", text):
    major = "Financial Engineering"
elif re.search(r"Financial\s*Engineering", text, flags=re.IGNORECASE):
    major = "Financial Engineering"
if not major:
    major = info.get('major') or major_default

# University detection (first occurrence of '大学' or 'University')
current_university = info.get('current_university')
if not current_university:
    m_uni_cn = re.search(r"([\u4e00-\u9fa5]{2,}大学)", text)
    m_uni_en = re.search(r"([A-Z][A-Za-z&\-\s]+University)", text)
    current_university = (m_uni_cn.group(1) if m_uni_cn else (m_uni_en.group(1) if m_uni_en else info.get('current_university')))

# Degree detection
degree = info.get('degree')
if not degree:
    if re.search(r"硕士|Master", text, flags=re.IGNORECASE):
        degree = "Bachelor to Master applicant"
    elif re.search(r"本科|Bachelor", text, flags=re.IGNORECASE):
        degree = "Bachelor"
    else:
        degree = info.get('degree') or "Bachelor"

# Name detection (prefer provided)
applicant_name = info.get('applicant_name') or name_en_default
name_cn = info.get('name_cn') or name_cn_default
name_en = info.get('name_en') or name_en_default

# Background summary
background_summary = info.get('background_summary')
if not background_summary:
    if re.search(r"量化|quant|trading|交易", text, flags=re.IGNORECASE):
        background_summary = "Quantitative trading and research experience; strong programming and data analysis."
    else:
        background_summary = "Strong quantitative background in finance and computing, with research experience."

# Persist back
new_info = {
    'applicant_name': applicant_name,
    'email': email,
    'phone': phone,
    'current_university': current_university or info.get('current_university') or '',
    'degree': degree,
    'gpa': gpa,
    'background_summary': background_summary,
    # Keep extended fields for recommendation
    'name_cn': name_cn,
    'name_en': name_en,
    'major': major,
}

os.makedirs(base, exist_ok=True)
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(new_info, f, ensure_ascii=False, indent=2)
print("Updated personal_info.json with:")
for k, v in new_info.items():
    print(f"  {k}: {v}")
