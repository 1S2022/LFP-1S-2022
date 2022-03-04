def regresarDatos(entrada):
    day = ''
    month = ''
    year = ''
    
    aux = ''
    estado = 'd'
    posicion = 1
    for c in entrada:
        if estado == 'd':
            #Reconocer Dia
            if c == '/':
                estado = 'm'
                day = aux
                aux = ''
            else:
                aux += c
            
            posicion += 1
        elif estado == 'm':
            #Reconocer Mes
            if c == '/':
                estado = 'y'
                month = aux
                aux = ''
            else:
                aux += c
            
            posicion += 1
        elif estado == 'y':
            if(posicion == len(entrada)):
                #Se termino la entrada
                aux += c
                year = aux
                aux = ''
            else:
                aux += c
            
            posicion += 1
        else:
            return None
    
    if (len(day) == 2 or len(day) == 1) and (len(month) == 2 or len(month) == 1) and (len(year) == 4):
        return [day, month, year]

    else:
        return None

def obtenerFechas(entrada):
    aux = ''
    posicion = 1
    
    for c in entrada:
        if(c != ';'):
            aux += c
            # Final de la linea que no tiene el ;
            if posicion == len(entrada):
                salida = regresarDatos(aux)
                if salida is None:
                    print('Error con el formato de la entrada, debe ser \'dd/MM/YYYY\'\n')
                    exit()
                else:
                    print(salida)
            posicion += 1
        else:
            tmp = aux
            aux = ''
            posicion += 1

            salida = regresarDatos(tmp)
            if salida is None:
                print('Error con el formato de la entrada, debe ser \'dd/MM/YYYY\'\n')
                exit()
            else:
                print(salida)

if __name__ == '__main__':
    #txt = input("Ingresar una fecha (dd/MM/YYYY): ")
    f = open("fechas.csv","r")
    txt = f.read()
    
    if txt == '':
        print('La entrada esta vacia, bye...\n')
    else:
        #print('La entrada es', end=' ')
        obtenerFechas(txt)
        print('\nPrograma Ejecutado con Exito')