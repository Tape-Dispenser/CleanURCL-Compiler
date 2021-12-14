def throwError(name,desc,linenum):
    print(f"ERROR on line {linenum}: \"{name}\": {desc}")
    quit()

def warn(name,desc,linenum):
    print(f"WARNING on line {linenum}: \"{name}\": {desc}")

def parseBlock(linenum):
    global code
    depth = 0
    start = depth + 1
    thingy = []
    for line1 in code[linenum:]:
        for char in line1:
            if char == '{':
                depth += 1
            elif char == '}':
                if depth == start:
                    thingy.append(char)
                    return ''.join(thingy).split('\n')
                depth -= 1
            thingy.append(char)


source = input("input file? (including extension) ")
arch = input("target architecture? ").strip()
target = __import__(f"{arch}.py")
comments = True if input("keep comments? (y/n) ") == "y" else False

with open(source, 'r') as f: code = f.readlines()

# handle comments
for c,line in enumerate(code):
    inComment = False
    if not comments:
        # remove all comments
        templine = list(line)
        for count,v in enumerate(templine[:-1]):
            if inComment:
                templine.pop(count)
            else:
                if templine[count:count+1] == '//':
                    templine = templine[:count-1]
                    break
                elif inComment:
                    templine.pop(count)
                elif templine[count:count+1] == '/*':
                    templine.pop(count)
                    templine.pop(count+1)
                    inComment = True
                elif templine[count:count+1] == '*/':
                    templine.pop(count)
                    templine.pop(count+1)
                    inComment = False
        line = ''.join(templine)
    if line.strip() == '':
        code.pop(c)
    else:
        code[c] = line.strip()
    # if comments are to be kept they will be dealt with later


# parse conditional assembly
inCondition = False
conditionBlocks = []
depth = 0
for c,line in enumerate(code):
    line = line.split()
    if line[0] == '&if':
        conditionBlocks.append([c,f'if {line[1]}',parseBlock(c)])
    elif line[0] == '&elif':
        conditionBlocks.append([c,f'elif {line[1]}',parseBlock(c)])
    elif line[0] == '&else':
        conditionBlocks.append([c,f'else {line[1]}',parseBlock(c)])
