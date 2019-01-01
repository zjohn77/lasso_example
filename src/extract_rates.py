"""
A driver program to fetch data from API and store it in a DB.
1. Call FRED api to load 7 Freddie survey primary rates from the beginning of 2010 to now.
2. Archive the extracted data to a PostgreSQL database.
"""
import lib.datarw as rw
from datetime import datetime

## 1. Request from FRED the variables in RATES.
RATES = ['MORTGAGE15US','MORTGAGE30US','MORTGAGE5US','MORTMRGN5US','MORTPTS15US','MORTPTS30US','MORTPTS5US']
fh = rw.read_fred(RATES, 
                  datetime(2010, 1, 1)
                 )
fh.columns = fh.columns.str.lower()
fh.index.name = "performance_date"

## 2. Write the resulting Pandas df to the 'fh' table in Postgres.
rw.df2pg(fh, 'fred')