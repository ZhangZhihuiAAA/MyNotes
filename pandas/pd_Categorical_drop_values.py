>>> cat
[a, b, c, a]
Categories (3, object): [a < b < c]
>>> cat.get_values()
array(['a', 'b', 'c', 'a'], dtype=object)
>>> cat = pd.Categorical(np.delete(cat.get_values(), 1), categories=cat.categories, ordered=True)
>>> cat
[a, c, a]
Categories (3, object): [a < b < c]
