#!/usr/bin/env python3
import os
import time
import pickle
from playsound import playsound

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# NOTE: which('pip3') returns #'/usr/bin/pip3'

#try:
#    subprocess.call(["wget", "your", "parameters", "here"])
#except FileNotFoundError:
#    # handle file not found error.

#try:
#    import time
#    print("module 'time' is installed")
#except ModuleNotFoundError:
#    print("module 'time' is not installed")
#    install("time") # the install function from the question



try:
    parametros = pickle.load(open('configuracion/parametrosActuales.config', 'rb'))
except FileNotFoundError:
    parametros = {'previa': 5, 'work': 20, 'descanso': 10}

previa = parametros['previa']
work = parametros['work']
descanso = parametros['descanso']
    
print("############################")
print("#         BIENVENIDO       #")
print("#  Copyleft CyberpunkLabs  #")
print("# cyberpunklabs.github.io  #")
print("############################")
print("\n### Configuración actual:")
print("Previa (minutos): {}".format(previa))
print("Tiempo de trabajo (minutos): {}".format(work))
print("Tiempo de descanso (minutos): {}".format(descanso))

while True:
    opcion = input("\nEnter para aceptar\nM para modificar ").lower()
    
    if opcion not in ["", "m"]:
        print("¡Opción incorrecta!")
        time.sleep(2)        
    else:
        break

      
if opcion == "":
    pass

elif opcion == "m":
    while True:
        opcion = input("Previa (minutos): ")
        try:
            previa = float(opcion)
            break
        except ValueError:
            print("\nERROR:")
            print(previa + " no es un número.\n¡Debes ingresar un número!\n")
            time.sleep(2)

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

    pickle.dump(dict(previa=previa, work=work, descanso=descanso), open('configuracion/parametrosActuales.config', 'wb'), protocol=2)

    print("\n### Configuración actual:")
    print("Previa (minutos): {}".format(previa))
    print("Tiempo de trabajo (minutos): {}".format(work))
    print("Tiempo de descanso (minutos): {}".format(descanso))

iteracion = 1
print("\nPrevia...")
# Tiempo de trabajo
time.sleep((previa - 1) * 60) 
print("La previa finaliza en 1 min...")
playsound('sonidos/bosque.mp3')

print("\n¡Trabaja!\nIteración # {}".format(iteracion))
playsound('sonidos/alarma.mp3')

while True:
    # Tiempo de trabajo
    time.sleep((work - 1) * 60) 
    print("El tiempo de trabajo finaliza en 1 min...")
    playsound('sonidos/bosque.mp3')

    # Tiempo de descanso
    print("\nDescansa...")
    print("El tiempo de descanso finaliza en 10 s...")
    time.sleep((descanso * 60) - 10)     
    playsound('sonidos/alarma.mp3')
    iteracion += 1

    # Nueva iteración
    print("\n¡Trabaja!\nIteración # {}".format(iteracion))

