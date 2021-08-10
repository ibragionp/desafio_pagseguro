from kaggle.api.kaggle_api_extended import KaggleApi
from variables import *

def extract_file_from_api():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file(data_url, data_file)

def main():
    extract_file_from_api()

main()