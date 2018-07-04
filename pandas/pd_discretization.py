>>> np.random.seed(123456)
>>> dist = np.random.normal(size=10)
>>> dist
array([ 0.4691123 , -0.28286334, -1.5090585 , -1.13563237,  1.21211203,
       -0.17321465,  0.11920871, -1.04423597, -0.86184896, -2.10456922])
>>> bins = pd.cut(dist, 5, right=False)
>>> bins
[[-0.115, 0.549), [-0.778, -0.115), [-2.105, -1.441), [-1.441, -0.778), [0.549, 1.215), [-0.778, -0.115), [-0.115, 0.549), [-1.441, -0.778), [-1.441,
-0.778), [-2.105, -1.441)]
Categories (5, interval[float64]): [[-2.105, -1.441) < [-1.441, -0.778) < [-0.778, -0.115) < [-0.115, 0.549) < [0.549, 1.215)]
>>> bins.categories
IntervalIndex([[-2.105, -1.441), [-1.441, -0.778), [-0.778, -0.115), [-0.115, 0.549), [0.549, 1.215)]
              closed='left',
              dtype='interval[float64]')
>>> bins.codes
array([3, 2, 0, 1, 4, 2, 3, 1, 1, 0], dtype=int8)

>>> ages = np.random.randint(6, 45, 50)
>>> ranges = [6, 12, 18, 35, 50]
>>> agebins = pd.cut(ages, ranges)
>>> agebins.describe()
            counts  freqs
categories
(6, 12]          9   0.18
(12, 18]         6   0.12
(18, 35]        22   0.44
(35, 50]        13   0.26
>>> labels = ['Youth', 'Young Adult', 'Adult', 'Middle Aged']
>>> agebins = pd.cut(ages, ranges, labels=labels)
>>> agebins.describe()
             counts  freqs
categories
Youth             9   0.18
Young Adult       6   0.12
Adult            22   0.44
Middle Aged      13   0.26
