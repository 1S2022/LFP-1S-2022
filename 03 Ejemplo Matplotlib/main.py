import matplotlib.pyplot as plt

# Datos Gráfica de Barras
ejeXB = ['Alberto','Kevin','María','Josué','Carolina','Michelle']
ejeYB = [100, 75, 105, 59, 73, 68]
# Datos Gráfica de Líneas
ejeXL = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado']
ejeYL = [100*3, 75*3, 105*3, 59*3, 73*3, 68*3]

plt.rcdefaults()
figB, axB = plt.subplots()
figL, axL = plt.subplots()

# GRÁFICA DE BARRAS
axB.bar(ejeXB, ejeYB) # Datos de los ejes de la gráfica de barras, se usa función bar()

axB.set_xlabel('Empleados') # Titulos de los ejes
axB.set_ylabel('Llamadas')

axB.grid(axis='y', color='lightgray', linestyle='dashed')
axB.set_title('Desempeño x Empleado Call-Center')
# -------------------------------------------------------

# GRÁFICA DE LÍNEAS
axL.plot(ejeXL, ejeYL) # Configuración de los ejes de la gráfica de lineas, se usa función plot()

# Titulos de los ejes
axL.set_xlabel('Días Laborados', fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'blue'})
axL.set_ylabel('Llamadas', fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'red'})

axL.grid(axis='y', color='darkgray', linestyle='dashed')
axL.set_title('Desempeño General Call-Center')
# -------------------------------------------------------

#plt.show()
figB.savefig('./graficaBarras.png')
figL.savefig('./graficaLineas.png')