#集合 唯一性 去重性 不支持[]索引

a = {1, 2, 2, 3}
print(a, type(a))


#set的参数可以元组或者列表
b = set((1,2,2,4))

print(b)

#不可变集合 frozen
num = frozenset([1,2])
print(num)
