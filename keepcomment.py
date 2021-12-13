if comments:
        # keep comments, translate them to target arch comments
        multiline = True
        if target.multiline_start == '\0' or target.multiline_end == '\0':
            multiline = False
        for count,v in enumerate(line[:-1]):
            if not inComment:
                if f'{v}{line[count+1]}' == "//":
                    if target.comments == '\0':
                        throwError("unsupported function", "The target architecture does not support comments.",count)
                    else:
                        line = f"{target.comments}{line[2:]}"
                if f'{v}{line[count+1]}' == "/*":
                    inComment = True
                    lineNum = count
                    if multiline:
                        try: line = f'{line[:count]}{target.multiline_start}{line[count+2:]}'
                        except IndexError: line = f'{line[:count]}{target.multiline_start}'
            else:
                if f'{v}{line[count+1]}' == "*/":
                    if not multiline and count == lineNum:
                        throwError("unsupported function", "The target architecture does not support inline comments", count)
                    else:
                        try: line = f'{line[:count]}{target.multiline_end}{line[count+2:]}'
                        except IndexError: line = f'{line[:count]}{target.multiline_end}'