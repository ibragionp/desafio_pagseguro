from sqlalchemy import create_engine
from os import environ
from constants import *
from transform_data import *


def load_dataframe_to_database():

    df = convert_csv_to_dataframe()

    engine = create_engine('mssql+pymssql://{}:{}@{}/{}'.format(environ.get(USERNAME_STR),
                                                                environ.get(PASSWORD_STR),
                                                                environ.get(SERVER_STR),
                                                                environ.get(DATABASE_STR)))                            
    df.to_sql(TABLE_NAME_STR, engine, schema='dbo', if_exists='append', index=False)

def main():
    load_dataframe_to_database()

main()

