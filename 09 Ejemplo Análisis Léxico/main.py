from operator import le
from tkinter import filedialog, Tk
from clases import Token, Error

listaToken = []
listaErrores = []

reservadas = ['RESULTADO', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio','julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title = "Seleccionar un archivo",
        initialdir = "./",
        filetypes = [
            ("Archivos DATA",  "*.data"),
            ("Todos los archivos",  "*.*")
        ]
    )

    if archivo == '':
        print('No se seleccionó ningun archivo')
        return None
    else:
        with open(archivo, 'r', encoding='utf8') as miarchivo:
            dataArchivo = miarchivo.read()
            miarchivo.close()
            print('Lectura exitosa')
            return dataArchivo

def isSimboloValido(caracter):
    # '(' - 40, ')' - 41, ',' - 44, ':' - 58, ';' - 59, '=' - 61, '[' - 91, ']' - 93
    if ord(caracter)==40 or ord(caracter)==41 or ord(caracter)==44 or ord(caracter)==58 or ord(caracter)==59 or ord(caracter)==61 or ord(caracter)==91 or ord(caracter)==93:
        return True
    else:
        return False

def retNombreSimb(simbolo):
    if simbolo == '(':
        return "SimParIzq"
    elif simbolo == ")":
        return "SimParDer"
    elif simbolo == ",":
        return "SimComa"
    elif simbolo == ":":
        return "SimDosPts"
    elif simbolo == ";":
        return "SimPtoComa"
    elif simbolo == "=":
        return "SimIgual"
    elif simbolo == "[":
        return "SimCorIzq"
    elif simbolo == "]":
        return "SimCorDer"

def retPalabraReservada(lexema):
    global reservadas

    for r in reservadas:
        if lexema == r:
            return 'Res_' + r
    return 'ID'

def analizar(entrada):
    global listaToken, listaErrores

    fila = 1
    columna = 1
    estado = "S0"
    anterior = "S0"
    lexema = ""
    
    for c in entrada:
        if estado == "S0":
            if c.isalpha():
                lexema += c
                estado = "S1"
            elif c.isdigit():
                lexema += c
                estado = "S2"
            elif c == '"':
                lexema += c
                estado = "S3"
            elif isSimboloValido(c):
                lexema += c
                anterior = "S0"
                estado = "S4"
            else:
                # Redireccion de estados
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == "$":
                    pass
                else:
                    #print("Error Lexico, se detecto " + c + " en S0. F: " + str(fila) + ", " + str(columna - len(lexema)))
                    listaErrores.append(Error(t='Lexico', v=c+" en S0", f=str(fila), c=str(columna - len(lexema))))
                
                #Reiniciar Lexema
                lexema = ""
                anterior = "S0"
                estado = "S0"

        elif estado == "S1":
            if c.isalpha():
                lexema += c
                estado = "S1"
            elif c.isdigit():
                lexema += c
                estado = "S1"
            elif c == '_':
                lexema += c
                estado = "S1"
            else:
                # Parte de aceptacion ya que esta en un Estado de Aceptacion
                #print("Se reconocio en S1: '" + lexema + "' F: " + str(fila) + ", C: " + str(columna - len(lexema)))
                listaToken.append(Token(n=retPalabraReservada(lexema), l=lexema, f=str(fila), c=str(columna - len(lexema))))

                lexema = ""
                # Redireccion de estados
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '$':
                    pass
                elif isSimboloValido(c) or c.isalpha() or c.isdigit() or c == '"':
                    if c.isalpha():
                        lexema += c
                        estado = "S1"
                    elif c.isdigit():
                        lexema += c
                        estado = "S2"
                    elif c == '"':
                        lexema += c
                        estado = "S3"
                    elif isSimboloValido(c):
                        lexema += c
                        anterior = "S0"
                        estado = "S4"
                    
                    continue
                # Error
                else:
                    #print("Error Lexico, se detecto: '" + c + "' en S1. (" + str(fila) + ", " + str(columna - len(lexema)) + ").")
                    listaErrores.append(Error(t='Lexico', v=c+" en S1", f=str(fila), c=str(columna - len(lexema))))

                # Reinicio del lexema
                anterior = "S0"
                estado = "S0"

        elif estado == "S2":
            if c.isdigit():
                lexema += c
                estado = "S2"
            elif c == '.':
                lexema += c
                estado = "S5"
            else:
                # Parte de aceptacion ya que esta en un Estado de Aceptacion
                #print("Se reconocio en S2: '" + lexema + "' F: " + str(fila) + ", C: " + str(columna - len(lexema)))
                listaToken.append(Token(n='Entero', l=lexema, f=str(fila), c=str(columna - len(lexema))))

                lexema = ""
                # Redireccion de estados
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '$':
                    pass
                elif isSimboloValido(c) or c.isalpha() or c.isdigit() or c == '"':
                    if c.isalpha():
                        lexema += c
                        estado = "S1"
                    elif c.isdigit():
                        lexema += c
                        estado = "S2"
                    elif c == '"':
                        lexema += c
                        estado = "S3"
                    elif isSimboloValido(c):
                        lexema += c
                        anterior = "S0"
                        estado = "S4"
                    
                    continue
                # Error
                else:
                    #print("Error Lexico, se detecto: '" + c + "' en S2. (" + str(fila) + ", " + str(columna - len(lexema)) + ").")
                    listaErrores.append(Error(t='Lexico', v=c+" en S2", f=str(fila), c=str(columna - len(lexema))))

                # Reinicio del lexema
                anterior = "S0"
                estado = "S0"

        elif estado == "S3":
            if c != '"' and c != "\n":
                lexema += c
                estado = "S3"
            elif c == '"':
                lexema += c
                anterior = estado
                estado = "S4"
            else:
                # Redireccion de estados
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9:
                    pass
                elif(c == "$"):
                    #print("Error Lexico, se detecto: 'Fin de Documento' en S3. F: " + str(fila) + ", " + str(columna - len(lexema)))
                    listaErrores.append(Error(t='Lexico', v='Fin de Documento en S3', f=str(fila), c=str(columna - len(lexema))))
                else:
                    #print("Error Lexico, se detecto " + c + " en S3. F: " + str(fila) + ", " + str(columna - len(lexema)))
                    listaErrores.append(Error(t='Lexico', v=c+" en S3", f=str(fila), c=str(columna - len(lexema))))
                
                #Reiniciar Lexema
                lexema = ""
                anterior = "S0"
                estado = "S0"

        elif estado == "S4":
            # Aceptación Directa
            if anterior == "S0":
                #print("Se reconocio en S4: '" + lexema + "' F: " + str(fila) + ", C: " + str(columna - len(lexema)))
                listaToken.append(Token(n=retNombreSimb(lexema), l=lexema, f=str(fila), c=str(columna - len(lexema))))
            elif anterior == "S3":
                #print("Se reconocio en S4: '" + lexema + "' F: " + str(fila) + ", C: " + str(columna - len(lexema)))
                listaToken.append(Token(n='String', l=lexema, f=str(fila), c=str(columna - len(lexema))))
            else:
                print("Error con Anterior evaluada en S4: " + anterior)
            
            # Preanalisis de S0
            lexema = ""

            if c.isalpha():
                lexema += c
                estado = "S1"
            elif c.isdigit():
                lexema += c
                estado = "S2"
            elif c == '"':
                lexema += c
                estado = "S3"
            elif isSimboloValido(c):
                lexema += c
                anterior = "S0"
                estado = "S4"
            else:
                # Redireccion de estados
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == "$":
                    pass
                else:
                    #print("Error Lexico, se detecto " + c + " en S0. F: " + str(fila) + ", " + str(columna - len(lexema)))
                    listaErrores.append(Error(t='Lexico', v=c+" en S0", f=str(fila), c=str(columna - len(lexema))))
                
                #Reiniciar Lexema
                lexema = ""
                anterior = "S0"
                estado = "S0"

        elif estado == "S5":
            if c.isdigit():
                lexema += c
                estado = "S6"
            else:
                if(c == "$"):
                    #print("Error Lexico, se detecto: 'Fin de Documento' en S5. F: " + str(fila) + ", " + str(columna - len(lexema)))
                    listaErrores.append(Error(t='Lexico', v='Fin de Documento en S5', f=str(fila), c=str(columna - len(lexema))))
                else:
                    #print("Error Lexico, se detecto " + c + " en S5. F: " + str(fila) + ", " + str(columna - len(lexema)))
                    listaErrores.append(Error(t='Lexico', v=c+" en S5", f=str(fila), c=str(columna - len(lexema))))
                
                #Reiniciar Lexema
                lexema = ""
                anterior = "S0"
                estado = "S0"

        elif estado == "S6":
            if c.isdigit():
                lexema += c
                estado = "S6"
            else:
                #print("Se reconocio en S6: '" + lexema + "' F: " + str(fila) + ", C: " + str(columna - len(lexema)))
                listaToken.append(Token(n='Decimal', l=lexema, f=str(fila), c=str(columna - len(lexema))))

                lexema = ""
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == "$":
                    pass
                elif isSimboloValido(c) or c.isalpha() or c.isdigit() or c == '"':
                    if c.isalpha():
                        lexema += c
                        estado = "S1"
                    elif c.isdigit():
                        lexema += c
                        estado = "S2"
                    elif c == '"':
                        lexema += c
                        estado = "S3"
                    elif isSimboloValido(c):
                        lexema += c
                        anterior = "S0"
                        estado = "S4"
                    
                    continue
                else:
                    #print("Error Lexico, se detecto " + c + " en S6. F: " + str(fila) + ", " + str(columna - len(lexema)))
                    listaErrores.append(Error(t='Lexico', v=c+" en S6", f=str(fila), c=str(columna - len(lexema))))
                
                #Reiniciar Lexema
                anterior = "S0"
                estado = "S0"

        # Control de filas y columnas
        # Salto de Linea
        if (ord(c) == 10):
            columna = 1
            fila += 1
            continue
        # Tab Horizontal
        elif (ord(c) == 9):
            columna += 4
            continue
        # Espacio
        elif (ord(c) == 32):
            columna += 1
            continue
                
        columna += 1

if __name__ == '__main__':
    listaToken = []
    listaErrores = []
    
    txt = abrir()
    if txt is not None:
        #print("Entrada: \n" + txt + "\n")
        txt += "$"
        analizar(txt)

        value = ""
        while(value != "3"):
            print("\n1. Mostrar Tabla de Tokens")
            print("2. Mostrar Tabla de Errores")
            print("3. Salir")
            value = input('Ingrese una opción: ')

            if value == "1":
                print('\n========== TOKENS ==========')
                for tk in listaToken:
                    print(tk.nombre + " - '" + tk.lexema + "' - F: " + tk.fila + " , C: " + tk.columna)
                print('========== ====== ==========')
            elif value == "2":
                print('\n========== ERRORES ==========')
                for er in listaErrores:
                    print("Error " + er.tipo + " - Se detectó '" + er.valor + "' - F: " + er.fila + " , C: " + er.columna)
                print('========== ======= ==========')
            elif value == "3":
                continue
            else:
                print("Opcion incorrecta")

    else:
        print('No se pudo analizar la entrada, intenta de nuevo')