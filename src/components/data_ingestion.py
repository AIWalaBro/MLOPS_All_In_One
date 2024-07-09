import os
import sys
from src.logger.logger import logging
from src.exception.exception import CustomException
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

class DataTransformation_config:
    pass

class DataTransfromation:
    def __init__(self):
        pass

    def get_data_transformation_obj(self):
        try:
            pass
        except Exception as e:
            logging.info('Exception Occured in the get_data_transformation_obj function')
            raise CustomException(e, sys)