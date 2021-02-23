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
    print("4- Encontrar video tendencia por categoria")
    print("5- Buscar videos con mas likes")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargados: ' + str(lt.size(catalog['category-id'])))

    elif int(inputs[0]) == 2:
        t1= time.process_time()
        print("Se realizo req 1")
        t2 = time.process_time()
        print(t2-t1)

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
        t8= time.process_time()
        print("Se realizo req 4")
        t9 = time.process_time()
        print(t9-t8)
    
    else:
        sys.exit(0)
sys.exit(0)
