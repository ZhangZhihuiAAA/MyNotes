The set of columns of the DataFrame objects used in an append do not need to be the same. The resulting data frame will consist of the union of the columns in both, with missing column data filled with NaN.

>>> df1 = sp500.iloc[0:3].copy()
>>> df2 = sp500.iloc[[10, 11, 2], [0, 1, 2]]
>>> df1.head()
             Sector   Price  BookValue  NewPrice1
Symbol
MMM     Industrials  141.14     26.668     1411.4
ABT     Health Care   39.60     15.573      396.0
ABBV    Health Care   53.95      2.954      539.5
>>> df2.head()
             Sector  Price  BookValue
Symbol
A       Health Care  56.18     16.928
GAS       Utilities  52.98     32.462
ABBV    Health Care  53.95      2.954
>>> df1.append(df2)
        BookValue  NewPrice1   Price       Sector
Symbol
MMM        26.668     1411.4  141.14  Industrials
ABT        15.573      396.0   39.60  Health Care
ABBV        2.954      539.5   53.95  Health Care
A          16.928        NaN   56.18  Health Care
GAS        32.462        NaN   52.98    Utilities
ABBV        2.954        NaN   53.95  Health Care

The ignore_index=True parameter can be used to append without forcing the index to be retained from either DataFrame. This is useful when the index values are not of significant meaning and you just want concatenated data with sequentially increasing integers as indexes.
>>> df1.append(df2, ignore_index=True)
   BookValue  NewPrice1   Price       Sector
0     26.668     1411.4  141.14  Industrials
1     15.573      396.0   39.60  Health Care
2      2.954      539.5   53.95  Health Care
3     16.928        NaN   56.18  Health Care
4     32.462        NaN   52.98    Utilities
5      2.954        NaN   53.95  Health Care
