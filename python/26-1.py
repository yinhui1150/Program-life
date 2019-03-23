#当字典不好用时
#formkeys

dict1 = {}
dict2 = dict1.fromkeys((1,2,3))
print(dict2)

dict3 = dict2.fromkeys((1,2), 'number')
print(dict3)

dict1 = dict1.fromkeys(range(32), '赞')
print(dict1)
for eachkey in dict1.keys():
    print(eachkey)
for value   in dict1.values():
    print(value)
for item    in dict1.items():
    print(item)

#字典中in not in查找的是key，列表中查找的是值
print(dict1.get(32, 'muyou'))
print(32 in dict1)
print(31 in dict1)

dict2 = dict1
#dict1 = {}
#dict1重新指向了一个空对象
print(dict1, dict2)

#dict1.clear()
#print(dict1, dict2)
print(dict1.pop(2))

print(dict1, dict2)

b = {'小白':'狗'}
a = {'1':'one', '2':'two'}
a.update(b)
print(a)




