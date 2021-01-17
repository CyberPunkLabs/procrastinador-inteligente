#!/usr/bin/env python3

import time
import pickle
from playsound import playsound

try:
    parametros = pickle.load(open('configuracion/parametrosActuales.config', 'rb'))
except FileNotFoundError:
    parametros = {'work': 20, 'descanso': 10}
    
work = parametros['work']
descanso = parametros['descanso']
    
print("\n\n################\n¡Bienvenido!\n#################")
print("\n### Configuración actual:")
print("Tiempo de trabajo (minutos): {}".format(work))
print("Tiempo de descanso (minutos): {}".format(descanso))

while True:
    opcion = input("\nEnter para aceptar\nM para modificar ").lower()
    
    if opcion in ["", "m"]:
        break
    else:
        print("¡Opción incorrecta!")
        time.sleep(2)

      
if opcion == "":
    pass

elif opcion == "m":
    while True:
        work = input("Tiempo de trabajo (minutos): ")
        try:
            work = float(work)
            break
        except ValueError:
            print("\nERROR:")
            print(work + " no es un número.\n¡Debes ingresar un número!\n")
            time.sleep(2)

    while True:
        descanso = input("Tiempo de descanso (minutos): ")
        try:
            descanso = float(descanso)
            break
        except ValueError:
            print("\nERROR:")    
            print(descanso + " no es un número.\n¡Debes ingresar un número!\n")
            time.sleep(2)

    pickle.dump(dict(work=work, descanso=descanso), open('configuracion/parametrosActuales.config', 'wb'), protocol=2)

    print("\n### Configuración actual:")
    print("Tiempo de trabajo (minutos): {}".format(work))
    print("Tiempo de descanso (minutos): {}".format(descanso))

iteracion = 1
print("\n¡Trabaja!\nIteración # {}".format(iteracion))

while True:
    # Tiempo de trabajo
    time.sleep((work - 1) * 60) 
    print("El tiempo de trabajo finaliza en 1 min...")
    playsound('sonidos/bosque.mp3')

    # Tiempo de descanso
    print("\nDescansa...")
    print("El tiempo de descanso finaliza en 10 s...")
    time.sleep((rest * 60) - 10)     
    playsound('sonidos/alarma.mp3')
    iteración += 1

    # Nueva iteración
    print("\n¡Trabaja!\nIteración # {}".format(iteración))

