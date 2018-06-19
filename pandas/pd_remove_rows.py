Remove rows using .drop(). The .drop() method takes a list of index labels to drop and returns a copy of the DataFrame with the specified rows removed.

>>> ss.drop(['ABT', 'FOO'])
             Sector   Price  Book Value
Symbol
MMM     Industrials  141.14      26.668
ABBV    Health Care   53.95       2.954
>>> ss
             Sector   Price  Book Value
Symbol
MMM     Industrials  141.14      26.668
ABT     Health Care   39.60      15.573
ABBV    Health Care   53.95       2.954
FOO      the sector  100.00     110.000


Remove rows using Boolean selection.
>>> bool_selection = sp500.Price > 300
>>> (len(bool_selection), sum(bool_selection))
(500, 10)
>>> price_less_than_300 = sp500[-bool_selection]
>>> price_less_than_300.shape
(490, 3)
>>> sp500.shape
(500, 3)


Remove rows using a slice.
No need to give an example.
