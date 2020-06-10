import matplotlib.pyplot as plt
import numpy as np
from hyperopt import fmin, rand, hp, Trials
from subprocess import Popen, PIPE, STDOUT

# Random states to make the experiments reproducible
RANDOM_STATES = [1, 2, 3, 4]

epochs = [7]
hidden_LSTM = [32, 64, 128]
learning_rate_batch = [(32, '1e-3'), (64, '2e-3')]
dropout = [0.5]

def get_best_value_epoch(e, candidates):
    """
    Return the candidate for e
    :param e: epoch
    :param candidates: x candidates
    :return: the best candidate
    """
    idx_min = np.argmin(e(candidates))
    return candidates[idx_min]

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

def mine_result(returned_output):
	returned_output = str(returned_output).split("\\n")
	for line in returned_output:
		if 'pearson correlation coeff: ' in line:
			return line
	return "None"


def run_random_search_experiment_epoch(e, n_trials, random_state):
    """
    Run the experiment for random search.
    :param e: epoch
    :param n_trials: number of trials
    :param random_state: value to make the experiment reproducible
    :param show_plot: show plot if true
    :return: the best candidate
    """
    trials = Trials()

    fmin(fn=e,
         space=hp.uniform('x', X_MIN, X_MAX),
         algo=rand.suggest,
         max_evals=n_trials,
         trials=trials,
         rstate=np.random.RandomState(random_state),
         show_progressbar=False)

    rs_candidates = \
        np.array([t['misc']['vals']['x'] for t in trials.trials]).flatten()

    # note: fmin already returns the best value, but let's use our function :)
    selected_value = get_best_value(e, rs_candidates)

    return selected_value


def run_experiments(e, n_trials, random_state, show=False):
    """
    Run the experiments for random search.
    :param e: epoch
    :param n_trials: number of trials
    :param random_state: value to make the experiment reproducible
    :param show: show plot and winner if true
    :return: the best candidates found for grid search and random search
    """
 
    rs_selected_value = run_random_search_experiment(e,
                                                     n_trials,
                                                     random_state,
                                                     show)

    return rs_selected_value

    modify_yaml(e, h, l, d)
	p = Popen(["python3", "./openkiwi.py"], stdin=PIPE, stdout=PIPE, close_fds=True)
	returned_output = p.stdout.read()
	file = open("results_all_rs.txt", "a+")
	setup = "################################ EPOCHS: " + str(e) + " hidden_LSTM: " + str(h) + " learning_rate_batch: " + str(l) + " dropout: " + str(d)
	result = mine_result(returned_output)
	print(setup)
	print(result)
	file.write(setup + "\n")
	file.write(result + "\n")
	file.close()