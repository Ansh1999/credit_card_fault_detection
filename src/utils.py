import pickle
import os,sys
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


class save_objects:
    def save_obj(self,obj,file_path):
        try:
            dir_name = os.path.dirname(file_path)
            os.makedirs(dir_name,exist_ok=True)

            with open(file_path,'wb') as file_obj:
                pickle.dump(obj,file_obj) 
        
        except Exception as e:
            raise CustomException(e,sys)
        
class evaluate_models:
    def evaluate(self,X_train,X_test,y_train,y_test,models,params):

        try:
            report = {}

            for i in range(len(list(models))):
                model = list(models.values())[i]
                para = params[list(models.keys())[i]]

                grid = GridSearchCV(model, param_grid=para, cv=3)
                grid.fit(X_train,y_train)

                model.set_params(**grid.best_params_)
                model.fit(X_train,y_train)

                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                train_score = accuracy_score(y_train,y_train_pred)
                test_score = accuracy_score(y_test,y_test_pred)

                report[list(models.keys())[i]] = test_score

                logging.info("Model training is done successfully.")

            return report

        except Exception as e:
            raise CustomException(e,sys)
        
        
class load_file:
    def load(self,file_path):
        try:
            with open(file_path,'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(CustomException(e,sys))