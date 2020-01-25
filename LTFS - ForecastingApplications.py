import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from pmdarima.arima.utils import ndiffs
from statsmodels.tsa.stattools import pacf,acf
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.graphics import tsaplots
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score
from sklearn.metrics.scorer import mean_absolute_error
from statsmodels.tsa.statespace.api import SARIMAX
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#Preprocessing the Data:
infile=r'C:\PraveenT\PycharmProjects\Trial\Analytics Vidhya\Hackathon\LTFS\train_fwYjLYX.csv'
outfile=r'C:\PraveenT\PycharmProjects\Trial\Analytics Vidhya\Hackathon\LTFS\output.txt'
df=pd.read_csv(infile)
df['application_date']=pd.to_datetime(df['application_date'])
df1=df[df['segment']==1]
df2=df[df['segment']==2]
df1=df1.set_index(df1['application_date'])
df2=df2.set_index(df2['application_date'])

#Grouping the data as per the requirement:
df1=df1.groupby('segment').resample('D').case_count.sum()
df2=df2.groupby('segment').resample('D').case_count.sum()

#Checking if the given series is stationary for segement 1:
X1=pd.DataFrame(df1)
X2=pd.DataFrame(df2)
X1_log=pd.DataFrame(np.log(X1['case_count']).replace([np.inf,-np.inf],np.nan).fillna(value=np.log(X1['case_count']+1)))

train1=X1_log
model1=auto_arima(train1,trace=True,error_action='ignore', suppress_warnings=True)
m1=model1.fit(train1)
predict1=m1.predict(87)
print(np.exp(predict1))

X2_log=pd.DataFrame(np.log(X2['case_count']).replace([np.inf,-np.inf],np.nan).fillna(value=np.log(X2['case_count']+1)))

#Training the model:

train2=X2_log
model2=auto_arima(train2,trace=True,error_action='ignore', suppress_warnings=True)
m2=model2.fit(train2)
predict2=m2.predict(93)
print(np.exp(predict2))


