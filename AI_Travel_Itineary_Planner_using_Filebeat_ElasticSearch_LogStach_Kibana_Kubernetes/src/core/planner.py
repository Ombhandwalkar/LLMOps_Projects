from langchain_core.messages import HumanMessage, AIMessage
from src.utils.custom_exception import CustomException
from src.utils.logger import get_logger
from src.chains.itinerary_chain import generate_itinerary

logger= get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=''
        self.interests=[]
        self.itinerary= ''

        logger.info('Initialized logger instance')

    def set_city(self, city:str):
        try:
            self.city= city
            self.messages.append(HumanMessage(content=city))
            logger.info('City set sucessfully')

        except Exception as e:
            logger.error(f" Error while seting city: {e}")
            raise CustomException(f'Failed to set city',e)
        
    def set_intrests(self, interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(',')]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info('Interests set sucessfully..')
        except Exception as e:
            logger.error(f"Failed to set interests: {e}")
            raise CustomException("Failed to set interests",e)
        
    def create_itinerary(self):
        try:
            logger.info(f" Generating itinerary for {self.city} for intrests: {self.interests}")
            itinerary= generate_itinerary(self.city, self.interests)
            self.itinerary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info('Itinerary generated sucessfully.')
            return itinerary
        except Exception as e:
            logger.error(f"Failed to generate itinerary: {e}")
            raise CustomException('Failed to generate itinerary',e)
        