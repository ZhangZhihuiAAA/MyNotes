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


>>> omh
          Date   MSFT    AAPL
0   2014-12-01  48.62  115.07
1   2014-12-02  48.46  114.63
2   2014-12-03  48.08  115.93
3   2014-12-04  48.84  115.49
4   2014-12-05  48.42  115.00
..         ...    ...     ...
17  2014-12-24  48.14  112.01
18  2014-12-26  47.88  113.99
19  2014-12-29  47.45  113.91
20  2014-12-30  47.02  112.52
21  2014-12-31  46.45  110.38
>>> omh[['MSFT', 'AAPL']].min()
MSFT     45.16
AAPL    106.75
dtype: float64
>>> omh[['MSFT', 'AAPL']].max()
MSFT     48.84
AAPL    115.93
dtype: float64
>>> omh[['MSFT', 'AAPL']].idxmin()
MSFT    11
AAPL    11
dtype: int64
>>> omh[['MSFT', 'AAPL']].idxmax()
MSFT    3
AAPL    2
dtype: int64
>>> omh.nsmallest(4, 'MSFT')
          Date   MSFT    AAPL
11  2014-12-16  45.16  106.75
12  2014-12-17  45.74  109.41
21  2014-12-31  46.45  110.38
10  2014-12-15  46.67  108.23
>>> omh.nsmallest(4, 'MSFT')['MSFT']
11    45.16
12    45.74
21    46.45
10    46.67
Name: MSFT, dtype: float64
>>> omh.nlargest(4, 'MSFT')['MSFT']
3     48.84
0     48.62
1     48.46
16    48.45
Name: MSFT, dtype: float64
>>> omh.MSFT.nsmallest(4)
11    45.16
12    45.74
21    46.45
10    46.67
Name: MSFT, dtype: float64
>>> omh.MSFT.nlargest(4)
3     48.84
0     48.62
1     48.46
16    48.45
Name: MSFT, dtype: float64


>>> s = pd.Series([1, 2, 3, 4])
>>> s
0    1
1    2
2    3
3    4
dtype: int64
>>> s.cumprod()
0     1
1     2
2     6
3    24
dtype: int64
>>> s.cumsum()
0     1
1     3
2     6
3    10
dtype: int64


>>> omh = pd.read_csv('data/omh.csv')
>>> omh
          Date   MSFT    AAPL
0   2014-12-01  48.62  115.07
1   2014-12-02  48.46  114.63
..         ...    ...     ...
20  2014-12-30  47.02  112.52
21  2014-12-31  46.45  110.38
>>> omh.describe()
            MSFT        AAPL
count  22.000000   22.000000
mean   47.493182  112.411364
std     0.933077    2.388772
min    45.160000  106.750000
25%    46.967500  111.660000
50%    47.625000  112.530000
75%    48.125000  114.087500
max    48.840000  115.930000
>>> omh.MSFT.describe()
count    22.000000
mean     47.493182
std       0.933077
min      45.160000
25%      46.967500
50%      47.625000
75%      48.125000
max      48.840000
Name: MSFT, dtype: float64
>>> omh.MSFT.describe()['mean']
47.493181818181824

>>> omh.mean(axis=1)
0     81.845
1     81.545
       ...
20    79.770
21    78.415
Length: 22, dtype: float64
>>> omh.median()
MSFT     47.625
AAPL    112.530
dtype: float64
>>> s = pd.Series([1, 2, 3, 3, 5, 1])
>>> s.mode()
0    1
1    3
dtype: int64


>>> a = pd.Series([3, 1, 5])
>>> a.var()
4.0
>>> help(a.var)
Help on method var in module pandas.core.series:

var(axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs) method of pandas.core.series.Series instance
    Return unbiased variance over requested axis.

    Normalized by N-1 by default. This can be changed using the ddof argument

    Parameters
    ----------
    axis : {index (0)}
    skipna : boolean, default True
        Exclude NA/null values. If an entire row/column is NA, the result
        will be NA
    level : int or level name, default None
        If the axis is a MultiIndex (hierarchical), count along a
        particular level, collapsing into a scalar
    ddof : int, default 1
        degrees of freedom
    numeric_only : boolean, default None
        Include only float, int, boolean columns. If None, will attempt to use
        everything, then use only numeric data. Not implemented for Series.

    Returns
    -------
    var : scalar or Series (if level specified)
>>> a.var(ddof=0)
2.6666666666666665
>>> a.std()
2.0
>>> a.std(ddof=0)
1.632993161855452
In statistics, the number of degrees of freedom is the number of values in the final calculation of a statistic that are free to vary.
The number of independent ways by which a dynamic system can move, without violating any constraint imposed on it, is called number of degrees of freedom. In other words, the number of degrees of freedom can be defined as the minimum number of independent coordinates that can specify the position of the system completely.
Estimates of statistical parameters can be based upon different amounts of information or data. The number of independent pieces of information that go into the estimate of a parameter are called the degrees of freedom. In general, the degrees of freedom of an estimate of a parameter are equal to the number of independent scores that go into the estimate minus the number of parameters used as intermediate steps in the estimation of the parameter itself (most of the time the sample variance has N − 1 degrees of freedom, since it is computed from N random scores minus the only 1 parameter estimated as intermediate step, which is the sample mean).


>>> omh.MSFT.cov(omh.AAPL)
1.9261240259740264
>>> omh.AAPL.cov(omh.MSFT)
1.9261240259740264
>>> help(omh.MSFT.cov)
Help on method cov in module pandas.core.series:

cov(other, min_periods=None) method of pandas.core.series.Series instance
    Compute covariance with Series, excluding missing values

    Parameters
    ----------
    other : Series
    min_periods : int, optional
        Minimum number of observations needed to have a valid result

    Returns
    -------
    covariance : float

    Normalized by N-1 (unbiased estimator).


>>> np.random.seed(12345)
>>> s = pd.Series(np.random.randn(5), index=list('abcde'))
>>> s
a   -0.204708
b    0.478943
c   -0.519439
d   -0.555730
e    1.965781
dtype: float64
>>> s.rank()
a    3.0
b    4.0
c    2.0
d    1.0
e    5.0
dtype: float64
There are a number of options that you can use to change this default behavior, such as specifying a custom ranking function and how to decide a ranking when there is a tie.


>>> omh[['MSFT']]
     MSFT
0   48.62
1   48.46
2   48.08
3   48.84
4   48.42
>>> omh[['MSFT']].pct_change()
        MSFT
0        NaN
1  -0.003291
2  -0.007842
3   0.015807
4  -0.008600
