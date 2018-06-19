>>> sp500.insert(1, 'RoundedPrice', sp500.Price.round())
>>> sp500.columns
Index(['Sector', 'RoundedPrice', 'Price', 'BookValue'], dtype='object')


>>> sp500['NewPrice1'] = sp500.Price * 10
>>> sp500.head()
                        Sector  RoundedPrice   Price  BookValue  NewPrice1
Symbol
MMM                Industrials         141.0  141.14     26.668     1411.4
ABT                Health Care          40.0   39.60     15.573      396.0
ABBV               Health Care          54.0   53.95      2.954      539.5
ACN     Information Technology          80.0   79.79      8.326      797.9
ACE                 Financials         103.0  102.91     86.897     1029.1
>>> sp500.loc[:, 'NewPrice2'] = sp500.Price * 5
>>> sp500.loc[:, 'NewPrice3'] = pd.Series(np.random.normal(size=len(sp500)), index=sp500.index)
>>> sp500.head()
                        Sector  RoundedPrice   Price  BookValue  NewPrice1  NewPrice2  NewPrice3
Symbol
MMM                Industrials         141.0  141.14     26.668     1411.4     705.70  -1.106731
ABT                Health Care          40.0   39.60     15.573      396.0     198.00   1.700464
ABBV               Health Care          54.0   53.95      2.954      539.5     269.75   0.537763
ACN     Information Technology          80.0   79.79      8.326      797.9     398.95   0.798772
ACE                 Financials         103.0  102.91     86.897     1029.1     514.55  -0.120335
>>> NewPrice4 = pd.DataFrame({'NewPrice4': sp500.Price * 7})
>>> sp500_new = pd.concat([sp500, NewPrice4], axis=1)
>>> sp500_new.columns
Index(['Sector', 'RoundedPrice', 'Price', 'BookValue', 'NewPrice1', 'NewPrice2', 'NewPrice3', 'NewPrice4'], dtype='object')


>>> dup_cols = pd.concat([sp500.Price, sp500_new.Price], axis=1)
>>> dup_cols.columns
Index(['Price', 'Price'], dtype='object')
>>> dup_cols.Price.head()
         Price   Price
Symbol
MMM     141.14  141.14
ABT      39.60   39.60
ABBV     53.95   53.95
ACN      79.79   79.79
ACE     102.91  102.91
