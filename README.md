# Files in this Repo:
- QE_WMT20.ipynb: Jupyter notebook with the code to run
- clean_tsv.py : code to convert the WMT20 tsv format of training data into individual files that this repo can understand
- grid_search_QE.py : conducts a grid search on parameters found in the train_estimator.yaml file, so that you can find the best performing model without having to babysit scripts
- openkiwi.py : runs the code to train the QE model (using pre-trained predictor, and train_estimator.yaml file)

# Steps to run:

1. Install OpenKiwi- We want to install OpenKiwi as a local package. Follow these steps: https://unbabel.github.io/OpenKiwi/installation.html#as-local-package

2. Create a folder called "data" <./data>

3. Create a folder called "runs" <./runs>, inside that folder create two folders "predictor" <./runs/predictor> and "estimator" <./runs/estimator>

4. Run the QE WMT20.ipynb

5. If you are using GPU, don't foget to change the %%yaml train_predictor at the last line "gpu-id: 1"

## If interested on connecting Google Colab to Google Cloud follow these steps:

1. https://medium.com/@senthilnathangautham/colab-gcp-compute-how-to-link-them-together-98747e8d940e
2. Machine type `n1-standard-8 (8 vCPUs, 30 GB memory)`
3. Image c2-deeplearning-pytorch-1-3-cu100-20191219
4. Made some changes in Step 3: Connect to your server and forward our port:
`gcloud compute ssh --zone us-central1-a instance-4 -- -L 8081:localhost:8081`
5. Made some changes in Step 4: Run a Jupyter Notebook server on your instance
`jupyter notebook --NotebookApp.allow_origin="https://colab.research.google.com" --port=8081 --NotebookApp.port_retries=0 --no-browser`
