from subprocess import Popen, PIPE, STDOUT


# ##########################################################################################

# Use the settings below to specify what parameters you want to try, in combination.
# You can easily add more parameters from the yaml to this script by observing how we
# mine them on lines 25-38.

# You can also choose to search for results in the stderr/stdout other than pearson by changing line 45

epochs = [7]
hidden_LSTM = [32, 64, 128]
learning_rate_batch = [(32, '1e-3'), (64, '2e-3')]
dropout = [0.5]


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

# This code does not save the best model, but you can either modify it to do that, or just re-run your model with the best parameters.
for e in epochs:
	for h in hidden_LSTM:
		for l in learning_rate_batch:
			for d in dropout:
				modify_yaml(e, h, l, d)
				p = Popen(["python3", "./openkiwi.py"], stdin=PIPE, stdout=PIPE, close_fds=True)
				returned_output = p.stdout.read()
				file = open("results_all.txt", "a+")
				setup = "################################ EPOCHS: " + str(e) + " hidden_LSTM: " + str(h) + " learning_rate_batch: " + str(l) + " dropout: " + str(d)
				result = mine_result(returned_output)
				print(setup)
				print(result)
				file.write(setup + "\n")
				file.write(result + "\n")
				file.close()