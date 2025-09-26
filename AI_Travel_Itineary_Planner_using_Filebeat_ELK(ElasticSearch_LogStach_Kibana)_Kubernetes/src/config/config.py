import os 
from dotenv import load_dotenv
load_dotenv()

# Calling the GROQ API
GROQ_API_KEY= os.getenv('GROQ_API_KEY')