l = [[0] for _ in range(10)]
print(l)

s = {i for i in range(1, 21)}
print(s, type(s))
d = {f"num{i}": i ** 2 for i in range(1, 21)}
print(d)

# tuple
t = (1+i for i in range(1,21))
print(tuple(t))
