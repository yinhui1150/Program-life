#lambda表达式
def ds(x):
    return 2 * x + 1
print(ds(5))
g = lambda x : 2 * x + 1
print(g(5))

g = lambda x, y : x + y
print(g(3, 4))

#filter
list(filter(None, [1, 0, 1]))

def odd(x):
    return x % 2

temp = range(10)
show = filter(odd, temp)
print(list(show))
print(list(filter(lambda x: x%2, temp)))

#map

print(list(map(lambda x : x * 2, range(10))))