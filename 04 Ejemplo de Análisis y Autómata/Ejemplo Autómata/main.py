from tkinter import filedialog, Tk

def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title = "Seleccionar un archivo",
        initialdir = "./",
        filetypes = [
            ("todos los archivos",  "*.*")
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
            
# letras = ['a', 'b', 'c'...., 'A', 'B' ]
def isLetra(caracter):
    if((ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122) or ord(caracter) == 164 or ord(caracter) == 165):
        return True
    else:
        return False

def isNumero(caracter):
    if ((ord(caracter) >= 48 and ord(caracter) <= 57)):
        return True
    else:
        return False

def analizar(entrada):
    fila = 1
    columna = 0 # por la forma en la que yo manejo las posiciones primero empiezo la col con 0, no en 1
    estado = 0
    lexActual = ""
    huboError = False

    ['l','e','n','g','u','a','j','e','s']
    
    for c in entrada:
        # Analisis
        if(estado == 0):
            if(ord(c) == 47) or (ord(c) == 92):
                lexActual = lexActual + c
                estado = 1
            elif(ord(c) == 35):
                lexActual = lexActual + c
                estado = 2
            else:
                # Redireccion de estados
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                    pass
                elif(c == "~"):
                    print("Error Lexico, se detecto: 'Fin de Documento' en S0 (" + str(fila) + ", " + str(columna - (len(lexActual) - 1)) + ").")
                else:
                    print("Error Lexico, se detecto " + c + " en S0. F: " + str(fila) + ", " + str(columna - (len(lexActual) - 1)))
            
                #Reiniciar Lexema
                lexActual = ""
        elif (estado == 1):
            # Verifico Letras
            if (isLetra(c)):
                lexActual = lexActual + c
            # Verifico Numeros
            elif (isNumero(c)):
                lexActual = lexActual + c
            else:
                # Parte de aceptacion ya que esta en un Estado de Aceptacion
                print("Se reconocio en S1: '" + lexActual + "' F: " + str(fila) + ", C: " + str(columna - (len(lexActual) - 1)))
                
                # Redireccion de estados
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                    pass
                # Error
                else:
                    print("Error Lexico, se detecto: '" + c + "' en S1 (" + str(fila) + ", " + str(columna - (len(lexActual) - 1)) + ").")

                # Reinicio del lexema
                lexActual = ""
                estado = 0
        elif (estado == 2): #
            # Verifico Letras
            if (isLetra(c)):
                lexActual = lexActual + c
                estado = 3
            # Error
            else:
                if(c == "~"):
                    print("Error Lexico, se detecto: 'Fin de Documento' en S2 (" + str(fila) + ", " + str(columna - (len(lexActual) - 1)) + ").")
                else:
                    print("Error Lexico, se detecto: '" + c + "' en S2 (" + str(fila) + ", " + str(columna - (len(lexActual) - 1)) + ").")
                huboError = True

                # Reinicio del lexema 
                lexActual = ""
                estado = 0
        elif (estado == 3): # Solo aceptacion
            # Parte de aceptacion ya que esta en un Estado de Aceptacion
                print("Se reconocio en S3: '" + lexActual + "' F: " + str(fila) + ", C: " + str(columna - (len(lexActual) - 1)))
                
                # Redireccion de estados
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9 or c == '~':
                    pass
                # Error
                else:
                    print("Error Lexico, se detecto: '" + c + "' en S3 (" + str(fila) + ", " + str(columna - (len(lexActual) - 1)) + ").")

                # Reinicio del lexema
                lexActual = ""
                estado = 0
        
        # Control de filas y columnas
        # Salto de Linea
        if (ord(c) == 10):
            columna = 0
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
    txt = abrir()
    if txt is not None:
        print("Entrada: '" + txt + "'\n")
        txt += "~"
        analizar(txt)
    else:
        print('No se pudo analizar la entrada, intenta de nuevo')