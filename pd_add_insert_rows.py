Rows can also be added to a DataFrame using the .loc property. The parameter for .loc specifies the index label where the row is to be placed. If the label does not exist, the values are appended to the data frame using the given index label. If the label does exist, the values in the specified row are replaced.

>>> ss
             Sector   Price  Book Value
Symbol
MMM     Industrials  141.14      26.668
ABT     Health Care   39.60      15.573
ABBV    Health Care   53.95       2.954
>>> ss.loc["FOO"] = ["the sector", 100, 110]
>>> ss
             Sector   Price  Book Value
Symbol
MMM     Industrials  141.14      26.668
ABT     Health Care   39.60      15.573
ABBV    Health Care   53.95       2.954
FOO      the sector  100.00     110.000
