import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from a .env file (optional)

# Twilio creds
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
WHATSAPP_FROM = os.getenv("WHATSAPP_FROM")

# Adzuna API creds
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

# MongoDB URI (if using DB)
MONGO_URI = os.getenv("MONGO_URI")
