import os
from src.config.settings import settings
from langchain_groq import ChatGroq


def get_groq_llm():
    return ChatGroq(
        model= settings.MODEL_NAME,
        api_key= settings.GROQ_API_KEY,
        temperature= settings.TEMPERATURE
    )