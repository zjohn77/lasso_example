from plotly.offline import *
from plotly.graph_objs import *
import pandas as pd
import psycopg2

cpr_rate = pd.read_sql('''SELECT m.performance_date AS "Performance Date",
                                 m.cpr AS "CPR",
                                 mortgage30us/100 AS "Mortgage Rate"
                          FROM (SELECT * FROM monthly_cpr_30y WHERE cpr IS NOT NULL) AS m
                          LEFT JOIN fred_monthly AS f
                          ON m.performance_date = f.performance_date
                          ORDER BY f.performance_date''' 
                       , con = psycopg2.connect('''host = localhost 
                                                   dbname = fn 
                                                   user = postgres 
                                                   password = john''')
                       , parse_dates = ['Performance Date']
                      ).set_index('Performance Date')


# In[3]:


X = cpr_rate.index
Y1 = cpr_rate['CPR']
Y2 = cpr_rate['Mortgage Rate']
Y1COLOR = 'darkblue'
Y2COLOR = 'darkred'
TITLE = 'Prepayment & Mortgage Rate Trends for Fannie Mae 30-Year Mortgages'


# In[4]:


trace1 = Scatter(
    x = X,
    y = Y1,
    name = 'CPR',
    line = dict(color=Y1COLOR)
)
trace2 = Scatter(
    x = X,
    y = Y2,
    name = 'Mortgage Rate',
    yaxis = 'y2',
    line = dict(color=Y2COLOR)
)


# In[5]:


layout = Layout(
    title = TITLE,
    xaxis = {'tickangle': -45,
             'dtick': 'M1'
            },
    yaxis = {'title': 'CPR',
             'range': [0, 0.075],
             'tickformat': '.1%',
             'tickfont': dict(color=Y1COLOR)
            },
    yaxis2 = {'title': 'Mortgage Rate',
              'overlaying': 'y',
              'side': 'right',
              'showgrid': False,
              'range': [0.036, 0.048],
              'tickformat': '.1%',
              'tickfont': dict(color=Y2COLOR)
             },
    legend = {'x': .67, 
              'y': .1,
              'borderwidth': 1
             },
    font = {'size': 16}
)

plot(Figure(data = [trace1, trace2], 
            layout = layout
           )
    )

