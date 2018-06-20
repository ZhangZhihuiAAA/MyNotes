>>> metals
[bronze, gold, silver, bronze]
Categories (3, object): [bronze < silver < gold]
>>> metals.add_categories(['coper'])
[bronze, gold, silver, bronze]
Categories (4, object): [bronze < silver < gold < coper]
>>> metals
[bronze, gold, silver, bronze]
Categories (3, object): [bronze < silver < gold]


>>> metals.remove_categories(['bronze'])
[NaN, gold, silver, NaN]
Categories (2, object): [silver < gold]
>>> metals
[bronze, gold, silver, bronze]
Categories (3, object): [bronze < silver < gold]


>>> with_platinum
[bronze, silver, gold, bronze]
Categories (4, object): [bronze, silver, gold, platinum]
>>> with_platinum.remove_unused_categories(inplace=True)
>>> with_platinum
[bronze, silver, gold, bronze]
Categories (3, object): [bronze, silver, gold]
