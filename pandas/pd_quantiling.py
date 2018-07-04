>>> dist = np.random.normal(size=1000)
>>> qbin = pd.qcut(dist, 5)
>>> qbin.describe()
                  counts  freqs
categories
(-3.584, -0.827]     200    0.2
(-0.827, -0.207]     200    0.2
(-0.207, 0.243]      200    0.2
(0.243, 0.877]       200    0.2
(0.877, 3.083]       200    0.2
>>> quantiles = [0, 0.25, 0.5, 0.75, 1]
>>> qbin = pd.qcut(dist, quantiles)
>>> qbin.describe()
                    counts  freqs
categories
(-3.584, -0.657]       250   0.25
(-0.657, -0.00493]     250   0.25
(-0.00493, 0.686]      250   0.25
(0.686, 3.083]         250   0.25
>>> quantiles = [0, 0.2, 0.5, 0.8, 1]
>>> qbin = pd.qcut(dist, quantiles)
>>> qbin.describe()
                    counts  freqs
categories
(-3.584, -0.827]       200    0.2
(-0.827, -0.00493]     300    0.3
(-0.00493, 0.877]      300    0.3
(0.877, 3.083]         200    0.2
