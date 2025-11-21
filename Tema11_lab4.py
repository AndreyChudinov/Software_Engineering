b = (i ** 2 for i in range(1, 5))
print(b) # вывод не такой, как у генератора списков
print('first')
for i in b:
    print(i)
print('second')
# из-за особенностей выражений генераторов,
# они не будут выводиться больше одного раза
for i in b:
    print(i)