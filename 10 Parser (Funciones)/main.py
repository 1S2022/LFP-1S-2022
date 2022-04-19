# Cree una clase Token sencilla, la cual importamos
from token import Token

# Inicializamos una variable global que usaremos como lista de Tokens
listaToken = []

# Metodo que usaremos durante el lab para la explicacion
def showList():
    print("")
    for tk in listaToken:
        print(tk.token + ' - ' + tk.valor)

# Metodo que usaremos durante el lab para la explicacion
def showFirst():
    print("- - - - -")
    print(listaToken[0].token + ' - ' + listaToken[0].valor)
    print("- - - - -")

# Metodo donde ingresamos los token para el ejemplo
def llenarLista():
    # Ingresaremos los token para la cadena: ( ( 3 ) + 2 ) - 1
    listaToken.append(Token('par_(','('))
    listaToken.append(Token('par_(','('))
    listaToken.append(Token('num','3'))
    listaToken.append(Token('par_)',')'))
    listaToken.append(Token('mas','+'))
    listaToken.append(Token('num','2'))
    listaToken.append(Token('par_)',')'))
    listaToken.append(Token('menos','-'))
    listaToken.append(Token('num','1'))
    
    # Simbolo de aceptacion, la ingeniera suele usar el simbolo #, pero yo esta vez usare el ~
    listaToken.append(Token('fin','~'))

    # Estas son mausequerramientas que nos ayudaran mas tarde...
        #listaToken.append(Token('par_(','('))
        #listaToken.append(Token('par_)',')'))

# Produccion <S0> -> <E>
def inicio():
    return verif_E()

# Produccion <E> -> tk_num <E'> | par_( <E> par_) <E'>
def verif_E():
    if (listaToken[0].token == 'num'):
        # Saco el token de la lista para un uso posterior
        numero = listaToken.pop(0)
        # Mando a resolver la produccion de <E'> pasando como valor heredado el numero de la instruccion anterior
        return verif_EP(numero.valor)

    elif (listaToken[0].token == 'par_('):
        # El parentesis ( no nos aporta ningun valor a operar, por lo cual solo lo sacamos de la lista
        listaToken.pop(0)

        # Mando a resolver la produccion de <E>
        # Si se dan cuenta mando a llamar al mismo metodo donde me encuentro ahora == Recursividad
        res1 = verif_E()

        if(res1 != None):
            # En este caso no hubo error sintactico 
            if (listaToken[0].token == 'par_)'):
                # Nuevamente el otro parentesis no tiene ningun valor a operar asi que solo lo saco de la lista
                listaToken.pop(0)

                # Resuelvo el simbolo faltante de la produccion, y paso como valor heredado 
                # el resultado de <E> obtenido previamente
                return verif_EP(res1)
            else:
                print('Error, se detecto ' + listaToken[0].token + ' ( \'' + listaToken[0].valor + '\' ). Se esperaba tk_par)')
                return None
        else:
            print('Error encontrado dentro de E\'')
            return None
    else:
        print('Error Sintactico, se detecto ' + listaToken[0].token + ' ( \'' + listaToken[0].valor + '\' ). Se esperaba el tk_num o tk_par(')
        return None

# Produccion <E'> -> tk_mas <E> <E'> | tk_menos <E> <E'> | epsilon
def verif_EP(valor):
    # Como ya reconoci un numero antes, ahora debo de verificar si viene una operacion o no
    # en caso de que solo venga un numero iremos al else y solo regresaremos dicho numero.
    
    if (listaToken[0].token == 'mas'):
        # Si se detecta el tk_mas solo lo sacamos de la lista y damos por seguro de que tendremos que
        # sumar dos valores en un futuro proximo.
        listaToken.pop(0)

        # Antes de sumar tenemos que obtener el valor No. 2 asi que segun la gramatica debemos de
        # llamar nuevamente a la produccion donde cuya cabeza es <E>
        resE = verif_E()
        
        # Verificamos que <E> no nos haya devuelto algun error
        if(resE != None):
            # Ahora que ya tenemos los dos datos (el primero es el parametro de la funcion 
            # y el segundo esta en resE) realizamos la suma
            suma = int(valor) + int(resE)
            '''
            print(valor + ' + ' + resE + ' = ' + str(suma))
            '''
            
            # Ahora mandamos a llamar la produccion <E'> por si hay otra operacion que se deba realizar,
            # para  ello pasamos el resultado de la suma como valor heredado.
            return verif_EP(str(suma))

        else:
            print('Error encontrado dentro de E')
            return None

    elif (listaToken[0].token == 'menos'):
        # Si se detecta el tk_menos solo lo sacamos de la lista y damos por seguro de que tendremos que
        # restar dos valores en un futuro proximo.
        listaToken.pop(0)

        # Antes de restar tenemos que obtener el valor No. 2 asi que segun la gramatica debemos de
        # llamar nuevamente a la produccion donde cuya cabeza es <E>
        resE = verif_E()

        # Verificamos que <E> no nos haya devuelto algun error
        if(resE != None):
            # Ahora que ya tenemos los dos datos (el primero es el parametro de la funcion 
            # y el segundo esta en resE) realizamos la resta
            resta = int(valor) - int(resE)
            '''
            print(valor + ' - ' + resE + ' = ' + str(resta))
            '''
            
            # Ahora mandamos a llamar la produccion <E'> por si hay otra operacion que se deba realizar,
            # para  ello pasamos el resultado de la resta como valor heredado.
            return verif_EP(str(resta))

        else:
            print('Error encontrado dentro de E')
            return None
    else:
        # En este caso, y por la funcion de mi lenguaje, en el caso de epsilon
        # solo devuelvo el valor heredado que viene como parametro y no saco nada de la lista.
        # No siempre es asi, por lo que deben de adaptar esto a sus necesidades.
        return valor


if __name__ == '__main__':
    # Simularemos que ya se realizo el analiis lexico y ya tenemos
    # una lista de tokens para realizar el analisis sintactico
    listaToken = []
    llenarLista()

    # Mandamos a resolver la produccion inicial, la cual nos devolvera el valor de la operacion.
    # ( 3 + 2 ) - 1
    res = inicio()
    
    # Para mi los errores me devuelven un None
    if res == None:
        print('Error Sintactico')
        listaToken = []
    else:
        # Verifico que todos los token de la lista fueron leidos.
        if(listaToken[0].token == 'fin'):
            print('Se acepta la entrada')
            print('>> ' + str(res))
        else:
            showList()
            print('Algo salio mal con el analisis')