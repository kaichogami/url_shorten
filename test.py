import pickle
a = {'change':0, 'last':'aaaaa'}

with open('data.txt', 'wb') as filee:
    pickle.dump(a, filee)
