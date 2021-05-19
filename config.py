import os

from dotenv import load_dotenv


load_dotenv()

DEBUG = os.getenv("DEBUG") == "True"
BANK_BASE_API_URL = os.getenv('BANK_BASE_API_URL')
