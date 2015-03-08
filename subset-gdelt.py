from path import path
import pandas as pd
from pandasql import sqldf
import os

os.chdir('C:\\Users\Allen\Desktop\GDELT\Files')

### 58 columns, no header

names = ['GLOBALEVENTID', 'SQLDATE', 'MonthYear', 'Year', 'FractionDate',
'Actor1Code', 'Actor1Name', 'Actor1CountryCode', 'Actor1KnownGroupCode',
'Actor1EthnicCode', 'Actor1Religion1Code', 'Actor1Religion2Code', 'Actor1Type1Code',
'Actor1Type2Code','Actor1Type3Code','Actor2Code','Actor2Name','Actor2CountryCode',
'Actor2KnownGroupCode','Actor2EthnicCode','Actor2Religion1Code','Actor2Religion2Code',
'Actor2Type1Code','Actor2Type2Code','Actor2Type3Code','IsRootEvent','EventCode',
'EventBaseCode','EventRootCode','QuadClass','GoldsteinScale','NumMentions',
'NumSources','NumArticles','AvgTone','Actor1Geo_Type','Actor1Geo_FullName',
'Actor1Geo_CountryCode','Actor1Geo_ADM1Code','Actor1Geo_Lat','Actor1Geo_Long',
'Actor1Geo_FeatureID','Actor2Geo_Type','Actor2Geo_FullName','Actor2Geo_CountryCode',
'Actor2Geo_ADM1Code','Actor2Geo_Lat','Actor2Geo_Long','Actor2Geo_FeatureID',
'ActionGeo_Type','ActionGeo_FullName','ActionGeo_CountryCode','ActionGeo_ADM1Code',
'ActionGeo_Lat','ActionGeo_Long','ActionGeo_FeatureID','DATEADDED','SOURCEURL']

columns = ['SQLDate','Actor1Code','Actor2Code','QuadClass','GoldsteinScale',
'NumMentions','ActionGeo_Lat','ActionGeo_Long','SOURCEURL']
master_table = pd.DataFrame(columns=columns)
selects = ', '.join(columns)

filepaths = path.getcwd().files('*.export.CSV')

for path in filepaths:
	print "Reading " + path[-19:]
	gdelt = pd.read_csv(path,sep='\t',header=None,names=names,encoding='utf-8',low_memory=False)
	q = """
	SELECT """ + selects + """
	FROM gdelt
	WHERE Actor1CountryCode == 'CHN' AND Actor2CountryCode == 'CHN'
	UNION ALL
	SELECT *
	FROM master_table;
	"""
	master_table = sqldf(q,globals())

# Subset by longitude/latitude (box around Xinjiang)
q = """
SELECT * FROM master_table
WHERE ActionGeo_Long BETWEEN 73 AND 97 AND ActionGeo_Lat BETWEEN 35 AND 50
"""
sub_table = sqldf(q,globals())

print sub_table.head()
print sub_table.info()

sub_table.to_csv('sub_table.csv')


