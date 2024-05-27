from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
import os

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Rutas de los archivos
ruta_clubs = os.path.join("data", "datos_clubs.txt")
ruta_jugadores = os.path.join("data", "datos_jugadores.txt")

# Función para procesar el archivo de clubs
def procesar_clubs():
    with open(ruta_clubs, 'r') as file:
        for line in file:
            datos = line.strip().split(';')
            club = Club(nombre=datos[0], deporte=datos[1], fundacion=int(datos[2]))
            session.add(club)

# Función para procesar el archivo de jugadores
# Función para procesar el archivo de jugadores
def procesar_jugadores():
    with open(ruta_jugadores, 'r') as file:
        for line in file:
            datos = line.strip().split(';')
            if len(datos) >= 4:  # Verifica que la lista tenga al menos 4 elementos
                club = session.query(Club).filter_by(nombre=datos[0]).first()
                if club:
                    jugador = Jugador(nombre=datos[3], dorsal=int(datos[2]), posicion=datos[1], club=club)
                    session.add(jugador)
            else:
                print("Error: La línea no tiene suficientes elementos:", line)



# Procesamiento de los archivos y guardado en la base de datos
procesar_clubs()
procesar_jugadores()

# Confirmación de las transacciones
session.commit()
