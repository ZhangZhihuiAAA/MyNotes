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
