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
