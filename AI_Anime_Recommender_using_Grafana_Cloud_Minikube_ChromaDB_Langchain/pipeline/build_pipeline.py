from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()
logger= get_logger(__name__)


def main():
    try:
        logger.info('Starting Pipeling...')

        loader= AnimeDataLoader('data/anime_with_synopsis.csv','data/anime_update.csv')
        processed_data= loader.load_and_process()
        logger.info('Data loaded and processed')

        vecotr_builder= VectorStoreBuilder(processed_data)
        vecotr_builder.build_and_save_vectorstore()
        logger.info('Vector store build sucessfully')

    except Exception as e:
        logger.error(f"Failed to execute pipeline {e}")
        raise CustomException('Error during pipeline',e)

if __name__=='__main__':
    main()