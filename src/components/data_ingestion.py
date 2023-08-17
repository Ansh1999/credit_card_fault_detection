import os, sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self):
        self.train_path = os.path.join(os.getcwd(),'artifacts','train.csv')
        self.test_path = os.path.join(os.getcwd(),'artifacts','test.csv')
        self.raw_data = os.path.join(os.getcwd(),'artifacts','raw_data.csv')

    def initiate_ingestion(self):
        logging.info("Ingestion has initiated")
        try:
            df = pd.read_csv('notebook/data/UCI_Credit_Card.csv')
            logging.info("Data is read successfuly...!!")

            path = os.path.join(os.getcwd(),'artifacts')
            os.makedirs(path,exist_ok=True)

            train,test = train_test_split(df, test_size=0.25, random_state=42)
            logging.info("Train test split is done successfully...!!!")
            
            train.to_csv(self.train_path,index=False,header=True)
            test.to_csv(self.test_path,index=False,header=True)
            df.to_csv(self.raw_data,index=False,header=True)
            logging.info("All csv's have been saved to artifacts")
            logging.info("Data ingestion is completed successfully")
        
            return self.train_path,self.test_path

        except Exception as e:
            raise CustomException(e,sys)
        
obj = DataIngestion()
obj.initiate_ingestion()