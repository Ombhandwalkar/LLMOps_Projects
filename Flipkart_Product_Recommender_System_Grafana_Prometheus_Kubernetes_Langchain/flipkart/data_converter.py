import pandas as pd
from langchain_core.documents import Document
from utils.logger import get_logger

logging= get_logger(__name__)

class DataConverter:
    def __init__(self, file_path:str):
        self.file_path= file_path

    def convert(self):
        try:
            df= pd.read_csv(self.file_path)[['product_title','review']]

            docs= [
                Document(page_content=row['review'], metadata= {'product_name':row['product_title']})
                for _, row in df.iterrows()
                  ]
            logging.info(f'Data loaded sucessfully from {self.file_path}')
            return docs
        except Exception as e:
            logging.error('Failed to load the data')
            raise 
            