>>> s = pd.Series(np.arange(6))
>>> s
0    0
1    1
2    2
3    3
4    4
5    5
dtype: int32
>>> s[s > 2 and s < 6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 1121, in __nonzero__
    .format(self.__class__.__name__))
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
>>> s[s > 2 & s < 6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Python36\lib\site-packages\pandas\core\generic.py", line 1121, in __nonzero__
    .format(self.__class__.__name__))
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
>>> s[(s > 2) & (s < 6)]
3    3
4    4
5    5
dtype: int32

 

>>> (s >= 0).all()
True
>>> (s < 2).any()
True
>>> s[s < 2].any()
True
>>> s.any()
True
>>> s.all()
False
>>> (s < 4).sum()
4
