import requests
from config import ADZUNA_APP_ID, ADZUNA_APP_KEY


def scrape_jobs(intent):
    APP_ID = "15be545d"
    APP_KEY = "d4aad047385a33c9632a41a4f44e9b55	"
    base_url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'what': intent.get('what', ''),
        'where': intent.get('where', ''),
    }

    if intent.get('salary_min'):
        params['salary_min'] = intent['salary_min']
    if intent.get('salary_max'):
        params['salary_max'] = intent['salary_max']

    response = requests.get(base_url, params=params)
    return response.json().get('results', [])
