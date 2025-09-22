from src.recommender import AnimeRecommender
from src.vector_store import VectorStoreBuilder
from config.config import GRAQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()
logger= get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir='chroma_db'):
        try:
            logger.info('Initializing the Recommendation pipeline')

            vector_builder= VectorStoreBuilder(csv_path='',persist_dir=persist_dir)
            retriever= vector_builder.load_vector_store().as_retriever()

            self.recommender= AnimeRecommender(retriever, GRAQ_API_KEY, MODEL_NAME)
            logger.info('Pipeline initilized sucessfully.')

        except Exception as e:
            logger.error(f'Failed to initialized pipeline {e}')
            raise CustomException('Error during pipeline initilaization',e)
        
    def recommend(self, query:str)-> str:
        try:
            logger.info('Query received')

            recommendation= self.recommender.get_recommendation(query)
            
            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)
        


        