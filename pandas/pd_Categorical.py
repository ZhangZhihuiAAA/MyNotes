>>> lmh_values = ['low', 'high', 'medium', 'medium', 'high']
>>> lmh_cat = pd.Categorical(lmh_values)
>>> lmh_cat
[low, high, medium, medium, high]
Categories (3, object): [high, low, medium]
>>> lmh_cat.categories
Index(['high', 'low', 'medium'], dtype='object')
>>> lmh_cat.get_values()
array(['low', 'high', 'medium', 'medium', 'high'], dtype=object)
>>> lmh_cat.codes
array([1, 0, 2, 2, 0], dtype=int8)
>>> lmh_cat = pd.Categorical(lmh_values, categories=['low', 'medium', 'high'])
>>> lmh_cat
[low, high, medium, medium, high]
Categories (3, object): [low, medium, high]
>>> lmh_cat.codes
array([0, 2, 1, 1, 2], dtype=int8)

>>> cat_series = pd.Series(lmh_values, dtype='category')
>>> cat_series
0       low
1      high
2    medium
3    medium
4      high
dtype: category
Categories (3, object): [high, low, medium]
>>> s = pd.Series(lmh_values)
>>> as_cat = s.astype('category')
>>> as_cat
0       low
1      high
2    medium
3    medium
4      high
dtype: category
Categories (3, object): [high, low, medium]
>>> cat_series.cat
<pandas.core.categorical.CategoricalAccessor object at 0x000000000B402E48>
>>> cat_series.cat.categories
Index(['high', 'low', 'medium'], dtype='object')
>>> cat_series.cat.codes
0    1
1    0
2    2
3    2
4    0
dtype: int8

>>> metal_values = ["bronze", "gold", "silver", "bronze"]
>>> metal_categories = ["bronze", "silver", "gold"]
>>> metals = pd.Categorical(metal_values, categories=metal_categories, ordered=True)
>>> metals
[bronze, gold, silver, bronze]
Categories (3, object): [bronze < silver < gold]

>>> metals_reversed = pd.Categorical(metals.get_values()[::-1], categories=metals.categories, ordered=True)
>>> metals_reversed
[bronze, silver, gold, bronze]
Categories (3, object): [bronze < silver < gold]
>>> metals.codes
array([0, 2, 1, 0], dtype=int8)
>>> metals_reversed.codes
array([0, 1, 2, 0], dtype=int8)
>>> metals <= metals_reversed
array([ True, False,  True,  True])
This comparison is performed by pandas by matching the underlying code for each value.
