

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
def sfind_between( s, first, last ):
    try:
        start = s.index( first ) 
        end = s.index( last, start ) + len( last )
        return s[start:end]
    except ValueError:
        return ""
def del_closedcomment(src):
    comentario=sfind_between(src,"/*","*/")
    return(src.replace(comentario, ""))
def includes(src): #Elimina includes.
    print("\nEliminando includes...")
    src_out = ""
    for index, line in enumerate(src.splitlines(), start=1):
        if (not line.startswith('#include')):
                src_out += line + '\n'
        else:
            print(" - [Linea: " + str(index) + "] " + line)
    return(src_out)
def defines(src): #Elimina defines.
    print("\nEliminando defines...")
    src_out = ""
    for index, line in enumerate(src.splitlines(), start=1):
        if (not line.startswith('#define')):
                src_out += line + '\n'
        else:
            print(" - [Linea: " + str(index) + "] " + line)
    return(src_out)
def commentlines(src): #elimina comentarios.
    print("\nEliminando comentarios de linea...")
    src_out = ""
    for i, line in enumerate(src.splitlines(), start=1):
        try:
            start = line.index( "//" )
            comentario = line[start:len(line)]
            print(comentario)
            line = line.replace(comentario, "")
            src_out += line + "\n"
        except ValueError:
            src_out += line + "\n"
            
            
    return(src_out)
def commentclosed(src): #elimina comentarios cerrados.
    print("\nEliminando comentarios cerrados...")
    src_out = src

    while src_out.count("/*") > 0:
        comentario=sfind_between(src_out,"/*","*/")
        comentariopt=comentario.replace("\n","")
        src_out = src_out.replace(comentario, "")
        print(" - " + comentariopt)

    return(src_out)
def blanks(src): #elimina lineas en blanco
    print("\nEliminando Lineas en blanco...")
    src_out = ""
    for index, line in enumerate(src.splitlines(), start=1):
        if (not line.isspace()):
            if ((line and line.strip())):
                src_out += line + '\n'
            else:
                print(" - [Linea: " + str(index) + "]")
        else:
            print(" - [Linea: " + str(index) + "]")
    return(src_out)