>>> s
0    0
1    1
2    2
3    3
4    4
5    5
dtype: int32
>>> del(s[3])
>>> s
0    0
1    1
2    2
4    4
5    5
dtype: int32


Columns can be deleted from a DataFrame by using the del keyword or the .pop() or .drop() method of the data frame. 
The behavior of each of these differs slightly:
del will simply delete the Series from the DataFrame (in-place)
pop() will both delete the Series and return the Series as a result (also inplace)
drop(labels, axis=1) will return a new data frame with the column(s) removed (the original DataFrame object is not modified)

>>> del(sp500.RoundedPrice)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: RoundedPrice
>>> del(sp500['RoundedPrice'])
>>> sp500.columns
Index(['Sector', 'Price', 'BookValue', 'NewPrice1', 'NewPrice2', 'NewPrice3'], dtype='object')
>>> del sp500.NewPrice3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: NewPrice3
>>> del sp500['NewPrice3']
>>> sp500.columns
Index(['Sector', 'Price', 'BookValue', 'NewPrice1', 'NewPrice2'], dtype='object')

>>> sp500.pop('NewPrice2')
Symbol
MMM     705.70
ABT     198.00
         ...
ZION    142.15
ZTS     152.65
Name: NewPrice2, Length: 500, dtype: float64
>>> sp500.columns
Index(['Sector', 'Price', 'BookValue', 'NewPrice1'], dtype='object')

The .drop() method can be used to remove both rows and columns. To use it to remove columns, specify axis=1.
>>> sp500.drop(['NewPrice1'], axis=1)
             Sector   Price  BookValue
Symbol
MMM     Industrials  141.14     26.668
ABT     Health Care   39.60     15.573
...             ...     ...        ...
ZION     Financials   28.43     30.191
ZTS     Health Care   30.53      2.150
