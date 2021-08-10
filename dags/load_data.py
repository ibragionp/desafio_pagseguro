from pandas import read_csv
from pyodbc import connect
from os import environ
from dotenv import load_dotenv
from variables import *

def set_up_environment_variable():
    load_dotenv(files_path + environment_variable_file)

def convert_csv_to_dataframe():
    df = read_csv(files_path + data_file, sep = sep_data, header = col_header_data)
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip().str.replace('\'', ''))
    return df

def load_dataframe_to_database(df):
    cnxn = connect('DRIVER={SQL Server};' + 'SERVER={};DATABASE={};UID={};PWD={}'.format(
        environ.get(server_str), environ.get(database_str), environ.get(username_str), environ.get(password_str)
    ))

    cursor = cnxn.cursor()

    for index, row in df.iterrows():
        cols_database_str = ", ".join([word.capitalize() for word in [col_step_str, col_customer_str, col_age_str, col_gender_str, 
        col_zipcode_ori_str, col_merchant_str, col_zip_merchant_str, col_category_str, col_amount_str, 
        col_fraud_str]])

        cursor.execute("INSERT INTO transactions ({}) values({})".format(cols_database_str, '?,'* 9 + '?'), 
        row[col_step_str], 
        row[col_customer_str],
        row[col_age_str], 
        row[col_gender_str],
        row[col_zipcode_ori_str],
        row[col_merchant_str],
        row[col_zip_merchant_str],
        row[col_category_str],
        row[col_amount_str],
        row[col_fraud_str])
    cnxn.commit()
    cursor.close()

def main():
    set_up_environment_variable()
    load_dataframe_to_database()

main()

