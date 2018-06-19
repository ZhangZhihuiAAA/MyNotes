A Series can be created from a python list.

A Series can be directly itinialized from a Python dictionary.
>>> pd.Series({'Mike': 'dad', 'Mary': 'mom', 'Mikeal': 'son'})
Mary      mom
Mike      dad
Mikeal    son
dtype: object


>>> pd.Series(np.arange(4, 9))
0    4
1    5
2    6
3    7
4    8
dtype: int32
>>> pd.Series(np.linspace(0, 21, 4))
0     0.0
1     7.0
2    14.0
3    21.0
dtype: float64
>>> pd.Series(np.linspace(0, 20, 5))
0     0.0
1     5.0
2    10.0
3    15.0
4    20.0
dtype: float64
>>> np.random.seed(12345)
>>> pd.Series(np.random.normal(size=5))
0   -0.204708
1    0.478943
2   -0.519439
3   -0.555730
4    1.965781
dtype: float64
>>> pd.Series(2)
0    2
dtype: int64


>>> s.index
Int64Index([0, 1, 2, 4, 5], dtype='int64')
>>> s.values
array([0, 1, 2, 4, 5])
