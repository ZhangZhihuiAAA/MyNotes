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
