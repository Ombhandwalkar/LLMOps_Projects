from langchain_core.messages import HumanMessage, AIMessage
from utils.custom_exception import CustomException
from utils.logger import get_logger
from src.chains.itineary_chain import generate_itineary

logger= get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=''
        self.intrests=[]
        self.itineary= ''

        logger.info('Initialized logger instance')

    def set_city(self, city:str):
        try:
            self.city= city
            self.messages.append(HumanMessage(content=city))
            logger.info('City set sucessfully')

        except Exception as e:
            logger.error(f" Error while seting city: {e}")
            raise CustomException(f'Failed to set city',e)
        
    def set_intrests(self, intrests_str:str):
        try:
            self.intrests = [i.strip() for i in intrests_str.split(',')]
            self.messages.append(HumanMessage(content=intrests_str))
            logger.info('Intrests set sucessfully..')
        except Exception as e:
            logger.error(f"Failed to set intrests: {e}")
            raise CustomException("Failed to set intrests",e)
        
    def create_itineary(self):
        try:
            logger.info(f" Generating itineary for {self.city} for intrests: {self.intrests}")
            itineary= generate_itineary(self.city, self.intrests)
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary))
            logger.info('Itineary generated sucessfully.')
            return itineary
        except Exception as e:
            logger.error(f"Failed to generate itineary: {e}")
            raise CustomException('Failed to generate itineary',e)
        