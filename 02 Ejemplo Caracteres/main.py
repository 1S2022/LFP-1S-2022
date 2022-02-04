from tkinter import filedialog, Tk

lista = []

def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo",
        initialdir = "./",
        filetypes = (
            ("archivos LFP", "*.lfp"),
            ("todos los archivos",  "*.*")
        )
    )

    if archivo is None:
        print('No se selecciono ningun archivo\n')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        return texto

if __name__ == '__main__':
    lista = []
    txt = abrir()

    if txt is not None:
        # print(txt)
        if(len(txt) > 0):
            for c in txt:
                # print(c, end="\n")
                if c == '\n':
                    pass
                elif c == ' ':
                    pass
                else:
                    # print(c + " - " + str( ord(c) ))
                    listaAux = [ord(c), c]
                    lista.append(listaAux)
            for e in lista:
                print('Ascii: ' + str(e[0]) + ' - Caracter: ' + e[1])
        else:
            print('No hay texto :v F')
    else:
        print('No se puede procesar\n')