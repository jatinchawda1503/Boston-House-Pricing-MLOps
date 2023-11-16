import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config as CFG
from boston.preprocess import Preprocessor

class Trainer:
    def train(self):
        preprocessor = Preprocessor()
        data = preprocessor.preprocess()
        X_train, X_test, y_train, y_test = preprocessor.split_data(data)
        X_train = preprocessor.scale_data(X_train, 'train')
        X_test = preprocessor.scale_data(X_test, 'test')
        preprocessor.train(X_train, y_train)
        y_pred = preprocessor.predict(X_test)
        return y_pred
    

if __name__ == '__main__':
    trainer = Trainer()
    trainer.train()
        
        
        
    
        
