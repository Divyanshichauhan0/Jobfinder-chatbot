import re

def extract_intent(text):
    intent = {'what': '', 'where': '', 'salary_min': None, 'salary_max': None}
    text = text.lower()

    # Job keyword
    match_job = re.search(r'\b(driver|plumber|electrician|sales|python)\b', text)
    if match_job:
        intent['what'] = match_job.group(1)

    # Location
    match_loc = re.search(r'in\s+(\w+)', text)
    if match_loc:
        intent['where'] = match_loc.group(1)

    # Salary
    match_sal = re.search(r'(\d{3,6})\s*(inr|₹)?', text)
    if match_sal:
        sal = int(match_sal.group(1))
        intent['salary_min'] = int(sal * 0.8)
        intent['salary_max'] = int(sal * 1.2)

    return intent
