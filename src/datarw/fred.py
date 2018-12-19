'''fetch 8+ (from 1/1/2010) years of history on 7 Freddie Mac Primary Survey rates via FRED.'''
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader.data import DataReader

def read_fred(symbols_, start_):
    return DataReader(symbols_,
                      'fred',
                      start_, 
                      None)  ## defaults to most recent date