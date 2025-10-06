import json
p = r"C:\\Users\\32854\\Desktop\\quant课\\HW_School_Application\\personal_info.json"
with open(p,'r',encoding='utf-8-sig') as f:
    d=json.load(f)
d.update({
    "recommender_name_en": "Lei Ge",
    "recommender_name_cn": "葛雷",
    "recommender_title": "EnnGroup Assistant Professor in Quantitative Economics",
    "recommender_affiliation": "Renmin University of China",
    "recommender_email": d.get("recommender_email", ""),
    "recommender_phone": d.get("recommender_phone", ""),
})
with open(p,'w',encoding='utf-8') as f:
    json.dump(d,f,ensure_ascii=False,indent=2)
print("Updated recommender fields in personal_info.json")
