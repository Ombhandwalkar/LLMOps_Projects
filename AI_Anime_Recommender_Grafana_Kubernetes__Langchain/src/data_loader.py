import pandas as pd
from typing import List, Set, Optional
from utils.logger import get_logger

logger = get_logger(__name__)

class AnimeDataLoader:
    def __init__(self, original_csv:str, processed_csv: str, encoding:str='utf=8', delimiter:str=',', required_cols: Optional[Set[str]]=None):
        self.original_csv= original_csv
        self.processed_csv= processed_csv
        self.encoding= encoding
        self.delimiter= delimiter
        self.required_cols= required_cols or {'Name','Genres','Sypnosis'}
    
    def load_and_process(self) -> pd.DataFrame:
        """Load the dataset from CSV"""
        try:
            logger.info(f"Loading dataset from {self.original_csv}")

            df = pd.read_csv(self.original_csv ,encoding=self.encoding,delimiter=self.delimiter, on_bad_lines='skip').dropna()
            logger.info(f"Loaded {len(df)} rows")
            return df
        except Exception as e:
            logger.error(f"Failed to load CSV: {e}")
            required_cols={'Name', 'Genres','Sypnosis'}
            raise
    
    def validate_column(self, df:pd.DataFrame)-> None:
        """Validate required columns"""
        missing= self.required_cols - self(df.columns)

        if missing:
            logger.error(f"Missing columns: {missing}")
            raise ValueError(f"Missing columns in CSV file: {missing}")
        logger.info('All required columns are present in the DataFrame')

    def process_data(self, df:pd.DataFrame)-> pd.DataFrame:
        """Create a combined column info """
        logger.info('Processing dataset')
        df= df.dropna(subset=self.required_cols)
        df['combined_info'] =( 'Title:' + df['Name'] + 'Overview:' + df['sypnosis' + 'Genres: '+ df['Genres']] )
        logger.info('Processing completed')
        return df[['combined_info']]
    
    def save_data(self,df:pd.DataFrame)->None:
        """Save the processed dataframe to CSV"""
        try:
            df.to_csv(self.process_data, index=False, encoding=self.encoding)
            logger.info(f"File saved sucessfully.")
        except Exception as e:
            logger.error(f"Failed to save the file ")
            raise 
    
    def load_and_process(self)->str:
        """Run the pipeline"""
        try:
            df= self.load_and_process()
            self.validate_column(df)
            processed_df= self.process_data(df)
            self.save_data(processed_df)
            return self.processed_csv
        except Exception as e:
            logger.critical(f"Pipeline failed: {e}")
            raise RuntimeError(f"Failed to process {self.original_csv}") from e