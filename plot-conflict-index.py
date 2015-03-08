import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
import pylab

matplotlib.rcParams['figure.figsize'] = [10,4]

os.chdir('C:\\Users\Allen\Desktop\GDELT')
xinjiang = pd.read_csv('xinjiang_goldstein.csv',header=False,encoding='utf-8',low_memory=False)

dates = pd.to_datetime(pd.Series(xinjiang['date']))

### Normalize index to max magnitude = 100
daily = xinjiang['goldstein']/abs(min(xinjiang['goldstein']))*100
EMA = xinjiang['EMA']/abs(min(xinjiang['EMA']))*100

daily.plot()
plt.title('XUAR Daily Conflict Index, 01/07-05/14')
pylab.ylim([-120,80])
pylab.show()

EMA.plot(color='red')
plt.title('XUAR Daily Conflict Index (EMA), 01/07-05/14')
pylab.ylim([-120,40])
pylab.show()
