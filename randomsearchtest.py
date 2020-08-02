import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from torch import nn
from kiwi.models.predictor_estimator import *

from skorch import NeuralNetRegressor

from subprocess import Popen, PIPE, STDOUT

def mine_result(returned_output):
	returned_output = str(returned_output).split("\\n")
	for line in returned_output:
		if 'pearson correlation coeff: ' in line:
			return line
	return "None"

p = Popen(["python3", "./openkiwi.py"], stdin=PIPE, stdout=PIPE, close_fds=True)
returned_output = p.stdout.read()