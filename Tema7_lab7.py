lines = ['one', 'two', 'three']
with open('Tema7_lab1_input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')