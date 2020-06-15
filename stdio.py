
stdioSpecifiers = ['c', 'd', 'i', 'e', 'E', 'f', 'g', 'G', 'o', 's', 'u', 'x', 'X', 'p', 'n', '%']
stdioVarEnd = [' ', ',', ')']

class stdioVarPlaceholder():
    def __init__(self, found, text, specifier, startIndex, endIndex):
        self.found = found
        self.text = text
        self.specifier = specifier
        self.startIndex = startIndex
        self.endIndex = endIndex
def getStdioVarPlaceholder(st, startIndex):
    endIndex = 0
    try:
        firstIndex = st.index("%", startIndex)
    except ValueError:
        return(stdioVarPlaceholder(0, "", '', 0, 0))
        
    lowestendIndex = len(st)
    foundspecifier = ''

    for specifier in stdioSpecifiers:
        try:
            endIndex = st.index(specifier, firstIndex + 1)
            if (endIndex <= lowestendIndex):
                lowestendIndex = endIndex
                foundspecifier = specifier
        except ValueError:
            endIndex = lowestendIndex
    
    endIndex = lowestendIndex
    
    text = str(st[firstIndex:endIndex + 1])
    return(stdioVarPlaceholder(1, text, foundspecifier, firstIndex, endIndex))
def getStdioVarReplace(st, startIndex):
    endIndex = 0
    try:
        firstIndex = st.index(" ", startIndex)
    except ValueError:
        return(stdioVarPlaceholder(0, "", '', 0, 0))
        
    lowestendIndex = len(st)
    foundspecifier = ''

    for specifier in stdioVarEnd:
        try:
            endIndex = st.index(specifier, firstIndex + 1)
            if (endIndex <= lowestendIndex):
                lowestendIndex = endIndex
                foundspecifier = specifier
        except ValueError:
            endIndex = lowestendIndex
    endIndex = lowestendIndex
    
    text = str(st[firstIndex + 1:endIndex])
    return(stdioVarPlaceholder(1, text, foundspecifier, firstIndex, endIndex))
def getVarList(st, startIndex):
    varList = []
    try:
        firstVar = getStdioVarPlaceholder(st, startIndex)
        if (firstVar.found == 0):
            return(varList)
        else:
            lastIndex = firstVar.endIndex + 1
            varList.append(firstVar)
    
            while getStdioVarPlaceholder(st, lastIndex).found == 1:
                varList.append(getStdioVarPlaceholder(st, lastIndex))
                lastIndex = getStdioVarPlaceholder(st, lastIndex).endIndex + 1
    except ValueError:
        varList = []
    return(varList)

def getReplaceVarList(st, startIndex):
    varList = []
    try:
        firstVar = getStdioVarReplace(st, startIndex)
        if (firstVar.found == 0):
            return(varList)
        else:
            lastIndex = firstVar.endIndex + 1
            varList.append(firstVar)

            while getStdioVarReplace(st, lastIndex).found == 1:
                varList.append(getStdioVarReplace(st, lastIndex))
                lastIndex = getStdioVarReplace(st, lastIndex).endIndex + 1
    except ValueError:
        varList = []
    return(varList)

def processtdio(src):
    print("\nCorrigiendo printf's...")
    src_out = ""
    for i, line in enumerate(src.splitlines(), start=1):
        try:
            printfstart = line.index( "printf" )
            printf_parentesis_start = line.index("(", printfstart)
            varList = getVarList(line, printf_parentesis_start)
            if (len(varList) > 0):
                printf_string_end = line.index("\",", printf_parentesis_start) + 1
                printf_end = line.index(");", printf_string_end)
                replaceVarList = getReplaceVarList(line, printf_string_end)
                line = line.replace(line[printf_string_end:printf_end], "")
                #reemplazar variables...
                replaceTasks = ""
                for index, var_s in enumerate(varList, start=0):
                    destvar = var_s.text
                    fromvar = "$" + str(replaceVarList[index].text)
                    line = line.replace(destvar, fromvar)
                    replaceTasks += destvar + " -> " + fromvar + "  "
                print(" - [Linea: " + str(i) + "] " + replaceTasks)
        except ValueError:
            pass
        src_out += line + "\n"

    print("\nCorrigiendo scanf's...")
    src_out_2 = ""
    for i, line in enumerate(src_out.splitlines(), start=1):
        try:
            scanfstart = line.index( "scanf" )
            scanf_parentesis_start = line.index("(", scanfstart)
            scanf_string_start = line.index("(\"", scanf_parentesis_start) + 1
            scanf_string_end = line.index("\",", scanf_string_start) + 3
            line = line.replace(line[scanf_string_start:scanf_string_end], "")
            line = line.replace("&", "")
            print(" - [Linea: " + str(i) + "] " + line[scanfstart:len(line)])
        except ValueError:
            pass
        src_out_2 += line + "\n"
    return(src_out_2)