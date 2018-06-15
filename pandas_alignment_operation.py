The alignment operation actually forms a Cartesian product of the labels in the two Series. If there are n 'a' labels in series 1, and m 'a' labels in series 2, then the result will have n*m 'a' labels in the result.

>>> s1 = pd.Series([1, 2, 3], index=['a', 'a', 'b'])
>>> s1
a    1
a    2
b    3
dtype: int64
>>> s2 = pd.Series([4, 5, 6, 7], index=['a', 'a', 'c', 'a'])
>>> s2
a    4
a    5
c    6
a    7
dtype: int64
>>> s1 + s2
a    5.0
a    6.0
a    8.0
a    6.0
a    7.0
a    9.0
b    NaN
c    NaN
dtype: float64
