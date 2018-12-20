import pandas as pd
from sklearn.linear_model import LassoLarsIC
from transform.add_lags import add_lags

data = pd.read_pickle('../data/rates.p')

## Add up to 3 lags.
lagged = add_lags(data, 3)
lagged = lagged.dropna()

## Train model.
y = lagged['30-Year Mortgage']
X = lagged.drop(['30-Year Mortgage'], axis=1)
model = LassoLarsIC(criterion = 'bic',
                    normalize = True,
                    positive = False).fit(X, y)

coefficients = pd.Series(model.coef_, index=X.columns)
print(coefficients)

## Look at cross-validation error.