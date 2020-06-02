# Files in this Repo:
QE_WMT20.ipynb: Jupyter notebook with the code to run
clean_tsv.py : code to convert the WMT20 tsv format of training data into individual files that this repo can understand
grid_search_QE.py : conducts a grid search on parameters found in the train_estimator.yaml file, so that you can find the best performing model without having to babysit scripts
openkiwi.py : runs the code to train the QE model (using pre-trained predictor, and train_estimator.yaml file)

# Steps to run:

1. Install OpenKiwi- We want to install OpenKiwi as a local package. Follow these steps: https://unbabel.github.io/OpenKiwi/installation.html#as-local-package

2. Create a folder called "data" <./data>

3. Create a folder called "runs" <./runs>, inside that folder create two folders "predictor" <./runs/predictor> and "estimator" <./runs/estimator>

4. Run the QE WMT20.ipynb

5. If you are using GPU, don't foget to change the %%yaml train_predictor at the last line "gpu-id: 1"
