from os import path

# extract_data variables
DATA_URL = 'ealaxi/banksim1'
DATA_FILE_NAME = 'bs140513_032310.csv'

# load_data variables
FILES_PATH = '/opt/airflow/dags'
DATA_FILE_CSV = '/bs140513_032310.csv.zip'
SEP_DATA = ','
COL_HEADER_DATA = 0

SERVER_STR = 'SERVER'
DATABASE_STR = 'DATABASE'
USERNAME_STR = 'USERNAMEMSSQL'
PASSWORD_STR = 'PASSWORD'
PORT_STR = 'PORT'

TABLE_NAME_STR = 'transactions'
COL_STEP_STR = 'step'
COL_CUSTOMER_STR = 'customer'
COL_AGE_STR = 'age'
COL_GENDER_STR = 'gender'
COL_ZIPCODEORI_STR = 'zipcodeOri'
COL_MERCHANT_STR = 'merchant'
COL_ZIP_MERCHANT_STR = 'zipMerchant'
COL_CATEGORY_STR = 'category'
COL_AMOUNT_STR = 'amount'
COL_FRAUD_STR = 'fraud'

