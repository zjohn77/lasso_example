from sqlalchemy import create_engine    

def df2pg(df_, table_):
    '''Write df_ to the Postgres table named table_.''' 
    df_.to_sql(name = table_,
               con = create_engine('postgresql://postgres:john@localhost/fn'),
               if_exists = 'replace'
              )