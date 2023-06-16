import hashlib as h
import os 

## Diccionario con todas las imágenes sin repetir a nivel de bytes.
set = {}
files = 0
dirs = 0


def leer_archivo(ruta):
    '''Lee un archivo en la ruta específicada como bytes.'''
    with open(ruta, "rb") as f: 
        ##read all file
        arch = f.read()
    return arch

def leer_carpeta(carpeta, rec = None):
    '''Lee todos los archivos que no son carpeta dentro de una ruta carpeta. Regresa una lista'''
    all = os.scandir(carpeta)
    global files
    global dirs
    for x in all:
        if x.is_file():
            evaluacion(x.path)
            files += 1
        elif rec == "-r" and x.is_dir():
            dirs += 1
            leer_carpeta(x.path + "/", rec)


def evaluacion(ruta):
    f = leer_archivo(ruta)
    hsh = h.sha256(f).hexdigest()
    if hsh in set:
        if (ruta != set[hsh]):
            print("Archivos duplicados: ", ruta, set[hsh])
    else:
        set[hsh] = ruta

    

def repr():
    for k in set.keys():
        print(f"'{k}': {set[k]}")

if __name__ == '__main__':
    
    leer_carpeta("../files/", "-r")
    #repr()
    print("files:", files)
    print("dirs:" , dirs)
    print(len(set.keys()))

