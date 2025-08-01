from flask import Flask, request, jsonify
from utils.scraper import scrape_jobs
from utils.pdf_parser import extract_text_from_pdf
from utils.nlp_engine import match_skills
from utils.notifier import send_whatsapp_notification
from utils.input_parser import extract_intent

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match_jobs():
    data = request.get_json()
    user_text = data['query']  # e.g. "Show jobs in Delhi for plumbers around ₹5000"

    intent = extract_intent(user_text)
    jobs = scrape_jobs(intent)

    if 'phone' in data:
        send_whatsapp_notification(data['phone'], jobs)

    return jsonify({'status': 'success', 'query': intent, 'jobs': jobs})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
