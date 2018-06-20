>>> cat = pd.Categorical(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c'])
>>> cat
[a, b, c, a]
Categories (3, object): [a, b, c]
>>> cat = pd.Categorical(cat, ordered=True)
>>> cat
[a, b, c, a]
Categories (3, object): [a < b < c]
