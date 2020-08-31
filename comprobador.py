#!/usr/bin/python
import psycopg2
from configparser import ConfigParser

def readConfig(archivo='config.ini', seccion='postgresql'):
    parser = ConfigParser()# Crear el parser y leer el archivo
    parser.read(archivo)
    db = {}# Obtener la sección de conexión a la base de datos
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            db[param[0]] = param[1]
        return db
    else:
        raise Exception('La secccion {0} no encontrada en el archivo {1}'.format(seccion, archivo))
    
def conectarDB():
    conexion = None
    try:
        params = readConfig()# Lectura de los parámetros de conexion
        print('Conectando a la base de datos PostgreSQL...')
        conexion = psycopg2.connect(**params)
        cur = conexion.cursor()
        print('La version de PostgreSQL es la:')
        cur.execute('SELECT version()')
        version = cur.fetchone()
        print(version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conexion is not None:
            conexion.close()
            print('Conexión finalizada.')
 
 
if __name__ == '__main__':
    conectarDB()