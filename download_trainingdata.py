import utils
from ipywidgets import interact, fixed, Textarea
from functools import partial
import tarfile

# Download Data
OK_url = 'https://www.quest.dcs.shef.ac.uk/wmt20_files_qe/en-de.openkiwi-predictor.tar.gz'
utils.download_kiwi(OK_url, "./data/traindev")

# Extract Data
my_tar = tarfile.open('./data/traindev/en-de.openkiwi-predictor.tar.gz')
my_tar.extractall('./data/traindev') # specify which folder to extract to
my_tar.close()