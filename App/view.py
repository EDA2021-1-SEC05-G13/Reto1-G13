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
    print("2- Encontrar buenos videos por categoria y pais")
    print("3- Encontrar video tendencia por pais")
    print("4- Encontrar el video con mas dias como tendencia segun una categoria")
    print("5- Encontrar videos con mas likes")

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

def printResults(ord_videos, sample): 
    size = lt.size(ord_videos) 
    if size >= sample: 
        print("Los primeros ", sample, " videos ordenados son:") 
        i=1 
        while i <= sample: 
            videos = lt.getElement(ord_videos,i) 
            print("Trending Date: {0} Titulo: {1} Channel Title {2} Publish Time: {3} Views: {4} Likes: {5} Dislikes: {6}".format(videos['trending_date'],videos['title'],videos['channel_title'],videos['publish_time'],videos['views'],videos['likes'],videos['dislikes'])) 
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
        size = int(input("Indique tamaño de la muestra: "))
        catid = " " + str(input("Escriba el nombre de la categoria: "))
        country = str(input("Indique el pais en el que desea buscar: "))
        result = controller.sortVideosCountry(catalog, catid, country)
        printResults(result, size)

    elif int(inputs[0]) == 3:
        sort = int(input("Escoja que tipo de algoritmo de ordenamiento desea implementar: \n 1. Selection sort \n 2. Insertion sort \n 3. Shell sort \n 4. Merge sort \n 5. Quick sort \n"))
        size = int(input("Indique el tamaño de la muestra "))
        country = str(input("Indique el pais que desea buscar: "))
        result = controller.sortVideoPais(country)
        printResults(result, size)

    elif int(inputs[0]) == 4:
        cat = " " + str(input("Escriba el nombre de la categoria: "))
        trending_video = controller.trendingVideo(catalog, cat)
        printResults(trending_video, size)
    
    elif int(inputs[0]) == 5:
        sort = int(input("Escoja que tipo de algoritmo de ordenamiento desea implementar: \n 1. Selection sort \n 2. Insertion sort \n 3. Shell sort \n 4. Merge sort \n 5. Quick sort \n"))
        size = int(input("Indique el tamaño de la muestra"))
        country = str(input("Indique el país que desea buscar: "))
        n = int(input("Indique el número de videos que desea enlistar: "))
        tag = " " + str(input("Indique el/los tag/s que desea buscar: "))
        result = controller.sortVideoLike(country, n, tag)
        printResults(result, size)
        
    else:
        sys.exit(0)
sys.exit(0)
