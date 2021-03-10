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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def initCatalog(parametro): 
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(parametro) 
    return catalog

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):
    """
    Carga los videos del archivo.  Por cada video se toma su canal y por
    cada uno de ellos, se crea en la lista de canales, a dicho canal y una
    referencia al video que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'), delimiter=',')
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategories(catalog):
    """
    Carga todos las categorias del archivo y los agrega a la lista de categorias
    """
    categoriasfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoriasfile, encoding='utf-8'), delimiter='\t')
    for cat in input_file:
        model.addCategory(catalog, cat)


# Funciones de ordenamiento
def sortVideos(catalog, size, sort):
    """
    Ordena los videos por views
    """
    return model.sortVideos(catalog, size, sort)

def sortVideosCountry(catalog, catid, country):
    return model.sortVideosByCountry(catalog, catid, country)

# Funciones de consulta sobre el catálogo

def trendingVideo(catalog, cat):
    return model.trendingVid(catalog, cat)