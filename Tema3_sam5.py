counter = 0
string = 'hello'
memory = ' world'
values = [0, 2, 4, 6, 8, 10]

while counter != 10:
    if counter in values:
        print(string + memory)
    else:
        print(string)
    counter += 1

print(string + memory)