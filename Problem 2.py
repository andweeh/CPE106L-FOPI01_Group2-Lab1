#input "sample.txt" as your sample file

inputFile = input("Enter the name of file: ")
lines = []

with open(inputFile, 'r') as a:
    for line in a:
        lines.append(line.strip())
        
while True:
    try:
        print("The file has", len(lines), "lines.")
        if len(lines) == 1:
            break
        numLine = int(input("Enter a line number. 0 to Exit: "))
        if numLine == 0:
            break
        else:
            print(numLine, ": ", lines[numLine - 1])
    except:
        print("Error: Line number must be within the range of", len(lines))
        
