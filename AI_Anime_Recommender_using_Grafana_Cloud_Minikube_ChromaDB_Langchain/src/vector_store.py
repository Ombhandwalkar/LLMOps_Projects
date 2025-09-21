from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logging= get_logger(__name__)


class VectorStoreBuilder:
    def __init__(self, csv_path:str, persist_dir:str='chroma_df', chunk_size:int=1000, chunk_overlap:int=100, metadata_cloumns:list=None):
        self.csv_path=csv_path
        self.persist_dir= persist_dir
        self.chunk_size=chunk_size
        self.chunk_overlap= chunk_overlap
        self.metadata_columns= metadata_cloumns
        self.embedding= HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

    def build_and_save_vectorstore(self)->None:
        """Load CSV, split, buld the file into VectorStore"""
        try:
            logging.info(f'Loading CSV from {self.csv_path}')

            loader=CSVLoader(
                file_path=self.csv_path,
                encoding='utf-8',
                metadata_columns=self.metadata_columns
            )
            data= loader.load()
            logging.info(f"Loaded {len(data)} documents from CSV")

            splitter= CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
            texts= splitter.split_documents(data)
            logging.info(f"Split documents into {len(texts)} chunks")

            db= Chroma.from_documents(texts, self.embedding, persist_directory=self.persist_dir)
            db.persist()
            logging.info(f"Vector store persisted as {self.persist_dir}")
        except Exception as e:
            logging.error(f"Failed to build vector store: {e}")
            raise

    def load_vector_store(self)->Chroma:
        """Load Chroma"""
        try:
            logging.info(f"Loading vector store from {self.persist_dir}")
            return Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding)
        except Exception as e:
            logging.error(f"Failed to load vector store {e}")
            raise