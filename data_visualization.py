# This script can be used to test visualization features in Python
# pip install --upgrade pandas, pandas_datareader, scipy, matplotlib, pyodbc, pycountry, azure
# workfolder = 'c:\\tmp'

import os, numpy as np, pandas as pd, pandas_datareader as dr, datetime
import matplotlib.pyplot as plt
# dir(pd)
# help(pd)

# Test Plot for Sales Figures
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
sales = [15000,18000,17000,17500,42000,32000,39000,89000,121000,289000]
plt.bar(years,sales)
plt.show()

# Configure Modules and Variables
fig = plt.figure()
now = datetime.datetime.now()
begindate = now - datetime.timedelta(days=730)
workfolder = 'c:\\tmp'
os.chdir(workfolder)
os.getcwd()
stock1 = 'GM' 
stock2 = 'TSLA' 
stock3 = 'AMZN' 
datestr = datetime.datetime.today().strftime("%Y%m%d%H%M")

# Download stock data for the last two year
stockprice1 = dr.DataReader(stock1,"yahoo",begindate,now)   
stockprice2 = dr.DataReader(stock2,"yahoo",begindate,now)  
stockprice3 = dr.DataReader(stock3,"yahoo",begindate,now)    

# Test datasets
stockprice1
stockprice1.columns
stockprice1.head()
stockprice1.head(10)
stockprice1.shape
stockprice1.size
stockprice1.describe
stockprice1.describe()
stockprice1.describe(include='all')
stockprice1.isnull().sum()

# Export data to CSV files
file1 = datestr+'_'+stock1
file2 = datestr+'_'+stock2
file3 = datestr+'_'+stock3
stockprice1.to_csv(file1+'.csv',encoding='utf-8')
stockprice2.to_csv(file2+'.csv',encoding='utf-8')
stockprice3.to_csv(file3+'.csv',encoding='utf-8')

# Create lists to be used by Matplotlib
x1 = pd.read_csv(file1+'.csv',sep=',').Date  
x1 = [datetime.datetime.strptime(dates,'%Y-%m-%d').date() for dates in x1]
x2 = pd.read_csv(file2+'.csv',sep=',').Date 
x2 = [datetime.datetime.strptime(dates,'%Y-%m-%d').date() for dates in x2]
x3 = pd.read_csv(file3+'.csv',sep=',').Date
x3 = [datetime.datetime.strptime(dates,'%Y-%m-%d').date() for dates in x3]
y1 = pd.read_csv(file1+'.csv',sep=',').Close
y2 = pd.read_csv(file2+'.csv',sep=',').Close
y3 = pd.read_csv(file3+'.csv',sep=',').Close

# Create Chart
plt.title('Stock Prices for Chosen Companies')
plt.xlabel('Dates')
plt.ylabel('Stock Price')
plt.plot(x1,y1,label=stock1)
plt.plot(x2,y2,label=stock2)
plt.plot(x3,y3,label=stock3)
plt.grid()
plt.legend()

# Save and Display Chart
fig.savefig(datestr+'_'+stock1+'_'+stock2+'_'+stock3+'.pdf')
plt.show()

