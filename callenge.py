import pandas as pd
from sodapy import Socrata
from sqlalchemy import create_engine

# extract data
client = Socrata("data.sfgov.org", None)
results = client.get("wr8u-xric")

# convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# set function to connect to mysql

# define credentials
user = ''
password = ''
host = ''
port = 3306
database = ''

# define function to connect to db
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
  
# connect to database
try:

    engine = get_connection()
    conn = engine.raw_connection()
    print(
        f"Connection to the {host} for user {user} created successfully.")

except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)


# send data to mysql table
results_df.to_sql('fire_incidents', con=engine, if_exists='replace')
conn.commit()
# close db connection
conn.close()


