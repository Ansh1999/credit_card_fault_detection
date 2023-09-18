# Credit Card Default Prediction Project
Internship for PHYSICS WALLAH PVT. LTD. 

## Overview
This machine learning project aims to predict whether a credit card user will default on their payment in the next month based on demographic factors, credit history, and payment behavior. We use the "Credit Card Default Prediction" dataset for this project.

## Motivation
There are times when even a seemingly manageable debt, such as credit cards, goes out of control. Loss of job, medical crisis or business failure are some of the reasons that can impact your finances. In fact, credit card debts are usually the first to get out of hand in such situations due to hefty finance charges (compounded on daily balances) and other penalties.

A lot of us would be able to relate to this scenario. We may have missed credit card payments once or twice because of forgotten due dates or cash flow issues. But what happens when this continues for months? How to predict if a customer will be defaulter in next months?

To reduce the risk of Banks, this model has been developed to predict customer defaulter based on demographic data like gender, age, marital status and behavioral data like last payments, past transactions etc.


## Project Structure
The project is organized as follows:

- **.ebextensions**: Configuration files for AWS Elastic Beanstalk (if applicable).
  - **python.config**: Python configuration file for AWS Elastic Beanstalk (if applicable).
- **LOGS**: Directory containing log files.
- **artifacts**: Directory for storing project artifacts.
  - **.DS_Store**: macOS-specific file, can be ignored.
  - **model.pkl**: Saved machine learning model.
  - **preprocessor.pkl**: Saved data preprocessor (if applicable).
  - **raw_data.csv**: Raw dataset file.
  - **test.csv**: Test dataset file.
  - **train.csv**: Training dataset file.
- **notebook**: Directory containing Jupyter notebooks.
  - **data**: Directory for Credit Card dataset in csv format.
    - **UCI_Credit_Card.csv**: Dataset 
  - **EDA_Credit_Card.ipynb**: Notebook for exploratory data analysis.
- **src**: Source code directory.
  - **components**: Directory for project components.
    - **__init__.py**: Initialization file.
    - **data_ingestion.py**: Module for data ingestion.
    - **data_transformation.py**: Module for data transformation.
    - **model_trainer.py**: Module for training machine learning models.
  - **pipeline**: Directory for data processing pipelines.
    - **__init__.py**: Initialization file.
    - **predict_pipeline.py**: Module for making predictions.
    - **train_pipeline.py**: Module for training pipelines.
  - **__init__.py**: Initialization file for the `src` directory.
  - **exception.py**: Module for custom exceptions.
  - **logger.py**: Module for logging.
  - **utils.py**: Module containing utility functions.
- **static**: Static files directory.
  - **styles.css**: CSS styles for web pages.
- **templates**: HTML templates for web pages.
  - **home.html**: Homepage template.
  - **index.html**: Index page template.
  - **result.html**: Result page template.
- **.gitignore**: Gitignore file to specify ignored files and directories.
- **Dockerfile**: Docker configuration file (if applicable).
- **README.md**: This file, providing an overview of the project.
- **application.py**: Python script for running the application.
- **requirements.txt**: Lists the Python packages and versions required to run the project.
- **setup.py**: Setup script for the project.

## Getting Started
1. **Clone the Repository:**

   ```
   git clone [https://github.com/Ansh1999/credit_card_fault_detection.git](https://github.com/Ansh1999/credit_card_fault_detection.git)
   cd credit-card-default-prediction
   ```
2. **Install Dependencies:**

   ```pip install -r requirements.txt```

3. **Explore the Notebooks:**
   Use the Jupyter notebooks in the `notebook/` directory to explore the data and perform analysis.

4. **Train and Deploy the Model:**
   Refer to the `src/` directory for code related to training and deploying machine learning models.

5. **Run the Web Application:**
   Execute `application.py` to run the web application.

After building the machine learning model and preprocessing pipelines, we've created a web application using Flask to make predictions accessible through a user-friendly interface. We then deployed this web application on AWS Elastic Beanstalk for easy access. Here's how to do it:

1. **Install Flask:**

   Ensure you have Flask installed in your Python environment. You can install it using pip:

   ```bash
   pip install Flask

2. **Create Flask Web App:**
   Develop your Flask web application by creating routes, templates, and necessary logic. Refer to the ```application.py``` file and the ```templates/``` directory in this repository for guidance.

3. **Configure AWS Elastic Beanstalk:**
   Set up an AWS Elastic Beanstalk environment and configure it according to your application's requirements.

4. **Deploy the Web Application:**
   Deploy your Flask application to AWS Elastic Beanstalk. You can use the AWS CLI, AWS Console, or other deployment methods supported by AWS Elastic Beanstalk.

5. **Access the Web Application:**
   Once deployed, you can access your web application using the provided Elastic Beanstalk URL.

## Usage
You can use the deployed web application to make predictions on whether a credit card user will default on their payment in the next month. Input the required information, and the application will provide predictions based on the machine learning model.

## Contributing
Contributions to improve this project are welcome! Please follow common open-source practices and create a pull request with your proposed changes.

## Acknowledgments
* The dataset was provided by Kaggle and can be found at [https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset).
* We acknowledge the UCI Machine Learning Repository for hosting and curating the dataset.
* Please refer to the original data source for information about licensing and usage restrictions.






   
