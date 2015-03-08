import pandas as pd
from pandasql import sqldf
import os
from geopy.geocoders import GoogleV3
import time

os.chdir('C:\\Users\Allen\Desktop\GDELT')

master = pd.read_csv('master_sub_table_b.csv',sep=',',header=False,encoding='utf-8',low_memory=False)
master = master.drop('Unnamed: 0',1)

q = """
SELECT DISTINCT ActionGeo_Lat, ActionGeo_Long
FROM master
"""
geo_distinct = sqldf(q,globals())
geo_distinct['Location'] = ""

geolocator = GoogleV3()
for i, row in geo_distinct.iterrows():
	latit = str(geo_distinct['ActionGeo_Lat'][i])
	longit = str(geo_distinct['ActionGeo_Long'][i])
	point = ', '.join([latit, longit])
	place = geolocator.reverse(point)
	if place != None:
		try:
			print point + "\t" + str(place[2])
			geo_distinct['Location'][i] = str(place[2])
		except:
			print point + "\tException"
			pass
	else:
		print point + "\tNo Result"
	time.sleep(4)

q = """
SELECT *
FROM master
NATURAL JOIN geo_distinct;
"""
master = sqldf(q,globals())


q = """
SELECT * FROM master
WHERE Location LIKE '%Xinjiang%'
"""
xinjiang_table = sqldf(q,globals())
print xinjiang_table.head()
print xinjiang_table.info()
xinjiang_table.to_csv('xinjiang_table.csv')


q = """
SELECT * FROM xinjiang_table
WHERE Actor1Code LIKE "%UIG%"
OR Actor2Code LIKE "%UIG%"
"""
uighur_table = sqldf(q,globals())
print uighur_table.head()
print uighur_table.info()
uighur_table.to_csv('uighur_table.csv', index=False)




