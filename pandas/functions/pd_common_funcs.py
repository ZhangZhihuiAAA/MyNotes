>>> s = pd.Series(['a', 'a', 'b', 'c', np.NaN])
>>> s
0      a
1      a
2      b
3      c
4    NaN
dtype: object
>>> s.unique()
array(['a', 'b', 'c', nan], dtype=object)
>>> s.nunique()
3
>>> s.nunique(dropna=False)
4
>>> s.value_counts(dropna=False)
a      2
b      1
c      1
NaN    1
dtype: int64


>>> omh
          Date   MSFT    AAPL
0   2014-12-01  48.62  115.07
1   2014-12-02  48.46  114.63
2   2014-12-03  48.08  115.93
3   2014-12-04  48.84  115.49
4   2014-12-05  48.42  115.00
..         ...    ...     ...
17  2014-12-24  48.14  112.01
18  2014-12-26  47.88  113.99
19  2014-12-29  47.45  113.91
20  2014-12-30  47.02  112.52
21  2014-12-31  46.45  110.38
>>> omh[['MSFT', 'AAPL']].min()
MSFT     45.16
AAPL    106.75
dtype: float64
>>> omh[['MSFT', 'AAPL']].max()
MSFT     48.84
AAPL    115.93
dtype: float64
>>> omh[['MSFT', 'AAPL']].idxmin()
MSFT    11
AAPL    11
dtype: int64
>>> omh[['MSFT', 'AAPL']].idxmax()
MSFT    3
AAPL    2
dtype: int64
>>> omh.nsmallest(4, 'MSFT')
          Date   MSFT    AAPL
11  2014-12-16  45.16  106.75
12  2014-12-17  45.74  109.41
21  2014-12-31  46.45  110.38
10  2014-12-15  46.67  108.23
>>> omh.nsmallest(4, 'MSFT')['MSFT']
11    45.16
12    45.74
21    46.45
10    46.67
Name: MSFT, dtype: float64
>>> omh.nlargest(4, 'MSFT')['MSFT']
3     48.84
0     48.62
1     48.46
16    48.45
Name: MSFT, dtype: float64
>>> omh.MSFT.nsmallest(4)
11    45.16
12    45.74
21    46.45
10    46.67
Name: MSFT, dtype: float64
>>> omh.MSFT.nlargest(4)
3     48.84
0     48.62
1     48.46
16    48.45
Name: MSFT, dtype: float64


>>> s = pd.Series([1, 2, 3, 4])
>>> s
0    1
1    2
2    3
3    4
dtype: int64
>>> s.cumprod()
0     1
1     2
2     6
3    24
dtype: int64
>>> s.cumsum()
0     1
1     3
2     6
3    10
dtype: int64
