from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from flipkart.data_converter import DataConverter
from flipkart.config import Config
from utils.logger import get_logger

logging= get_logger(__name__)


class DataIngestor:
    def __init__(self):
        self.embeddingg= HuggingFaceEmbeddings(model= Config.EMBEDDING_MODEL)

        self.vstore= AstraDBVectorStore(
            embedding= self.embeddingg,
            collection_name= 'flipkart_database',
            api_endpoint= Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace= Config.ASTRA_DB_KEYSPACE
        )

    def data_ingestion(self, load_existing=True):
        try:
            if load_existing==True:
                return self.vstore
            
            docs = DataConverter('data/flipkart_product_review.csv').convert()
            self.vstore.add_documents(docs)
            logging.info('Data Ingested sucessfully')
            return self.vstore
        except Exception as e:
            logging.error('Failed to Ingestion.')
            raise 