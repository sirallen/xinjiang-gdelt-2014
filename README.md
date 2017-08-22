# xinjiang-gdelt-2014

These are Python files for a research project (term paper) that I did in May 2014. I used the Global Database of Events, Languages, and Tone (http://data.gdeltproject.org/events/index.html) to identify incidents of Uyghur-Han ethnic violence in Xinjiang, People's Republic of China, and then used this information to assess the policies of the Communist Party of China, which have promoted economic development at the expense of minority rights.

`subset-gdelt.py` and `aggregate-subtables.py` subset the GDELT event files (250 million records in total) to find events that occurred between Chinese actors in a box around Xinjiang province. I used the `pandasql` package, which allows SQL queries of pandas DataFrames.

`reverse-geolocate.py` uses the Google Maps geolocation service to identify which of these events occurred in Xinjiang, given long/lat coordinates, and outputs a table `xinjiang_table.csv`.

