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
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qu
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

    if parametro==1:
        catalog['videos'] = lt.newList('SINGLE_LINKED', 
                                   cmpfunction=cmpVideosByViews) 
        catalog['category-id'] = lt.newList('SINGLE_LINKED',
                                  cmpfunction=None) 

    elif parametro == 2:
        catalog['videos'] = lt.newList('ARRAY_LIST', 
                                   cmpfunction=cmpVideosByViews) 
        catalog['category-id'] = lt.newList('ARRAY_LIST', 
                                    cmpfunction=None) 


    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category_):
    """
    Adiciona una catagoria a la lista de categorias
    """
    lt.addLast(catalog['category-id'], category_)
    
def findCat(catalog, cat):
    tam = lt.size(catalog['category-id'])
    i = 1
    while i <= tam:
        categories = lt.getElement(catalog['category-id'], i)
        if cat == str(categories ['name']):
            numid = categories['id']
            return numid
        else:
            pass
        i+=1

def cmpVideosByViews(video1, video2):
    if(int(video1['views']) < int (video2['views'])):
        return False
    elif(int(video1['views']) > int (video2['views'])):
        return True
    else:
        if(int(video1['likes']) < int(video2['likes'])):
            return False
        elif(int(video1['likes']) > int(video2['likes'])):
            return True

def cmpVideosById(video1, video2):
    if(str(video1['video_id']) < str(video2['video_id'])):
        return False
    elif(str(video1['video_id']) > str(video2['video_id'])):
        return True

def cmpVideosByTD(video1, video2):
    if(int(video1['trending days']) < int(video2['trending days'])):
        return False
    elif(int(video1['trending days']) > int(video2['trending days'])):
        return True

def cmpVideoByTag(video1, video2):
    if(int(video1['tags']) < int(video2['tags'])):
        return False
    elif(int(video1['tags']) > int(video2['tags'])):
        return True
    else:
        if(int(video1['likes']) < int(video2['likes'])):
            return False
        elif(int(video1['likes']) > int(video2['likes'])):
            return True

def sortVideos(catalog):
    sub_list = catalog.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByViews) 
    return sorted_list

def sortById(catalog):
    sub_list = catalog.copy()
    sorted_list = mer.sort(sub_list, cmpVideosById)
    return sorted_list

def sortByTD(catalog):
    sub_list = catalog.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByTD)
    return sorted_list

def sortVideosByCountry(catalog, catid, country):
    siz = lt.size(catalog['videos'])
    i = 1 
    lst = lt.newList('ARRAY_LIST', cmpVideosByViews)
    id_ = findCat(catalog,catid)
    while i <= siz: 
        videos = lt.getElement(catalog['videos'],i) 
        if videos['country'] == country and videos['category_id'] == id_:
            lt.addLast(lst, videos)
        else:
            pass
        i+=1
    ordered_videosByCat = sortVideos(lst)
    return ordered_videosByCat

def sortVideoPais(country)
    siz = lt.size(catalog['videos'])
    i = 1
    lst = lt.newList('ARRAY_LIST', cmpVideosByTD)
    while i <= siz:
        videos = lt.getElement(catalog['videos'], i)
        if videos['country'] == country :
            lt.addLast(lst, videos)
        else:
            pass
        i+=1
    ordered_videosCoun = sortVideos(lst)
    return ordered_videosCoun        

def sortVideoLike(country, n, tag)
    size = lt.size(catalog['videos'])
    i = 1
    lst = lt.newList('ARRAY_LIST', cmpVideoByTag)
    while i <= size:
        videos = lt.getElement(catalog['videos'], i)
        if (videos['country'] == country, 'n'== n, videos['tags'] == tag):
            lt.addLast(lst, videos)
        else:
            pass
        i+=1
    ordered_videosLike = sortVideos(lst)
    return ordered_videosLike        


def trendingVid(catalog, cat):
    
    id_ = findCat(catalog,cat)
    lst = videosByCat(catalog, id_)
    lst_ord = sortById(lst)
    tam = lt.size(lst_ord)
    f_lt = lt.newList('ARRAY_LIST')
    vid = lt.getElement(lst_ord, 0)
    vid['trending days'] = 1 
    lt.addLast(f_lt, vid)
    j = 0
    y = 0

    while y <= tam:
        if lt.getElement(lst_ord, y)['video_id'] == lt.getElement(f_lt,j)['video_id']:
            lt.getElement(f_lt,j)['trending days'] += 1
            y+=1
        else:
            lt.getElement(lst_ord, y)['trending days'] = 1
            lt.addLast(f_lt, lt.getElement(lst_ord,y))
            y+=1
            j+=1
 
    list_orderedByTD = sortByTD(f_lt)
    return list_orderedByTD

def videosByCat (catalog, cat):
    size = lt.size(catalog['videos'])
    dic = lt.newList('ARRAY_LIST', cmpVideosByViews)
    i = 1
    while i <= size:
        videos = lt.getElement(catalog['videos'], i) 
        if videos['category_id'] == cat:
            lt.addLast(dic, videos)
        else:
            pass
        i+=1
    
    return dic



