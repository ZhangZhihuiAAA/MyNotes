>>> sp500.rename(columns={'Book Value': 'BookValue'})
             Sector   Price  BookValue
Symbol
MMM     Industrials  141.14     26.668
ABT     Health Care   39.60     15.573
...             ...     ...        ...
ZION     Financials   28.43     30.191
ZTS     Health Care   30.53      2.150

[500 rows x 3 columns]
>>> sp500.columns
Index(['Sector', 'Price', 'Book Value'], dtype='object')
