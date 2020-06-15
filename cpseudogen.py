import sys
import re
import os.path
from os import path
import stdio
import delete

reglas = [
    ["return 0;\n}","\nFIN;"],
    ["return 0;}","\nFIN;"],
    ["return 1;\n}","\nFIN;"],
    ["return 1;}","\nFIN;"],
    ["return 0;","FIN;"],
    ["return 1;","FIN;"],
    ["printf","Imp"],
    ["scanf","Leer"],
    ["for ","Para "],
    ["if (","Si ("],
    ["else","else "],
    ["else ","Sino "],
    ["while ","Mientras "],
    ["do {","Hacer {"],
    ["int argc,char **argv",""],
    ["int main(void)","int main()"],
    ["int main()\n{","INICIO;"],
    ["int main(){","INICIO;"],
    ["Sino  Si ","SinoSi "],
    ["switch (", "Segun ("],
    ["case", "caso"],
    ["break;", "salto;"],
    ["default: ", "otro: "],
    ['\\' + 'n',""], #quitar \n de printfs y demas
    ["\n    ","\n"]] #quitar 1 tabulacion


#Inicializar el programa
if len(sys.argv) != 2:
    print("Error, especifique archivo de entrada")
    print("ejemplo: <python3 c-to-pseudo.py test.c>")
    exit()
filename = sys.argv[1]
outputfilename = filename.replace(".c", "-pseudo.txt")
if not path.exists(filename):
    print("No se encontro el archivo: <" + filename + ">")
    exit()



#Todo OK!
print("Abriendo el archivo: <" + filename + ">")
sourcefile = open(filename, "r").read()

#eliminar includes, defines, lineas vacias, comentarios, etc. primera pasada
source = delete.includes(sourcefile)
source = delete.defines(source)
source = delete.commentlines(source)
source = delete.commentclosed(source)
source = delete.blanks(source)

#procesar printf y scanf (stdio)
source = stdio.processtdio(source)
print(source)

#ejecutar reglas de reemplazo simples.
for regla in reglas:
    source = source.replace(regla[0], regla[1])

#eliminar includes, defines, lineas vacias, comentarios, etc. segunda pasada
source = delete.blanks(source)






print("\nEscribiendo el archivo: <" + outputfilename + ">.")
output = open(outputfilename, "w+")
output.write(source)
print("Listo.")