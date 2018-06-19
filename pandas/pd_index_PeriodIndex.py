It is also important to be able to represent periods such as a day, month, or year. This is much like an interval but for a period of time. These scenarios can be modeled by using the PeriodIndex and specifying a specific frequency for the periods in the index.

>>> periods = pd.PeriodIndex(['2018-1', '2018-2', '2018-3'], freq='M')
>>> periods
PeriodIndex(['2018-01', '2018-02', '2018-03'], dtype='period[M]', freq='M')
>>> pd.Series(np.arange(3), periods)
2018-01    0
2018-02    1
2018-03    2
Freq: M, dtype: int32
>>> s = pd.Series(np.arange(3), periods)
>>> s.index
PeriodIndex(['2018-01', '2018-02', '2018-03'], dtype='period[M]', freq='M')
>>> s.loc['2018-1']
0
>>> s.loc['2018-02']
1
>>> s.loc['2018/3']
2
>>> s.loc['2018']
0
