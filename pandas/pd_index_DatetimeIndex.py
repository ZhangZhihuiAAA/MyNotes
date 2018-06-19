>>> drng = pd.date_range('5/1/2018', periods=5, freq='H')
>>> drng
DatetimeIndex(['2018-05-01 00:00:00', '2018-05-01 01:00:00',
               '2018-05-01 02:00:00', '2018-05-01 03:00:00',
               '2018-05-01 04:00:00'],
              dtype='datetime64[ns]', freq='H')
>>> ts = pd.Series(np.random.randn(len(drng)), index=drng)
>>> ts
2018-05-01 00:00:00   -0.912307
2018-05-01 01:00:00   -0.767173
2018-05-01 02:00:00   -1.176121
2018-05-01 03:00:00    1.040696
2018-05-01 04:00:00   -0.758245
Freq: H, dtype: float64
>>> ts.loc['2018-05-01 03:00:00']
1.0406963603721826
>>> ts.loc['2018-05-01']
2018-05-01 00:00:00   -0.912307
2018-05-01 01:00:00   -0.767173
2018-05-01 02:00:00   -1.176121
2018-05-01 03:00:00    1.040696
2018-05-01 04:00:00   -0.758245
Freq: H, dtype: float64
>>> ts.loc['2018-05-01 01']
-0.7671731188006791
>>> ts.loc['2018-05-01 0']
KeyError: 'the label [2018-05-01 0] is not in the [index]'

The underlying representation of the date/time is a 64-bit integer, making lookups by date and time very efficient.
