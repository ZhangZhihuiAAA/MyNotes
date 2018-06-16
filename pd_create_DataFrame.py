>>> pd.DataFrame(np.arange(1, 6))
   0
0  1
1  2
2  3
3  4
4  5
>>> df = pd.DataFrame(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]))
>>> df
   0  1  2  3
0  1  2  3  4
1  5  6  7  8
>>> df.index
RangeIndex(start=0, stop=2, step=1)
>>> df.columns
RangeIndex(start=0, stop=4, step=1)
>>> df = pd.DataFrame(np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), columns=['c1', 'c2', 'c3', 'c4'], index=['a', 'b'])
>>> df
   c1  c2  c3  c4
a   1   2   3   4
b   5   6   7   8
>>> df.index
Index(['a', 'b'], dtype='object')
>>> df.columns
Index(['c1', 'c2', 'c3', 'c4'], dtype='object')


>>> temps_missoula = [70, 71]
>>> temps_philly = [90, 91]
>>> temperatures = {'Missoula': temps_missoula, 'Philly': temps_philly}
>>> temperatures
{'Missoula': [70, 71], 'Philly': [90, 91]}
>>> pd.DataFrame(temperatures)
   Missoula  Philly
0        70      90
1        71      91


>>> temps_t0 = pd.Series([70, 71])
>>> temps_t1 = pd.Series([80, 81])
>>> df = pd.DataFrame([temps_t0, temps_t1])
>>> df
    0   1
0  70  71
1  80  81
>>> df.columns = ['Temp0', 'Temp1']
>>> df
   Temp0  Temp1
0     70     71
1     80     81


>>> sp500 = pd.read_csv("data/sp500.csv", index_col='Symbol', usecols=[0, 2, 3, 7])
>>> sp500.head()
                        Sector   Price  Book Value
Symbol
MMM                Industrials  141.14      26.668
ABT                Health Care   39.60      15.573
ABBV               Health Care   53.95       2.954
ACN     Information Technology   79.79       8.326
ACE                 Financials  102.91      86.897
>>> sp500.shape
(500, 3)
>>> sp500.size
1500
