import os,sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import inititate_model_training
from src.utils import save_objects

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

try:
    train_path,test_path = DataIngestion().initiate_ingestion()
except Exception as e:
    print(CustomException(e,sys))

class DataTransformation:
    def __init__(self):
        self.datatransformationconfig = os.path.join("artifacts","preprocessor.pkl")

    def DataTransformationPipeline(self,num_columns,cat_columns):

        try:
            '''
            This function is responsible for creating pipelines.
            '''
            logging.info("Pipeline creation has started.")
            num_pipline = Pipeline(
                                    steps=[ 
                                            ("imputation",SimpleImputer(strategy='median')),
                                            ("scaler",StandardScaler(with_mean=False))
                                        ]
                                )
            
            cat_pipeline = Pipeline(
                                    steps=[ 
                                            ("imputation",SimpleImputer(strategy='most_frequent')),
                                            ("encoding",OneHotEncoder()),
                                            ("scaler",StandardScaler(with_mean=False))
                                        ]
                                )
            
            preprocessor = ColumnTransformer(
                                                [
                                                ("num_transformer",num_pipline,num_columns),
                                                ("cat_transformer",cat_pipeline,cat_columns)
                                                ]
                                            )
            logging.info("Pipeline has successfully created.")
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def DataTransformationInitiate(self):
        
        try:
            logging.info('Data transformation has initiated.')
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            num_columns = [i for i in train_data.columns if (train_data[i].dtypes!='O')]
            num_columns.remove('DEFAULT_PAYMENT_NEXT_MONTH')
            cat_columns = [i for i in train_data.columns if (train_data[i].dtypes=='O')]

            obj_preprocessor = self.DataTransformationPipeline(num_columns,cat_columns)

            target = 'DEFAULT_PAYMENT_NEXT_MONTH'

            train_features = train_data.drop(target,axis=1)
            train_target = train_data[target]

            test_features = test_data.drop(target,axis=1)
            test_target = test_data[target]

            train_features_processed = obj_preprocessor.fit_transform(train_features)
            test_features_processed = obj_preprocessor.transform(test_features)

            train_arr = np.c_[train_features_processed,np.array(train_target)]
            test_arr = np.c_[test_features_processed,np.array(test_target)]

            save = save_objects()
            save.save_obj(obj=obj_preprocessor,file_path=self.datatransformationconfig)
            
            logging.info('Data transformation is done and saved as pickle file.')
            
            return train_arr,test_arr
        
        except Exception as e:
            raise CustomException(e,sys)
    

if __name__=="__main__":
    data = DataTransformation()
    train_array,test_array = data.DataTransformationInitiate()

    training = inititate_model_training()
    final_score = training.inititate_training(train_array,test_array)