>>> np.random.seed(12345)
>>> df = pd.DataFrame(np.random.randn(5, 4), columns=['A', 'B', 'C', 'D'])
>>> s = df.iloc[0]
>>> df
          A         B         C         D
0 -0.204708  0.478943 -0.519439 -0.555730
1  1.965781  1.393406  0.092908  0.281746
2  0.769023  1.246435  1.007189 -1.296221
3  0.274992  0.228913  1.352917  0.886429
4 -2.001637 -0.371843  1.669025 -0.438570
>>> s
A   -0.204708
B    0.478943
C   -0.519439
D   -0.555730
Name: 0, dtype: float64
>>> df -s
          A         B         C         D
0  0.000000  0.000000  0.000000  0.000000
1  2.170488  0.914462  0.612347  0.837476
2  0.973730  0.767491  1.526628 -0.740491
3  0.479699 -0.250030  1.872356  1.442160
4 -1.796930 -0.850786  2.188464  0.117161
>>> ss = s.reset_index().drop('index', axis=1)
>>> ss
          0
0 -0.204708
1  0.478943
2 -0.519439
3 -0.555730
>>> df - ss
    A   B   C   D   0
0 NaN NaN NaN NaN NaN
1 NaN NaN NaN NaN NaN
2 NaN NaN NaN NaN NaN
3 NaN NaN NaN NaN NaN
4 NaN NaN NaN NaN NaN
>>> s2 = s[1:3]
>>> s2['E'] = 0
>>> df + s2
    A         B         C   D   E
0 NaN  0.957887 -1.038877 NaN NaN
1 NaN  1.872349 -0.426531 NaN NaN
2 NaN  1.725378  0.487751 NaN NaN
3 NaN  0.707856  0.833478 NaN NaN
4 NaN  0.107101  1.149587 NaN NaN
>>> s2 + df
    A         B         C   D   E
0 NaN  0.957887 -1.038877 NaN NaN
1 NaN  1.872349 -0.426531 NaN NaN
2 NaN  1.725378  0.487751 NaN NaN
3 NaN  0.707856  0.833478 NaN NaN
4 NaN  0.107101  1.149587 NaN NaN


>>> a_col = df['A']
>>> df - a_col
    A   B   C   D   0   1   2   3   4
0 NaN NaN NaN NaN NaN NaN NaN NaN NaN
1 NaN NaN NaN NaN NaN NaN NaN NaN NaN
2 NaN NaN NaN NaN NaN NaN NaN NaN NaN
3 NaN NaN NaN NaN NaN NaN NaN NaN NaN
4 NaN NaN NaN NaN NaN NaN NaN NaN NaN
>>> df.sub(a_col, axis=1)
    A   B   C   D   0   1   2   3   4
0 NaN NaN NaN NaN NaN NaN NaN NaN NaN
1 NaN NaN NaN NaN NaN NaN NaN NaN NaN
2 NaN NaN NaN NaN NaN NaN NaN NaN NaN
3 NaN NaN NaN NaN NaN NaN NaN NaN NaN
4 NaN NaN NaN NaN NaN NaN NaN NaN NaN
>>> df.sub(a_col, axis=0)
     A         B         C         D
0  0.0  0.683651 -0.314731 -0.351023
1  0.0 -0.572375 -1.872873 -1.684034
2  0.0  0.477412  0.238167 -2.065244
3  0.0 -0.046079  1.077925  0.611438
4  0.0  1.629795  3.670663  1.563068
