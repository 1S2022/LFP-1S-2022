import matplotlib.pyplot as plt
from pymysql import NULL
plt.rcdefaults()

class Producto:
    def __init__(self, n, p, c, i) -> None:
        self.nombre = n
        self.precio = p
        self.cantidad = c
        self.ingresos = i

nombreMes, year, nombreImg, tipoGrafica, titulo, ejeX, ejeY = '','','','','','',''
listaProductos, listaNombres, listaIngresos = [],[],[]

def analizarDATA():
    global listaProductos

    archivo = open('C:\\Users\\Douglas\\Desktop\\LFP-1S-2022\\04 Ejemplo de Análisis y Autómata\\Práctica 1\\prod_2.data', 'r', encoding="utf-8")
    data = archivo.read()
    archivo.close()
    del archivo

    obtenerDatos(data)
    del data
    
    aux = []
    for p in listaProductos:
        listaNombres.append(p[0])
        listaIngresos.append(round(p[1] * p[2], 2))
        aux.append(Producto(p[0], p[1], p[2], round(p[1] * p[2], 2)))
    del p

    listaProductos = aux
    del aux

def analizarLFP():
    global nombreImg, tipoGrafica, titulo, ejeX, ejeY

    archivo = open('C:\\Users\\Douglas\\Desktop\\LFP-1S-2022\\04 Ejemplo de Análisis y Autómata\\Práctica 1\\inst_3.lfp', 'r', encoding="utf-8")
    data = archivo.read()
    archivo.close()
    del archivo

    contenido = data.split("¿")[1].split("?")[0]
    del data

    junto = juntar(contenido)
    del contenido
    
    instrucciones = junto.split(',')
    del junto

    for i in instrucciones:
        icv = i.split(":")
        if icv[0].lower() == 'nombre':
            nombreImg = icv[1].replace('"', '')
        elif icv[0].lower() == 'grafica':
            tipoGrafica = icv[1].replace('"', '')
        elif icv[0].lower() == 'titulo':
            titulo = icv[1].replace('"', '')
        elif icv[0].lower() == 'titulox':
            ejeX = icv[1].replace('"', '')
        elif icv[0].lower() == 'tituloy':
            ejeY = icv[1].replace('"', '')
    del i
    
    # Valor por default
    if titulo == '':
        titulo = 'Reporte de Ventas ' + nombreMes + ' - ' + year

def obtenerDatos(texto):
    global nombreMes,  year, listaProductos

    # Split primiario
    noIgual = texto.split('=')

    # Dividir Nombre:Year
    ny = noIgual[0].split(':')
    nombreMes = ny[0].replace(" ", "")
    year = ny[1].replace(" ", "")

    # Obtener datos
    contenido = noIgual[1]
    junto = juntar(contenido)

    productos = junto.split(';')
    productos.pop(len(productos) - 1)
    listaProductos = []
    for pr in productos:
        listaProductos.append(eval(pr))

def juntar(cont):
    auxNoBlanks = ''
    estado = 0
    for c in cont:
        if c == '\n' or c == '\t' or c == '(' or c == ')':
            pass
        else:
            if estado == 0 and c != ' ':
                auxNoBlanks += c
                if c == '\"':
                    estado = 1
            elif estado == 1:
                auxNoBlanks += c
                if c == '\"':
                    estado = 0
    
    return auxNoBlanks

def burbuja(arreglo):
    for i in range(len(arreglo)):
        for j in range(len(arreglo) - 1):
            if arreglo[j].ingresos < arreglo[j + 1].ingresos:
                arreglo[j + 1], arreglo[j] = arreglo[j], arreglo[j + 1]

def showValuePie(vals):
    def string(pct):
        total = sum(vals)
        val = round(pct*total/100.00)
        return '{v:.2f}'.format(v=val)
    return string

def graficar():
    fig, ax = plt.subplots()
    
    if tipoGrafica.lower() == 'barras' or tipoGrafica.lower() == 'lineas':
        if tipoGrafica.lower() == 'barras':
            ax.bar(listaNombres, listaIngresos)
        elif tipoGrafica.lower() == 'lineas':
            ax.plot(listaNombres, listaIngresos)

        ax.set_xlabel(ejeX)
        ax.set_ylabel(ejeY)
        ax.grid(axis='y', color='lightgray', linestyle='dashed')
        plt.draw()
        
        for tick in ax.get_xticklabels():
            tick.set_rotation(90)
    elif tipoGrafica.lower() == 'pie':
        ax.pie(listaIngresos, labels=listaNombres, autopct=showValuePie(listaIngresos))
        plt.axis('equal')

    ax.set_title(titulo)

    fig.savefig('C:\\Users\\Douglas\\Desktop\\LFP-1S-2022\\04 Ejemplo de Análisis y Autómata\\Práctica 1\\' + nombreImg + '.png')

if __name__ == '__main__':
    nombreMes, year, nombreImg, tipoGrafica, titulo, ejeX, ejeY = '','','','','','',''
    listaProductos, listaNombres, listaIngresos = [],[],[]

    # Archivo .data
    analizarDATA()
    burbuja(listaProductos)
    #print('\tNOMBRE - INGRESOS (PRECIO, CANTIDAD)')
    #for pr in listaProductos:
    #    print('\t\t' + pr.nombre + ' - ' + str(pr.ingresos) + ' (' + str(pr.precio) + ', ' + str(pr.cantidad) + ')')

    # Archivo .lfp
    analizarLFP()

    # Graficas
    graficar()

    # Mayor y Menor
    mayor = NULL
    menor = NULL
    for e in listaProductos:
        if mayor == NULL:
            mayor = e
            menor = e
        else:
            # Es Mayor?
            if e.cantidad > mayor.cantidad:
                mayor = e
            # Es Menor?
            if e.cantidad < menor.cantidad:
                menor = e
    
    print('El producto mas vendido es: ' + mayor.nombre + ' con ' + str(mayor.cantidad) + ' unidades.')
    print('El producto menos vendido es: ' + menor.nombre + ' con ' + str(menor.cantidad) + ' unidades.')
