# Files in this Repo:
- train_predictor.py: python script to download data, reduce the training data and run train_predictor.yaml file
- clean_tsv.py : code to convert the WMT20 tsv format of training data into individual files that this repo can understand
- grid_search_QE.py : conducts a grid search on hyperparameters found in the train_estimator.yaml file, so that you can find the best performing model without having to babysit scripts
- random_search_QE.py: conducts a random search on the hyperparameters found in the train_estimator.yaml file, so that you can find the best performing model without having to babysit scripts
- openkiwi.py : runs the code to train the QE model (using pre-trained predictor model, and train_estimator.yaml file)

# Steps to run:

1. Clone this repo

2. Install Poetry via the recommended way:

<curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python>

3. To install all dependencies just run:

<poetry install>

4. To download the data, reduce the training data to about 200MB and execute train_predictor.yaml - run the following:

<python3 train_predictor.py>


## If interested on connecting Google Colab to Google Cloud follow these steps:

1. https://medium.com/@senthilnathangautham/colab-gcp-compute-how-to-link-them-together-98747e8d940e
2. Machine type `n1-standard-8 (8 vCPUs, 30 GB memory)`
3. Image c2-deeplearning-pytorch-1-3-cu100-20191219
4. Made some changes in Step 3: Connect to your server and forward our port:
`gcloud compute ssh --zone us-central1-a instance-4 -- -L 8081:localhost:8081`
5. Made some changes in Step 4: Run a Jupyter Notebook server on your instance
`jupyter notebook --NotebookApp.allow_origin="https://colab.research.google.com" --port=8081 --NotebookApp.port_retries=0 --no-browser`
