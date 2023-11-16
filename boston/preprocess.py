import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as CFG

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


import pickle

class Preprocessor:
    def __init__(self):
        self.data_path =  os.path.join(CFG.get_data_path(), CFG.get_file_name())
        self.model_dir = CFG.get_model_path()
        self.column_names = CFG.get_columns_names()
        self.split_settings = CFG.get_split_settings()
        self.model = CFG.get_model()
        
    def read_data(self):
        return pd.read_csv(self.data_path, header=None, delimiter=r"\s+", names=self.column_names)
    
    def fix_outliers(self,data):
        for col in data.columns:
            q1 = data[col].quantile(0.25)
            q3 = data[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - (1.5 * iqr)
            upper_bound = q3 + (1.5 * iqr)
            outliers = data[(data[col] <= lower_bound) | (data[col] >= upper_bound)]
            if len(outliers) > 0.7 * len(data):
                data.drop(col, axis=1, inplace=True)
            else:
                data.loc[outliers.index, col] = data[col].mean()
        return data
        
    def split_data(self, data):
        X = data.drop('PRICE', axis=1)
        y = data['PRICE']
        return train_test_split(X, y, test_size=self.split_settings['test_size'], random_state=self.split_settings['random_state'])
    
    def scale_data(self,data,mode):
        if mode == 'train':
            scaler = StandardScaler()
            scaler.fit(data)
            pickle.dump(scaler, open(os.path.join(self.model_dir, 'scaler.pkl'), 'wb'))
        else:
            scaler = pickle.load(open(os.path.join(self.model_dir, 'scaler.pkl'), 'rb'))
        scaler.transform(data)
        return data
    
    def train(self, X_train, y_train):
        model = self.model
        model.fit(X_train, y_train)
        pickle.dump(model, open(os.path.join(self.model_dir, 'model.pkl'), 'wb'))
        
    
    def predict(self,test_data):
        model = pickle.load(open(os.path.join(self.model_dir, 'model.pkl'), 'rb'))
        return model.predict(test_data)
        
        
    def preprocess(self):
        data = self.read_data()
        data = self.fix_outliers(data)
        return data
    
    

    
        
