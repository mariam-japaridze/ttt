from sklearn.ensemble import RandomForestClassifier

x = [
    [180, 15, 0, 85, 0],
    [167, 42, 1, 60, 1],
    [136, 35, 1, 55, 1],
    [174, 15, 0, 90, 0],
    [141, 28, 1, 45, 1]
]

y = ['sportsman', 'not sportsman', 'not sportsman', 'sportsman', 'not sportsman']

clf = RandomForestClassifier()
clf.fit(x, y)
prediction = clf.predict([[133, 37, 1, 47, 0]])

print(prediction)
