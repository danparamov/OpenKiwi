import utils
import yaml
from ipywidgets import interact, fixed, Textarea
from functools import partial
import tarfile
import pandas as pd
import kiwi
import os

# Download Data
OK_url = 'https://www.quest.dcs.shef.ac.uk/wmt20_files_qe/training_en-de.tar.gz'
utils.download_kiwi(OK_url, "./data/training")

# Extract Data
my_tar = tarfile.open('./data/training/training_en-de.tar.gz')
my_tar.extractall('./data/training') # specify which folder to extract to
my_tar.close()

# Reduction of Data
# English
tinytrainen = pd.read_csv('./data/training/train.ende.en',chunksize=10000, sep='None, /n', engine='python')
readme = tinytrainen.get_chunk(10000)
readme.to_csv(r'./data/training/tinytrainen', index=False, header=False)
# German
tinytrainde = pd.read_csv('./data/training/train.ende.de',chunksize=10000, sep='None, /n', engine='python')
reader = tinytrainde.get_chunk(10000)
reader.to_csv(r'./data/training/tinytrainde', index=False, header=False)

#Run train_predictor.yaml file
predictor_config = './experiments/train_predictor.yaml'
kiwi.train(predictor_config)