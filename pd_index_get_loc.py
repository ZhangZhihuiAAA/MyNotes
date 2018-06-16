>>> loc_1 = sp500.index.get_loc('MMM')
>>> loc_1
0
>>> loc_2 = sp500.index.get_loc('ACE')
>>> loc_2
4
>>> sp500.iloc[[loc_1, loc_2]]
             Sector   Price  Book Value
Symbol
MMM     Industrials  141.14      26.668
ACE      Financials  102.91      86.897
