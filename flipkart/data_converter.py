import sys
import os

# Add root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
from langchain_core.documents import Document

class DataConverter:
    def __init__(self,file_path:str):
        self.file_path = file_path

    def convert(self):
        df = pd.read_csv(self.file_path)[["product_title","review"]]   

        docs = [
            Document(page_content=row['review'] , metadata = {"product_name" : row["product_title"]})
            for _, row in df.iterrows()
        ]

        return docs
