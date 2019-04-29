import pandas as pd
import numpy as np
import math
import sys
from datetime import datetime
import calendar
import scipy.stats as st
from scipy.stats.stats import pearsonr
from decimal import Decimal
import nltk


df_Beijing = pd.read_csv('./data/BeijingPM20100101_20151231.csv')
df_Beijing.index = pd.to_datetime(df_Beijing.year*1000000 + df_Beijing.month*10000 + df_Beijing.day*100 + df_Beijing.hour, format='%Y%m%d%H')
df_Beijing = df_Beijing.rename(columns={'PM_US Post': 'pm25', 'DEWP': 'dew_point',
                       'HUMI': 'humidity', 'PRES': 'pressure',
                       'TEMP' : 'temp', 'cbwd': 'wind_dir',
                       'Iws': 'wind_speed'})
df = df_Beijing.copy()
df_wind = df.loc[:,'wind_dir':'wind_speed']
df = df.loc[:,'pm25':'precipitation']
df = df.drop(['wind_dir','wind_speed'], axis=1)
df_wind = df_wind.pivot(columns='wind_dir', values='wind_speed')
df_wind = df_wind.rename(columns={'cv': 'SW'})
df_wind = df_wind.loc[:,'NE':'SW']
df_wind.fillna(0, inplace=True)
df = pd.concat([df, df_wind], axis=1)
df = df.dropna()


# Construct X and y

y = df['pm25'].values
x = df.loc[:,['temp','humidity','pressure','dew_point','precipitation','NW','NE','SE','SW']].values


def main(StringData):
    print(StringData)
    inputData = [float(elem) for elem in StringData]
    print(inputData)
    inputData = [inputData]
    print(inputData)
    from sklearn.ensemble import RandomForestRegressor
    rf_model=RandomForestRegressor(n_estimators=10)
    rf_model.fit(x,y.ravel())
    #rf_test_predict=rf_model.predict_proba(inputData)
    rf_test_predict=rf_model.predict(inputData)
    rf_test_predict=float(rf_test_predict)
    #print("%-30s%-4.2f%-1s"%('Likelihood of Heart Disease is ',100*rf_test_predict[0][1],'%'))
    #print("PM 2.5 Concentration is:%s "%(rf_test_predict))
    if rf_test_predict>0 and rf_test_predict<=50:
    	return ("PM 2.5 Concentration is:" +str(rf_test_predict),"No Health Implications")
    elif rf_test_predict>50 and rf_test_predict<=100:
    	return ("PM 2.5 Concentration is:" +str(rf_test_predict),"Hypersensitive individuals should reduce outdoor Activities")
    elif rf_test_predict>100 and rf_test_predict<=150:
    	return ("PM 2.5 Concentration is:" +str(rf_test_predict),"Individual with breathing or heart problem should reduce outdoor Activities")
    elif rf_test_predict>150 and rf_test_predict<=200:
    	return ("PM 2.5 Concentration is:" +str(rf_test_predict),"Individual with breathing or heart problem should reduce outdoor Activities")
    elif rf_test_predict>200 and rf_test_predict<=300:
    	return ("PM 2.5 Concentration is:" +str(rf_test_predict),"Individual with breathing or heart problem should avoid outdoor Activities")
    elif rf_test_predict>300 and rf_test_predict<=500:
    	return ("PM 2.5 Concentration is:" +str(rf_test_predict),"Healthy Individual should avoid outdoor Activities")


if __name__=="__main__":
    main(sys.argv[1:])
