A slice is a reference to the data in the source. The use of .iloc[] returns a copy of the data in the source.

>>> import pandas as pd
>>> a = pd.Series([0, 1, 2, 3, 4, 5])
>>> b = a[2:4]
>>> c = a[2:4]
>>> b
2    2
3    3
dtype: int64
>>> c
2    2
3    3
dtype: int64
>>> id(b)
225931504
>>> id(c)
226309400
>>> b[2] = 9
>>> a
0    0
1    1
2    9
3    3
4    4
5    5
dtype: int64
>>> b
2    9
3    3
dtype: int64
>>> c
2    9
3    3
dtype: int64
>>> b[7] = 11
>>> b
2     9
3     3
7    11
dtype: int64
>>> c
2    9
3    3
dtype: int64
>>> c[3] = 20
>>> a
0     0
1     1
2     9
3    20
4     4
5     5
dtype: int64
>>> b
2     9
3     3
7    11
dtype: int64
>>> c
2     9
3    20
dtype: int64
>>>
