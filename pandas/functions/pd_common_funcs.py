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
