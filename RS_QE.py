import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split                                                
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score
import numpy as np 
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
import kiwi
from kiwi.lib.train import *

def modify_yaml(e, h, l, drop):
	file = open("./experiments/train_estimator.yaml", "r")
	data = file.readlines()
	file.close()

	file = open("./experiments/train_estimator.yaml", "w")
	for d in data:
		if 'epochs:' in d:
			file.write('epochs: ' + str(e) + '\n')
		elif 'hidden-est:' in d:
			file.write('hidden-est: ' + str(h) + '\n')
		elif 'learning-rate:' in d:
			file.write('learning-rate: ' + str(l[1]) + '\n')	
		elif 'train-batch-size:' in d:
			file.write('train-batch-size: ' + str(l[0]) + '\n')	
		elif 'valid-batch-size:' in d:
			file.write('valid-batch-size: ' + str(l[0]) + '\n')		
		elif 'dropout-est:' in d:
			file.write('dropout-est: ' + str(drop) + '\n')		
		else:
			file.write(d)
	file.close()
	print("finished modifying yaml file...")											

random_search = {'epochs': [7],
                'hidden_LSTM': [32, 64, 128],
                'learning_rate_batch': [(32, '1e-3'), (64, '2e-3')],
                'dropout': [0.5]}

predictor = train_from_file('./experiments/train_estimator.yaml')
model = RandomizedSearchCV(estimator = predictor, param_distributions = random_search, n_iter = 80, 
                               cv = 4, verbose= 5, random_state= 101, n_jobs = -1)
modify_yaml(e, h, l, d)



