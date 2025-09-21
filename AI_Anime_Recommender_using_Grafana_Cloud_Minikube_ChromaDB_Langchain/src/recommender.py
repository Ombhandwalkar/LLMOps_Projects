from langchain.chains import Retrieval_QA
from langchain_graq import ChatGraq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key:str, model_name:str):
        self.llm= ChatGraq(api_key=api_key, model=model_name, temperature=0)
        self.prompt= get_anime_prompt()

        self.qa_chain= Retrieval_QA.from_chain_type(
            llm= self.llm,
            chain_type= 'stuff',
            retriever= retriever,
            return_source_documents=True,
            chain_type_kwargs= {'prompt':self.prompt}
        )

    def get_recommendation(self,query:str)->str:
        '''Get Anime recommendation based on query.'''
        try:
            result= self.qa_chain({'query':query})
            return result['result']
        except Exception as e:
            return f"Error generating recommendation {e}"
            