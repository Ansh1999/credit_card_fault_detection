import pickle
import os,sys
from src.exception import CustomException


class save_objects:
    def save_obj(self,obj,file_path):
        try:
            dir_name = os.path.dirname(file_path)
            os.makedirs(dir_name,exist_ok=True)

            with open(file_path,'wb') as file_obj:
                pickle.dump(obj,file_obj) 
        
        except Exception as e:
            raise CustomException(e,sys)