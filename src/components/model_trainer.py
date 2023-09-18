import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import save_objects, evaluate_models

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB,BernoulliNB
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

class inititate_model_training():
    def __init__(self):
        self.modelconfig = os.path.join('artifacts','model.pkl')

    def inititate_training(self,train_arr,test_arr):
        try:
            logging.info("Model training has initiated")
            X_train,X_test,y_train,y_test = (train_arr[:1001,:-1],
                                            test_arr[:1001,:-1],
                                            train_arr[:1001,-1],
                                            test_arr[:1001,-1]
                                            )
            logging.info("X_train, X_test, y_train, y_test are created successfuly.")

            models = {  
                        "Logistic Regression": LogisticRegression(),
                        "SVC": SVC(),
                        "Decision Tree": DecisionTreeClassifier(),
                        "Gausian Naive Bayes": GaussianNB(),
                        "Bernoulli Naive Bayes": BernoulliNB(),
                        #"Xgboost": XGBClassifier(),
                        "Random Forest": RandomForestClassifier(),
                        "Ada Boost": AdaBoostClassifier(),
                        "Gradient Boosting": GradientBoostingClassifier() 

            }

            params = {
                        "Logistic Regression": {
                                                'penalty': ['l1', 'l2'],
                                                'C': [0.001, 0.01, 0.1, 1, 10],
                                                'solver':['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'],
                                                'max_iter': [100, 200, 300]
                                            },
                        "SVC": { 
                                'C': [0.1, 1, 10],
                                'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
                                'gamma': ['scale', 'auto', 0.1, 1],
                            },

                        "Decision Tree": {
                                            'criterion': ['gini', 'entropy'],
                                            'max_depth': [None, 10, 20, 30], 
                                            'min_samples_split': [2, 5, 10],    
                                            'min_samples_leaf': [1, 2, 4]
                        },
                        "Gausian Naive Bayes": { 
                                                'var_smoothing':[1e-09]

                        },
                        "Bernoulli Naive Bayes": {

                                                'alpha': [0.1, 0.5, 1.0],
                                                'binarize': [None, 0.0, 0.5],
                        },      
                        #"Xgboost": {
                        #            'n_estimators': [50, 100, 150],
                        #            'learning_rate': [0.1, 0.01, 0.001],   
                        #            'max_depth': [3, 5, 7],               
                        #            'subsample': [0.8, 1.0],               
                        #            'colsample_bytree': [0.8, 1.0]
                       # },
                        "Random Forest": {
                                            'n_estimators': [50, 100, 150], 
                                            'max_depth': [None, 10, 20, 30],          
                                            'min_samples_split': [2, 5, 10],           
                                            'min_samples_leaf': [1, 2, 4],          
                                            'max_features': ['auto', 'sqrt', 'log2'],  
                                            'bootstrap': [True, False],                
                                            'criterion': ['gini', 'entropy']
                        },
                        "Ada Boost": {
                                        'n_estimators': [50, 100, 150],   
                                        'learning_rate': [0.01, 0.1, 1.0],        
                                        'algorithm': ['SAMME', 'SAMME.R']      
                        },
                        "Gradient Boosting": {
                                                'n_estimators': [50, 100, 150],    
                                                'learning_rate': [0.01, 0.1, 1.0],     
                                                'max_depth': [3, 5, 7],                 
                                                'subsample': [0.8, 1.0],             
                                                'max_features': ['auto', 'sqrt', 'log2'],
                        }               
            
            }
        
            eval = evaluate_models()
            report = eval.evaluate(X_train,X_test,y_train,y_test,models,params)
            logging.info("Report has been created successfully.")
            logging.info(report)

            best_model_score = max(list(report.values()))
            logging.info(best_model_score)
            logging.info(list(report.values()))
            best_model_name = list(report.keys())[list(report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            logging.info("Best model and best accuracy score has been extracted successfully.")

            if best_model_score<0.6:
                raise CustomException("No model is working as the best model.")
            
            obj = save_objects()
            obj.save_obj(best_model,self.modelconfig)
            logging.info("model.pkl has been created successfully.")

            final_predicted = best_model.predict(X_test)
            final_score = accuracy_score(y_test,final_predicted)

            return final_score


        except Exception as e:
            raise CustomException(e,sys)


