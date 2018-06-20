>>> metals.describe()
            counts  freqs
categories
bronze           2   0.50
silver           1   0.25
gold             1   0.25
>>> metals.value_counts()
bronze    2
silver    1
gold      1
dtype: int64
>>> (metals.min(), metals.max(), metals.mode())
('bronze', 'gold', [bronze]
Categories (3, object): [bronze < silver < gold])
