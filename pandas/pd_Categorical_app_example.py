>>> np.random.seed(123456)
>>> names = ['Ivana', 'Norris', 'Ruth', 'Lane', 'Skye', 'Sol', 'Dylan', 'Katina', 'Alissa', "Marc"]
>>> grades = np.random.randint(50, 101, len(names))
>>> scores = pd.DataFrame({'Name': names, 'Grade': grades})
>>> scores
   Grade    Name
0     51   Ivana
1     92  Norris
2    100    Ruth
3     99    Lane
4     93    Skye
5     97     Sol
6     93   Dylan
7     77  Katina
8     82  Alissa
9     73    Marc
>>>
>>> score_bins = [ 0, 59,  62, 66,  69,  72, 76,  79,  82, 86,  89,  92, 99, 100]
>>> letter_grades = ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
>>>
>>> letter_cats = pd.cut(scores.Grade, score_bins, labels=letter_grades)
>>> letter_cats
0     F
1    A-
2    A+
3     A
4     A
5     A
6     A
7    C+
8    B-
9     C
Name: Grade, dtype: category
Categories (13, object): [F < D- < D < D+ ... B+ < A- < A < A+]
>>> scores['Letter'] = letter_cats
>>> scores
   Grade    Name Letter
0     51   Ivana      F
1     92  Norris     A-
2    100    Ruth     A+
3     99    Lane      A
4     93    Skye      A
5     97     Sol      A
6     93   Dylan      A
7     77  Katina     C+
8     82  Alissa     B-
9     73    Marc      C
>>>
>>> scores.Letter.value_counts()
A     4
A+    1
A-    1
B-    1
C+    1
C     1
F     1
B+    0
B     0
C-    0
D+    0
D     0
D-    0
Name: Letter, dtype: int64
>>> scores.sort_values(by=['Letter'], ascending=False)
   Grade    Name Letter
2    100    Ruth     A+
6     93   Dylan      A
5     97     Sol      A
4     93    Skye      A
3     99    Lane      A
1     92  Norris     A-
8     82  Alissa     B-
7     77  Katina     C+
9     73    Marc      C
0     51   Ivana      F
>>> scores
   Grade    Name Letter
0     51   Ivana      F
1     92  Norris     A-
2    100    Ruth     A+
3     99    Lane      A
4     93    Skye      A
5     97     Sol      A
6     93   Dylan      A
7     77  Katina     C+
8     82  Alissa     B-
9     73    Marc      C
