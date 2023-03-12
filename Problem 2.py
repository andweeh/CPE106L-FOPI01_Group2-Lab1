inputFile = input('Enter the name of file: ')
lines = []

with open(inputFile, 'r') as a:
    for line in a:
        lines.append(line.strip())