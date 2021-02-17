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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los canales y
    una lista vacia para las categorias. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               #'channel_title': None,
               'category-id': None}

    catalog['videos'] = lt.newList()
    #catalog['channel_title'] = lt.newList('ARRAY_LIST'),
                                    #cmpfunction=comparechannel)
    catalog['category-id'] = lt.newList('ARRAY_LIST')
                                 #cmpfunction=comparecategory)

    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], video)
    # Se obtienen los autores del libro
    #channel_title = video['channel_title'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    #for channel in channel_title:
        #addVideoChannel(catalog, channel.strip(), video)


#def addVideoChannel(catalog, channelname, video):
    """
    Adiciona un canal a lista de canales, la cual guarda referencias
    a los videos de dicho canal
    """
    #channel_title = catalog['channel_title']
    #poschannel = lt.isPresent(channel_title, channelname)
    #if poschannel > 0:
        #channel = lt.getElement(channel_title, poschannel)
    #else:
        #channel = newChannel(channelname)
        #lt.addLast(channel_title, channel)
    #lt.addLast(channel['videos'], video)


def addCategory(catalog, category_):
    """
    Adiciona una catagoria a la lista de categorias
    """
    #c = newVideoCategory(category_['name'], category_['id'])
    lt.addLast(catalog['category-id'], category_)
    


# Funciones para creacion de datos
#def newChannel(name):
    """
    Crea una nueva estructura para modelar los videos de
    un canal
    """
    #channel = {'name': "", "books": None}
    #channel['name'] = name
    #channel['videos'] = lt.newList('ARRAY_LIST')
    #return channel


#def newVideoCategory(name, id):
    """
    Esta estructura almancena las categorias utilizadas para marcar videos.
    """
    #cat = {'name': '', 'tag_id': ''}
    #cat['name'] = name
    #cat['tag_id'] = id
    #return cat


#def newBookTag(cat_id, video_id):
    """
    Esta estructura crea una relación entre una categoria y
    los videos que han sido marcados con dicho cat.
    """
    #category_ = {'id': tag_id, 'video_id': video_id}
    #return category_

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento