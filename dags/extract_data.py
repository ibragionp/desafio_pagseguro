from kaggle.api.kaggle_api_extended import KaggleApi
from constants import *

def extract_file_from_api():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file(DATA_URL,DATA_FILE_NAME,FILES_PATH)

def main():
    extract_file_from_api()

main()