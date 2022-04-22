from simbolos import Terminal, noTerminal

entrada = []
pila = []

def showList():
    for tk in entrada:
        print("| " + tk.token + ' - "' + tk.valor, end='" ')
    print("|")

def showFirst():
    print("\n- - FIRST - -")
    if(len(entrada) > 0):
        print(entrada[0].token + ' - "' + entrada[0].valor + '"')
    else:
        print("")
    print("- - - - - - -")

def showStack():
    print("- - - - - - - - - -")
    for i in range(len(pila) - 1, -1, -1):
        if(isinstance(pila[i], noTerminal)):
            print("->> <" + pila[i].nombre + ">")
        elif(isinstance(pila[i], Terminal)):
            print("->> " + pila[i].token + " - " + pila[i].valor)
    print("- - - - - - - - - -")

def showTop():
    print("- - - TOP - - -")
    if(len(pila) > 0):
        if(isinstance(pila[len(pila) - 1], noTerminal)):
            print("<" + pila[len(pila) - 1].nombre + ">")
        elif(isinstance(pila[len(pila) - 1], Terminal)):
            print(pila[len(pila) - 1].token + " - " + pila[len(pila) - 1].valor)
    else:
        print("")
    print("- - - - - - - -")

def llenarEntrada():
    entrada.append(Terminal('tk_id','Datos'))
    entrada.append(Terminal('tk_igual','='))
    entrada.append(Terminal('tk_num','5'))
    entrada.append(Terminal('tk_coma',','))
    entrada.append(Terminal('tk_num','7'))
    entrada.append(Terminal('tk_coma',','))
    entrada.append(Terminal('tk_num','1'))
    entrada.append(Terminal('tk_ord','Ordenar'))
    entrada.append(Terminal('tk_coma',','))
    entrada.append(Terminal('tk_bus','Buscar'))
    entrada.append(Terminal('tk_num','3'))
    entrada.append(Terminal('aceptacion','#'))

def removeFirst():
    # Se puede usar el metodo pop(0)
    global entrada
    aux = []
    for i in range(1, len(entrada)):
        aux.append(entrada[i])
    entrada = aux

def parsear():
    estado = 'i'

    while(True):
        if(estado == 'i'):
            # Paso 3
            pila.append(Terminal('aceptacion','#'))
            estado = 'p'
        elif(estado == 'p'):
            # Paso 4
            pila.append(noTerminal("inicio"))
            estado = 'q'
        elif(estado == 'q'):
            # Paso 5, sustityo producciones N -> w, saco N e ingreso w
            if(isinstance(pila[len(pila) - 1], noTerminal)):
                auxTope = pila.pop()

                if(auxTope.nombre == 'inicio'):
                    print('inicio')
                    pila.append(noTerminal("otra_lista"))
                    pila.append(noTerminal("lista"))

                elif(auxTope.nombre == 'lista'):
                    print('lista')
                    pila.append(noTerminal("acciones"))
                    pila.append(noTerminal("elementos"))
                    pila.append(Terminal("tk_igual",""))
                    pila.append(Terminal("tk_id",""))
                
                elif(auxTope.nombre == 'otra_lista'):
                    print('otra_lista')
                    if(entrada[0].token == 'tk_id'):
                        pila.append(noTerminal("inicio"))
                
                elif(auxTope.nombre == 'elementos'):
                    print('elementos')
                    pila.append(noTerminal("otro_num"))
                    pila.append(Terminal("tk_num",""))
                
                elif(auxTope.nombre == 'otro_num'):
                    print('otro_num')
                    if(entrada[0].token == 'tk_coma'):
                        pila.append(noTerminal("otro_num"))
                        pila.append(Terminal("tk_num",""))
                        pila.append(Terminal("tk_coma",""))
                
                elif(auxTope.nombre == 'acciones'):
                    print('acciones')
                    if(entrada[0].token == 'tk_bus'):
                        pila.append(noTerminal("ordenar"))
                        pila.append(Terminal("tk_num",""))
                        pila.append(Terminal("tk_bus",""))

                    elif(entrada[0].token == 'tk_ord'):
                        pila.append(noTerminal("buscar"))
                        pila.append(Terminal("tk_ord",""))
                    
                    elif(entrada[0].token != 'aceptacion'):
                        pila.append(auxTope)
                        return False
                
                elif(auxTope.nombre == 'ordenar'):
                    print('ordenar')
                    if(entrada[0].token == 'tk_coma'):
                        pila.append(Terminal("tk_ord",""))
                        pila.append(Terminal("tk_coma",""))
                
                elif(auxTope.nombre == 'buscar'):
                    if(entrada[0].token == 'tk_coma'):
                        pila.append(Terminal("tk_num",""))
                        pila.append(Terminal("tk_bus",""))
                        pila.append(Terminal("tk_coma",""))

            elif(isinstance(pila[len(pila) - 1], Terminal)):
                if(pila[len(pila) - 1].token != 'aceptacion'):
                    # Paso 6, por cada terminal listado se realiza la transicion: (terminalEntrada, terminalPila; epsilon)
                    if(entrada[0].token == pila[len(pila) - 1].token):
                        pila.pop()
                        removeFirst()
                    else:
                        print("error sintactico")
                        return False
                else:
                    # Paso 7
                    if(entrada[0].token == pila[len(pila) - 1].token):
                        print('Pop aceptacion')
                        pila.pop()
                        removeFirst()
                        estado = 'f'
        elif(estado == 'f'):
            return True

if __name__ == '__main__':
    # Simulamos el analisis lexico, y obtenemos la lista de tokens
    entrada = []
    pila = []
    llenarEntrada()
    #showList()

    if(parsear()):
        print('Se acepta la entrada')
    else:
        print('Error :v')