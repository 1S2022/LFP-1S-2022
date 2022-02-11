def isLetra(char):
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
        return True
    return False

def isNumero(char):
    if ord(char) >= 48 and ord(char) <= 57:
        return True
    return False

def isBlanco(char):
    if ord(char) == 32 or ord(char) == 10 or ord(char) == 9:
        return True
    return False

if __name__ == '__main__':
    totalLetras = 0
    totalNumeros = 0
    totalSimbolos = 0

    archivo = open('entrada.txt', 'r')
    texto = archivo.read()
    archivo.close()

    if len(texto) > 0:
        for c in texto:
            if isBlanco(c):
                pass
            elif isNumero(c):
                totalNumeros += 1
            elif isLetra(c):
                totalLetras += 1
            else:
                totalSimbolos += 1
        
        print('Total de Letras: ' + str(totalLetras))
        print('Total de Números: ' + str(totalNumeros))
        print('Total de Símbolos: ' + str(totalSimbolos))
    else:
        print('No hay texto para analizar')