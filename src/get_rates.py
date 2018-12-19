"""
Call FRED api to load 7 Freddie survey primary rates from the 1st of 2010 to now.
"""
import datarw as rw
from datetime import datetime

RATES = ['MORTGAGE15US','MORTGAGE30US','MORTGAGE5US','MORTMRGN5US','MORTPTS15US','MORTPTS30US','MORTPTS5US']
fh = rw.read_fred(RATES, 
                  datetime(2010, 1, 1)
                 )
fh.columns = fh.columns.str.lower()
fh.index.name = "performance_date"

## Write the resulting Pandas df to the 'fh' table in Postgres.
rw.df2pg(fh, 'fred')