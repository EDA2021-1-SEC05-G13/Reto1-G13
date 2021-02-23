"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(parametro): 
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los canales y
    una lista vacia para las categorias. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'category-id': None}

    catalog['videos'] = lt.newList(parametro, 
                                   cmpfunction=cmpVideosByViews) 
    catalog['category-id'] = lt.newList(parametro) 

    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category_):
    """
    Adiciona una catagoria a la lista de categorias
    """
    lt.addLast(catalog['category-id'], category_)
    


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
    if(int(video1['views']) < int (video2['views'])):
        return true
# Funciones de ordenamiento

def sortVideos(catalog, size):
    sub_list = lt.subList(catalog ['videos'], 0, size)
    sub_list = sub_list.copy()
    time1 = time.process_time()
    sorted_list = sa.sort(catalog, cmpVideosByViews)
    time2 = time.process_time()
    time3 = (time2 - time1) * 1000
    return time3, sorted_list