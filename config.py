import os
import sys

from sklearn.ensemble import RandomForestRegressor

class Config:    
    @staticmethod   
    def get_file_name():
        return 'housing.csv'
    
    @staticmethod
    def get_root_path():
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_data_path():
        return os.path.join(Config.get_root_path(), 'data')

    @staticmethod
    def get_model_path():
        return os.path.join(Config.get_root_path(), 'assets')
    
    @staticmethod
    def get_split_settings():
        return {'test_size': 0.2, 'random_state': 42}
    
    @staticmethod
    def get_columns_names():
        return ['CRIM', 
                'ZN', 
                'INDUS', 
                'CHAS', 
                'NOX', 
                'RM', 
                'AGE', 
                'DIS', 
                'RAD', 
                'TAX', 
                'PTRATIO', 
                'B', 
                'LSTAT', 
                'PRICE']
    
    @staticmethod
    def get_model():
        return RandomForestRegressor()