Python 3.6.5 (default, Jul 10 2018, 04:44:26)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from unittest import mock
>>> help(mock.side_effect)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'unittest.mock' has no attribute 'side_effect'
>>> values = {'a': 1, 'b': 2, 'c': 3}
>>> def side_effect(arg):
...     return values[arg]
...
>>> mock.side_effect = side_effect
>>> help(mock.side_effect)
Help on function side_effect in module __main__:

side_effect(arg)
(END)
>>> zzh.side_effect = side_effect
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'zzh' is not defined
>>> import os
>>> os.side_effect = side_effect
>>>
