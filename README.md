🧠 Jobfinder Chatbot Backend
A real-world, agentic AI-powered backend that connects informal workers to live job listings via a conversational chatbot—complete with PDF parsing, NLP, WhatsApp notifications, and scalable IBM Cloud deployment.

⚒️ Technologies Used
Python + Flask — RESTful backend and chatbot logic

Adzuna API — Real-time job scraping

PDF Parsing (PyMuPDF / pdfminer) — Resume insights

Natural Language Processing (spaCy / NLTK) — Smart intent and keyword handling

MongoDB — Job listing and resume storage

IBM Cloud Code Engine — Containerized deployment

watsonx.ai Studio — Agentic AI orchestration

WhatsApp Notification (Twilio or similar) — Real-time user updates

🚀 Features
🗣️ NLP-driven job matching via chat

📄 PDF resume upload and parsing

📡 Real-time scraping of job postings

🔒 MongoDB-based persistent storage

📲 WhatsApp notifications for new matches

🛠️ Modular backend with agentic action endpoints

☁️ Seamless IBM Cloud deployment with CLI integration

📦 Setup Instructions
1. Clone the repo
bash
git clone https://github.com/Divyanshichauhan0/Jobfinder-chatbot.git
cd Jobfinder-chatbot
2. Create a virtual environment
bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
3. Install dependencies
bash
pip install -r requirements.txt
4. Configure environment variables
Create a .env file and include:

bash
ADZUNA_API_KEY=your_key
MONGO_URI=your_mongo_uri
WHATSAPP_TOKEN=your_token
FLASK_SECRET=your_flask_secret
🧠 How It Works
User uploads resume → parsed and stored

Chatbot receives user queries via Watsonx Assistant

Adzuna API fetches job listings based on parsed skills and query intent

Agentic AI filters, matches, and routes job data

WhatsApp / Chatbot sends job matches to user

🧪 Local Development
bash
flask run
Visit http://localhost:5000 to test endpoints.

🚀 Deployment Notes
Connect repo to IBM Cloud Code Engine

Use ibmcloud CLI for container deployment

Structure endpoint routing for agentic tool-calling

Link MongoDB Atlas if needed with secured API access

🤝 Contribution
Pull requests welcome! For feature ideas or bug reports, open an issue or reach out via GitHub discussions.
