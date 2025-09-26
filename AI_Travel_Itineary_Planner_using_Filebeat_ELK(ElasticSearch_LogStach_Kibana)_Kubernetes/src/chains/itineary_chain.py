from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config.config import GROQ_API_KEY

# Initiate the LLM
llm= ChatGroq(groq_api_key=GROQ_API_KEY, model_name='llama-3.3-70b-versatile', temperature=0.3)

# Creating Prompt
itnieary_prompt= ChatPromptTemplate([
    ('system',"You are a helpful travel asssistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"),
    ("human",'Create a itineary for my day trip')
])

 # Create function to return actual content
def generate_itineary(city:str, intrests:list[str])-> str:
    response = llm.invoke(itnieary_prompt.format_messages(city=city, intrests=', '.join(intrests)))
    return response.content