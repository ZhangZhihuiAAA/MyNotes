Creates bins of objects within specific ranges of values.
Reutrns a Categorical.

>>> np.random.seed(12345)
>>> values = np.random.randint(0, 100, 5)
>>> values
array([98, 29,  1, 36, 41])
>>> bins = pd.DataFrame({"values": values})
>>> bins
   values
0      98
1      29
2       1
3      36
4      41
>>> bins['group'] = pd.cut(values, range(0, 101, 10))
>>> bins
   values      group
0      98  (90, 100]
1      29   (20, 30]
2       1    (0, 10]
3      36   (30, 40]
4      41   (40, 50]
>>> bins.columns
Index(['values', 'group'], dtype='object')
>>> bins.group
0    (90, 100]
1     (20, 30]
2      (0, 10]
3     (30, 40]
4     (40, 50]
Name: group, dtype: category
Categories (10, interval[int64]): [(0, 10] < (10, 20] < (20, 30] < (30, 40] ... (60, 70] < (70, 80] < (80, 90] < (90, 100]]
