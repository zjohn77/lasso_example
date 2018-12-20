def add_lags(df, nlags):
   assert (type(nlags) == int) and (nlags >= 1), "nlags is not an positive integer"
   
   for col in df.columns:
      for n in range(1, nlags+1):
         df[col + ' lag' + str(n)] = df[col].shift(n)
   
   return df