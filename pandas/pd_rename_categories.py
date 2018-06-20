>>> cat = pd.Categorical(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c'])
>>> cat
[a, b, c, a]
Categories (3, object): [a, b, c]
>>> cat.categories = ['bronze', 'silver', 'gold']    # In place
>>> cat
[bronze, silver, gold, bronze]
Categories (3, object): [bronze, silver, gold]
>>> cat.rename_categories(['x', 'y', 'z'])    # NOT in place
[x, y, z, x]
Categories (3, object): [x, y, z]
>>> cat
[bronze, silver, gold, bronze]
Categories (3, object): [bronze, silver, gold]
