import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

demand_df = pd.read_csv('/Users/shantanuraut/Desktop/Shell.Ai/Demand_History.csv')
demand_df.head()


L2019 = []
L2020 = []
for i in range(0, len(demand_df)):
    y = np.array(list(demand_df.loc[i])[3:]).reshape(-1, 1)
    x = np.array([10,11,12, 13, 14, 15, 16, 17, 18]).reshape(-1, 1)
    regr = LinearRegression()
    regr.fit(x, y)
    x = [19]
    y_pred = regr.predict(np.array(x).reshape(-1, 1))
    L2019.append(y_pred[0][0])
demand_df['2019'] = L2019
demand_df.head()
for i in range(0, len(demand_df)):
    y = np.array(list(demand_df.loc[i])[3:]).reshape(-1, 1)                     #For demand value
    x = np.array([10,11,12, 13, 14, 15, 16, 17, 18,19]).reshape(-1, 1)          #For years
    regr = LinearRegression()
    regr.fit(x, y)
    x = [20]
    y_pred = regr.predict(np.array(x).reshape(-1, 1))
    L2020.append(y_pred[0][0])
demand_df['2020'] = L2020
demand_df.head()
# print(demand_df.to_string())
demand_df.to_csv("demand_value_2019-20.csv")

