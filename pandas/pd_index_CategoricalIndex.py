A CategoricalIndex is used to represent a sparsely populated index for an underlying Categorical.
>>> df_categorical = pd.DataFrame({'A': np.arange(6), 'B': list('aabbca')})
>>> df_categorical
   A  B
0  0  a
1  1  a
2  2  b
3  3  b
4  4  c
5  5  a
>>> df_categorical['B'] = df_categorical['B'].astype('category', categories=list('abc'))
__main__:1: FutureWarning: specifying 'categories' or 'ordered' in .astype() is deprecated; pass a CategoricalDtype instead
>>> df_categorical
   A  B
0  0  a
1  1  a
2  2  b
3  3  b
4  4  c
5  5  a
>>> df_categorical.index
RangeIndex(start=0, stop=6, step=1)
>>> df_categorical = df_categorical.set_index('B')
>>> df_categorical.index
CategoricalIndex(['a', 'a', 'b', 'b', 'c', 'a'], categories=['a', 'b', 'c'], ordered=False, name='B', dtype='category')
>>> df_categorical.loc['a']
   A
B
a  0
a  1
a  5
>>> from pandas.api.types import CategoricalDtype
>>> t = CategoricalDtype(categories=['b', 'c', 'a'], ordered=True)
>>> t
CategoricalDtype(categories=['b', 'c', 'a'], ordered=True)
>>> df_categorical['C'] = df_categorical.index
>>> df_categorical
   A  C
B
a  0  a
a  1  a
b  2  b
b  3  b
c  4  c
a  5  a
>>> df_categorical['C'] = df_categorical['C'].astype(t)
>>> df_categorical = df_categorical.set_index('C')
>>> df_categorical
   A
C
a  0
a  1
b  2
b  3
c  4
a  5
>>> df_categorical.loc['b']
   A
C
b  2
b  3
