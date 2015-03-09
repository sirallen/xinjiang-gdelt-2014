from path import path
import pandas as pd
from pandasql import sqldf
import os

os.chdir('C:\\Users\Allen\Desktop\GDELT\sub_table')

filepaths = path.getcwd().files('*.csv')

columns = ['SQLDate','Actor1Code','Actor2Code','QuadClass','GoldsteinScale',
'NumMentions','ActionGeo_Lat','ActionGeo_Long','SOURCEURL']
master_table = pd.DataFrame(columns=columns)

for path in filepaths:
	print "Reading " + path
	subtable = pd.read_csv(path,sep=',',header=False,names=columns,encoding='utf-8',low_memory=False)
	q = """
	SELECT *
	FROM subtable
	UNION ALL
	SELECT *
	FROM master_table;
	"""
	master_table = sqldf(q,globals())

# Sorting
master_table = sqldf("SELECT * FROM master_table ORDER BY SQLDate",globals())

print master_table.head()
print master_table.info()

os.chdir('C:\\Users\Allen\Desktop\GDELT')
master_table.to_csv('master_sub_table.csv', index=False)

