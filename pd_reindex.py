>>> s
0    0
1    1
2    2
3    3
4    4
5    5
dtype: int32
>>> s.reindex([0, 'a', 2, 'b', 4, 'c', 'd', 'e'])
0    0.0
a    NaN
2    2.0
b    NaN
4    4.0
c    NaN
d    NaN
e    NaN
dtype: float64
>>> s.reindex([0, 'a', 2, 'b', 4, 'c', 'd', 'e'], fill_value=9)
0    0
a    9
2    2
b    9
4    4
c    9
d    9
e    9
dtype: int32
>>> s
0    0
1    1
2    2
3    3
4    4
5    5
dtype: int32

  
>>> s.reindex([0, 1, 2, 3, 4, 5, 6, 7, 8])
0    0.0
1    1.0
2    2.0
3    3.0
4    4.0
5    5.0
6    NaN
7    NaN
8    NaN
dtype: float64
>>> s.reindex([0, 11, 2, 33, 4, 54, 6, 7, 8], method='ffill')
0     0
11    5
2     2
33    5
4     4
54    5
6     5
7     5
8     5
dtype: int32
>>> s.reindex([0, 'a', 2, 'b', 4, 'c', 'd', 'e'])
0    0.0
a    NaN
2    2.0
b    NaN
4    4.0
c    NaN
d    NaN
e    NaN
dtype: float64
>>> s.reindex([0, 'a', 2, 'b', 4, 'c', 'd', 'e'], method='ffill')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Python36\lib\site-packages\pandas\core\series.py", line 2681, in reindex
    return super(Series, self).reindex(index=index, **kwargs)
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3023, in reindex
    fill_value, copy).__finalize__(self)
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 3036, in _reindex_axes
    tolerance=tolerance, method=method)
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2990, in reindex
    tolerance=tolerance)
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2684, in get_indexer
    tolerance=tolerance)
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2691, in get_indexer
    indexer = self._get_fill_indexer(target, method, limit, tolerance)
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2721, in _get_fill_indexer
    limit)
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2742, in _get_fill_indexer_searchsorted
    side)
  File "D:\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3541, in _searchsorted_monotonic
    return self.searchsorted(label, side=side)
  File "D:\Python36\lib\site-packages\pandas\util\_decorators.py", line 118, in wrapper
    return func(*args, **kwargs)
  File "D:\Python36\lib\site-packages\pandas\core\base.py", line 1099, in searchsorted
    return self.values.searchsorted(value, side=side, sorter=sorter)
TypeError: '<' not supported between instances of 'int' and 'str'
>>>


>>> s1 = pd.Series(['red', 'green', 'blue'], index=[0, 3, 5])
>>> s1
0      red
3    green
5     blue
dtype: object
>>> s1.reindex(np.arange(7), method='ffill')
0      red
1      red
2      red
3    green
4    green
5     blue
6     blue
dtype: object
>>> s1.reindex([0, 6, 7, 3, 8, 5, 9], method='ffill')
0      red
6     blue
7     blue
3    green
8     blue
5     blue
9     blue
dtype: object
