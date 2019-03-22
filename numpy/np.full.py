>>> a = np.full((2, 3, 4), 0)
>>> a
array([[[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],

       [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]])
>>> b = np.full((2, 3, 4), np.array([0, 0, 0, 0]))
>>> b
array([[[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],

       [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]])
>>> c = np.full((2, 3, 4), np.array([[0, 0, 0, 0],
...         [0, 0, 0, 0],
...         [0, 0, 0, 0]]))
>>> c
array([[[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],

       [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]])
>>> assert a.all() == b.all() == c.all()
>>> d = np.full((2, 3, 4), np.array([0, 0]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.6/dist-packages/numpy/core/numeric.py", line 336, in full
    multiarray.copyto(a, fill_value, casting='unsafe')
ValueError: could not broadcast input array from shape (2) into shape (2,3,4)
