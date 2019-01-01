import pandas as pd
from sklearn.linear_model import LassoLarsIC
from lib.munge import add_lags, split_sample_bytime

## 1. Read the data serialized by visualize.ipynb
data = pd.read_pickle('../data/rates.p')

## 2. Add up to 3 lags and drop holes created from lagging, or holidays.
lagged = add_lags(data, 3).dropna()

## 3. Train/test split.
lagged.index = pd.to_datetime(lagged.index, utc=True)
X_train, y_train, X_holdout, y_holdout = split_sample_bytime(lagged)

## 4. Train model.
model = LassoLarsIC(criterion = 'bic',
                    normalize = True,
                    positive = False).fit(X_train, y_train)

## Compare the training set error and the out-of-time holdout error.
R2_train = model.score(X_train, y_train)
R2_holdout = model.score(X_holdout, y_holdout)
print(R2_train)
print(R2_holdout)


## Print the coefficients of the LASSO model.
coefficients = pd.Series(model.coef_, 
                         index = X_train.columns
                        )
print(coefficients)