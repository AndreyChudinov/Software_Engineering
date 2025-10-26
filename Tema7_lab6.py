with open('Tema7_lab1_input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('Tema7_lab1_input.txt', 'r') as f:
    result = f.readlines()
    print(result)