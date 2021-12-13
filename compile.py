def throwError(name,desc,linenum):
    print(f"ERROR on line {linenum}: \"{name}\": {desc}")
    quit()

def warn(name,desc,linenum):
    print(f"WARNING on line {linenum}: \"{name}\": {desc}")

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

