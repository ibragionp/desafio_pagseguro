from pandas import read_csv
from constants import *

def convert_csv_to_dataframe():
    df = read_csv(FILES_PATH + DATA_FILE_CSV, sep = SEP_DATA, header = COL_HEADER_DATA)
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip().str.replace('\'', ''))
    return df
