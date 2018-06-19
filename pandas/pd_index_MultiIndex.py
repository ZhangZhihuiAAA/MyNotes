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
