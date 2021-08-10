from os import path

# extract_data variables
data_url = 'ealaxi/banksim1'
data_file = 'bs140513_032310.csv'

# load_data variables
#files_path = path.dirname(path.realpath(__file__))
files_path = 'C:/Users/isabella.pereira/Desktop/airflow-docker'
data_file_csv = '/bs140513_032310.csv.zip'
sep_data = ','
col_header_data = 0

environment_variable_file = '/db_auth.env'

server_str = 'SERVER'
database_str = 'DATABASE'
username_str = 'USERNAMEMSSQL'
password_str = 'PASSWORD'

col_step_str = 'step'
col_customer_str = 'customer'
col_age_str = 'age'
col_gender_str = 'gender'
col_zipcode_ori_str = 'zipcodeOri'
col_merchant_str = 'merchant'
col_zip_merchant_str = 'zipMerchant'
col_category_str = 'category'
col_amount_str = 'amount'
col_fraud_str = 'fraud'

