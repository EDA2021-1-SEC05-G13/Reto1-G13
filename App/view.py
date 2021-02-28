"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Sub lista ordenada de videos con mas views")
    print("3- ")
    print("4- ")
    print("5- ")

def initCatalog(parametro): 
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(parametro) 

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printResults(ord_videos, sample=10): 
    size = lt.size(ord_videos) 
    if size >= sample: 
        print("Los primeros ", sample, " videos ordenados son:") 
        i=0 
        while i <= sample: 
            videos = lt.getElement(ord_videos,i) 
            print("Titulo: {0} Views: {1} ".format(videos['title'],videos['views'])) 
            i+=1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        parametro = int(input(("Escoja un tipo de lista para representar el catalogo: \n 1. LINKED_LIST \n 2. ARRAY_LIST\n")))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(parametro)    
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargados: ' + str(lt.size(catalog['category-id'])))

    elif int(inputs[0]) == 2:
        sort = int(input(("Escoja que tipo de algoritmo de ordenamiento desea implementar: \n 1. Selection sort \n 2. Insertion sort\n 3. Shell sort\n 4. Merge sort\n 5. Quick sort\n")))
        size = input("Indique tamaño de la muestra: ") 
        result = controller.sortVideos(catalog, int(size), sort) 
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0])) 
        printResults(result[1])

    elif int(inputs[0]) == 3:
        t4= time.process_time()
        print("Se realizo req 2")
        t5 = time.process_time()
        print(t5-t4)

    elif int(inputs[0]) == 4:
        t6= time.process_time()
        print("Se realizo req 3")
        t7 = time.process_time()
        print(t7-t6)
    
    elif int(inputs[0]) == 5:
        pass
    
    else:
        sys.exit(0)
sys.exit(0)
