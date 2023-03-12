inputFile = input('Enter the name of file: ')
lines = []

with open(inputFile, 'r') as a:
    for line in a:
        lines.append(line.strip())
        
while True:
    print("The file has", len(lines), "lines.")
    if len(lines) == 1:
        break
    numberLine = int(input("Enter a line number. 0 to Exit: "))
    if numberLine == 1:
        break
    else:
        print(numberLine, ": ", lines[numberLine - 1])
