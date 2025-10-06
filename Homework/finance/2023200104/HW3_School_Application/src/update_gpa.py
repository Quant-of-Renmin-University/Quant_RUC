import json
p = r"C:\Users\32854\Desktop\quant课\HW_School_Application\personal_info.json"
with open(p,'r',encoding='utf-8-sig') as f:
    d=json.load(f)
d['gpa'] = "3.99(24-25 ACADEMIC YEAR)"
with open(p,'w',encoding='utf-8') as f:
    json.dump(d,f,ensure_ascii=False,indent=2)
print("GPA updated to", d['gpa'])
