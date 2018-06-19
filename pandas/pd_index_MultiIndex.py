Hierarchical indexing is a feature of pandas that allows the combined use of two or more indexes per row. Each of the indexes in a hierarchical index is referred to as a level. The specification of multiple levels in an index allows for efficient selection of different subsets of data using different combinations of the values at each level.

>>> s0
  Symbol                  Sector   Price  Book Value
0    MMM             Industrials  141.14      26.668
1    ABT             Health Care   39.60      15.573
2   ABBV             Health Care   53.95       2.954
3    ACN  Information Technology   79.79       8.326
4    ACE              Financials  102.91      86.897
>>> s00 = s0.set_index(['Sector', 'Symbol'])
>>> s00
                                Price  Book Value
Sector                 Symbol
Industrials            MMM     141.14      26.668
Health Care            ABT      39.60      15.573
                       ABBV     53.95       2.954
Information Technology ACN      79.79       8.326
Financials             ACE     102.91      86.897
>>> s00.index
MultiIndex(levels=[['Financials', 'Health Care', 'Industrials', 'Information Technology'], ['ABBV', 'ABT', 'ACE', 'ACN', 'MMM']],
           labels=[[2, 1, 1, 3, 0], [4, 1, 0, 3, 2]],
           names=['Sector', 'Symbol'])


The values of the index itself, at a specific level for every row, can be retrieved by the .get_level_values() method.
>>> s00.index.get_level_values(0)
Index(['Industrials', 'Health Care', 'Health Care', 'Information Technology',
       'Financials'],
      dtype='object', name='Sector')
>>> s00.index.get_level_values(1)
Index(['MMM', 'ABT', 'ABBV', 'ACN', 'ACE'], dtype='object', name='Symbol')

Access to values in the DataFrame object via a hierarchical index is performed using the .xs() method.
>>> s00.xs('Health Care')
        Price  Book Value
Symbol
ABT     39.60      15.573
ABBV    53.95       2.954
>>> s00.xs('Health Care', drop_level=False)
                    Price  Book Value
Sector      Symbol
Health Care ABT     39.60      15.573
            ABBV    53.95       2.954
>>> s00.xs('ABT', level=1)
             Price  Book Value
Sector
Health Care   39.6      15.573
>>> s00.xs('Health Care').xs('ABT')
Price         39.600
Book Value    15.573
Name: ABT, dtype: float64
>>> s00.xs('Health Care', drop_level=False)
                    Price  Book Value
Sector      Symbol
Health Care ABT     39.60      15.573
            ABBV    53.95       2.954
>>> s00.xs('Health Care', drop_level=False).xs('ABT')
Traceback (most recent call last):
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2525, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'ABT'
