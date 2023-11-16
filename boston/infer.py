import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as CFG
from boston.preprocess import Preprocessor

import pandas as pd

class Infer:
    def __init__(self, data) -> dict:
        self.data = data
        
    def read_data(self):
        return pd.DataFrame(self.data, index=[0])
    
    def get_predictions(self):
        preprocessor = Preprocessor()
        data = self.read_data()
        data = preprocessor.scale_data(data, 'test')
        return {'predictions': preprocessor.predict(data)[0]}
    







