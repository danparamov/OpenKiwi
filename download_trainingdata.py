import utils
from ipywidgets import interact, fixed, Textarea
from functools import partial
import tarfile

# Download Data
OK_url = 'https://github.com/facebookresearch/mlqe/blob/master/data/en-de.tar.gz?raw=true'
utils.download_kiwi(OK_url, "./data/traindev")

# Extract Data
my_tar = tarfile.open('./data/traindev/en-de.tar.gz')
my_tar.extractall('./data/traindev') # specify which folder to extract to
my_tar.close()