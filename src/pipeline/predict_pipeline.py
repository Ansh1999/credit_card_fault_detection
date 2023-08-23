import os,sys
import pandas as pd
from src.utils import load_file
from src.exception import CustomException
from src.logger import logging


class PredictPipeline:

    def __init__(self):
        pass

    def predict(self,features):

        try:
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            model_path = os.path.join("artifacts","model.pkl")

            ld = load_file()
            
            obj_preprocessor = ld.load(file_path=preprocessor_path)
            obj_model = ld.load(file_path=model_path)

            scaled = obj_preprocessor.transform(features)
            pred = obj_model.predict(scaled)

            return pred
        
        except Exception as e:
            print(CustomException(e,sys))

class CustomData:

    def __init__(self,
                LIMIT_BAL,
                SEX,
                EDUCATION,
                MARRIAGE,
                AGE,
                PAY_1,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,
                BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,
                PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6
                ):
        try :
            self.LIMIT_BAL = LIMIT_BAL
            self.SEX = SEX
            self.EDUCATION = EDUCATION
            self.MARRIAGE = MARRIAGE
            self.AGE = AGE
            self.PAY_1 = PAY_1
            self.PAY_2 = PAY_2
            self.PAY_3 = PAY_3
            self.PAY_4 = PAY_4
            self.PAY_5 = PAY_5
            self.PAY_6 = PAY_6
            self.BILL_AMT1 = BILL_AMT1
            self.BILL_AMT2 = BILL_AMT2
            self.BILL_AMT3 = BILL_AMT3
            self.BILL_AMT4 = BILL_AMT4
            self.BILL_AMT5 = BILL_AMT5
            self.BILL_AMT6 = BILL_AMT6
            self.PAY_AMT1 = PAY_AMT1
            self.PAY_AMT2 = PAY_AMT2
            self.PAY_AMT3 = PAY_AMT3
            self.PAY_AMT4 = PAY_AMT4
            self.PAY_AMT5 = PAY_AMT5
            self.PAY_AMT6 = PAY_AMT6

        except Exception as e:
            print(CustomException(e,sys))
        
    def get_as_dataframe(self):

        try:
            custom_data = {
                            "LIMIT_BAL" : self.LIMIT_BAL,
                            "SEX" : self.SEX,
                            "EDUCATION" : self.EDUCATION,
                            "MARRIAGE" : self.MARRIAGE,
                            "AGE" : self.AGE,
                            "PAY_1" : self.PAY_1,
                            "PAY_2" : self.PAY_2,
                            "PAY_3" : self.PAY_3,
                            "PAY_4" : self.PAY_4,
                            "PAY_5" : self.PAY_5,
                            "PAY_6" : self.PAY_6,
                            "BILL_AMT1" : self.BILL_AMT1,
                            "BILL_AMT2" : self.BILL_AMT2,
                            "BILL_AMT3" : self.BILL_AMT3,
                            "BILL_AMT4" : self.BILL_AMT4,
                            "BILL_AMT5" : self.BILL_AMT5,
                            "BILL_AMT6" : self.BILL_AMT6,
                            "PAY_AMT1" : self.PAY_AMT1,
                            "PAY_AMT2" : self.PAY_AMT2,
                            "PAY_AMT3" : self.PAY_AMT3,
                            "PAY_AMT4" : self.PAY_AMT4,
                            "PAY_AMT5" : self.PAY_AMT5,
                            "PAY_AMT6" : self.PAY_AMT6
            }

            df = pd.DataFrame(custom_data, index=[0])

            return df

        except Exception as e:
            print(CustomException(e,sys))
