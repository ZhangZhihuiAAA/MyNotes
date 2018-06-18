It is a best practice when performing exploratory data analysis to first load the data and explore it using queries / Boolean selection. Then create an index if your data naturally supports one, or if you do require the increased speed.

Index types:

>>> temps
           City  Temperature
0      Missoula           70
1  Philadelphia           80
>>> temps.columns
Index(['City', 'Temperature'], dtype='object')

While this type of index generally works well for alphanumeric column names, it is possible to use other types of indexes as the column index if desired.


>>> df = pd.DataFrame(np.arange(10, 20))
>>> df
    0
0  10
1  11
2  12
3  13
4  14
5  15
6  16
7  17
8  18
9  19
>>> df.columns
RangeIndex(start=0, stop=1, step=1)
>>> df.index
RangeIndex(start=0, stop=10, step=1)

RangeIndex has become the default index for pandas objects.


>>> df_f64 = pd.DataFrame(np.arange(0, 1000, 5), np.arange(0, 100, 0.5))
>>> df_f64.iloc[:5]
      0
0.0   0
0.5   5
1.0  10
1.5  15
2.0  20
>>> df_f64.columns
RangeIndex(start=0, stop=1, step=1)
>>> df_f64.index
Float64Index([ 0.0,  0.5,  1.0,  1.5,  2.0,  2.5,  3.0,  3.5,  4.0,  4.5,
              ...
              95.0, 95.5, 96.0, 96.5, 97.0, 97.5, 98.0, 98.5, 99.0, 99.5],
             dtype='float64', length=200)
>>> df_f64 = pd.DataFrame({"c1": np.arange(0, 1000, 5)}, np.arange(0, 100, 0.5))
>>> df_f64
       c1
0.0     0
0.5     5
1.0    10
1.5    15
2.0    20
...   ...
97.5  975
98.0  980
98.5  985
99.0  990
99.5  995
>>> df_f64.columns
Index(['c1'], dtype='object')
>>> df_f64.index
Float64Index([ 0.0,  0.5,  1.0,  1.5,  2.0,  2.5,  3.0,  3.5,  4.0,  4.5,
              ...
              95.0, 95.5, 96.0, 96.5, 97.0, 97.5, 98.0, 98.5, 99.0, 99.5],
             dtype='float64', length=200)

>>> df_f64.iloc[0]
c1    0
Name: 0.0, dtype: int32
>>> df_f64.iloc[1]
c1    5
Name: 0.5, dtype: int32
>>> df_f64.iloc[2]
c1    10
Name: 1.0, dtype: int32
>>> df_f64.loc[0.0]
c1    0
Name: 0.0, dtype: int32
>>> df_f64.loc[0.5]
c1    5
Name: 0.5, dtype: int32
>>> df_f64.loc[1.0]
c1    10
Name: 1.0, dtype: int32


>>> df_f64.loc[:5]
     c1
0.0   0
0.5   5
1.0  10
1.5  15
2.0  20
..   ..
3.0  30
3.5  35
4.0  40
4.5  45
5.0  50

[11 rows x 1 columns]
Floating-point numbers can be used as index labels by using a Float64Index.
Note that this slice returned 11 rows, instead of the first five.
This is because of the Float64Index, and pandas taking our
statement to mean from the beginning to all values up to 5.0.

Need iloc to slice first five.
>>> df_f64.iloc[:5]
     c1
0.0   0
0.5   5
1.0  10
1.5  15
2.0  20


Distinct buckets of labels can be represented using an IntervalIndex. The interval is closed at one end, either the left or right, meaning that the value at that end of the interval is included in that interval.
>>> df_interval = pd.DataFrame({"A": [1, 2, 3, 4]}, index=pd.IntervalIndex.from_breaks([0, 0.5, 1.0, 1.5, 2.0]))
>>> df_interval
            A
(0.0, 0.5]  1
(0.5, 1.0]  2
(1.0, 1.5]  3
(1.5, 2.0]  4
>>> df_interval.index
IntervalIndex([(0.0, 0.5], (0.5, 1.0], (1.0, 1.5], (1.5, 2.0]]
              closed='right',
              dtype='interval[float64]')
>>> df_interval.index.get_loc(1.2)
2
>>> df_interval.index.get_loc(1.7)
3
>>> df_interval.iloc[df_interval.index.get_loc(1.7)]
A    4
Name: (1.5, 2.0], dtype: int64


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
