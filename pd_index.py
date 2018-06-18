It is a best practice when performing exploratory data analysis to first load the data and explore it using queries / Boolean selection. Then create an index if your data naturally supports one, or if you do require the increased speed.

Index types:

>>> temps
           City  Temperature
0      Missoula           70
1  Philadelphia           80
>>> temps.columns
Index(['City', 'Temperature'], dtype='object')

While this type of index generally works well for alphanumeric column names, it is possible to use other types of indexes as the column index if desired.
