from pathlib import Path
import pandas as pd

base = Path(__file__).resolve().parents[1]

# Universities: 10 from top30, 10 from top60, 10 from top90 (curated static list)
universities = [
    # Top 30 (10)
    ('Harvard University', 'top30'), ('Massachusetts Institute of Technology', 'top30'), ('Stanford University', 'top30'),
    ('University of Chicago', 'top30'), ('Princeton University', 'top30'), ('University of California, Berkeley', 'top30'),
    ('Yale University', 'top30'), ('Columbia University', 'top30'), ('New York University', 'top30'), ('Northwestern University', 'top30'),
    # Top 60 (10)
    ('University of Michigan', 'top60'), ('Duke University', 'top60'), ('University of Pennsylvania', 'top60'), ('Cornell University', 'top60'),
    ('University of California, Los Angeles', 'top60'), ('University of WisconsinMadison', 'top60'), ('Boston University', 'top60'),
    ('University of California, San Diego', 'top60'), ('Brown University', 'top60'), ('University of Maryland', 'top60'),
    # Top 90 (10)
    ('Ohio State University', 'top90'), ('University of Arizona', 'top90'), ('University of Colorado Boulder', 'top90'),
    ('Indiana University', 'top90'), ('University of Pittsburgh', 'top90'), ('University of Rochester', 'top90'),
    ('University of Iowa', 'top90'), ('Texas A&M University', 'top90'), ('University of Virginia', 'top90'), ('University at Buffalo', 'top90'),
]

Path(base / 'data').mkdir(parents=True, exist_ok=True)
pd.DataFrame(universities, columns=['university_name', 'tier']).to_excel(base / 'data' / 'universities.xlsx', index=False)

# Research areas (3)
research_areas = ['Economics', 'Finance', 'Management']
pd.DataFrame(research_areas, columns=['research_area']).to_excel(base / 'data' / 'research_areas.xlsx', index=False)

# Top journals per area (3 each)
journals = [
    ('Economics', 'American Economic Review'), ('Economics', 'Econometrica'), ('Economics', 'Quarterly Journal of Economics'),
    ('Finance', 'Journal of Finance'), ('Finance', 'Review of Financial Studies'), ('Finance', 'Journal of Financial Economics'),
    ('Management', 'Academy of Management Journal'), ('Management', 'Academy of Management Review'), ('Management', 'Strategic Management Journal'),
]
pd.DataFrame(journals, columns=['research_area', 'journal_name']).to_excel(base / 'data' / 'top_journals.xlsx', index=False)

# Skills (example list from typical job postings)
skills = ['Python', 'R', 'Stata', 'SQL', 'Econometrics', 'Machine Learning', 'Data Analysis', 'Communication', 'LaTeX']
pd.DataFrame(skills, columns=['skill']).to_excel(base / 'data' / 'skills.xlsx', index=False)
