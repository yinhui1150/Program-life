#字典
list1 = [1, 2, 3, 4]
list2 = ['one', 'two', 'three', 'four']

print(list2[list1.index(2)])

dict1 = {1:'one', 2:'two'}
print(dict1)

dict2 = dict(((1,'one'), (2,'two')))
print(dict2)

dict3 = dict(i='one', l='two')
print(dict3)
dict3['l'] = 'love'
print(dict3['l'])