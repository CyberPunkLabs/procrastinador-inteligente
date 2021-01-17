## Procrastinador inteligente
¿Despiertas los lunes con muchas ganas de procrastinar, pero el trabajo te lo impide?<br>
¿Te gustaría mejorar tus tiempos y la calidad de tu procrastinación, pero inevitablemente terminas dedicándole mucho tiempo al trabajo?<br><br>

El Procrastinador inteligente utiliza el método de trabajo eficiente recomendado por Thomas Jefferson y Richard Feynman, pero al revés: programa la cantidad de minutos en que quieres procrastinar y la cantidad de minutos en que quieres trabajar: el procrastinador inteligente emite un sonido en los tiempos de transición entre trabajo y descanso (una alarma y un ruido de bosque, respectivamente), para que procrastines con eficiencia.<br><br>

Versión actual para Linux. Pronto versión para Windows.<br>

Copyleft Laboratorios CyberPunk<br>
Úsalo y distribúyelo a tu antojo.

## Linux
### Requiere
```
pip3 install playsound
```

#### Uso
```
python3 main.py
```

#### Entrega
```
##########
Configuración actual:
Tiempo de trabajo: 20.0 min
Tiempo de descanso: 10.0 min

Enter para aceptar
M para modificar


Descansa...
Iteración # 1
El tiempo de descanso finaliza en 10 s...

¡Trabaja!
El tiempo de trabajo finaliza en 1 min...


Descansa...
Iteración # 2
El tiempo de descanso finaliza en 10 s...

¡Trabaja!
El tiempo de trabajo finaliza en 1 min...


Descansa...
Iteración # n
El tiempo de descanso finaliza en 10 s...

¡Trabaja!
El tiempo de trabajo finaliza en 1 min...


```

## Windows
Por implementar...

## Cómo funciona
Revisa aquí el tutorial Python: De saber nada a saber algo en 15 minutos, o estos excelentes tutoriales:

El código explicado:

### Código
Primero importas los módulos. Time permite pausar la ejecución del programa por 2 segundos, pickle guardar y cargar la configuración de usuario y playsound permite hacer sonar un sonido.

```
#!/usr/bin/env python3

import time
import pickle
from playsound import playsound
```

Carga últimos parámetros con pickle:
```
try:
    parametros = pickle.load(open('parametrosActuales.config', 'rb'))
except FileNotFoundError:
    parametros = {'work': 20, 'descanso': 10}
    
```

crea variables con los tiempos de trabajo y descanso cargándolos (de existir) desde archivo con los últimos parámetros, y los imprime en la pantalla.
```
work = parametros['work']
descanso = parametros['descanso']
    
print("\n\n################\n¡Bienvenido!\n#################")
print("\n### Configuración actual:")
print("Tiempo de trabajo (minutos): {}".format(work))
print("Tiempo de descanso (minutos): {}".format(descanso))

```

pregunta si aceptar los parámetros actuales, u modificarlos por nuevos:
```
while True:
    opcion = input("\nEnter para aceptar\nM para modificar ").lower()
    
    if opcion in ["", "m"]:
        break
    else:
        print("¡Opción incorrecta!")
        time.sleep(2)

```
si la opción es enter (aceptar), simplemente sigue de largo; si la opción es "m" (modificar), pide ingresar los datos:

```      
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

    pickle.dump(dict(work=work, descanso=descanso), open('parametrosActuales.config', 'wb'), protocol=2)

    print("\n### Configuración actual:")
    print("Tiempo de trabajo (minutos): {}".format(work))
    print("Tiempo de descanso (minutos): {}".format(descanso))
            

```

define el loop que itera entre tiempos de trabajo y descanso:
```
iteracion = 1
print("\n¡Trabaja!\nIteración # {}".format(iteracion))
#playsound('alarma.mp3')

while True:
    # Tiempo de trabajo
    time.sleep((work - 1) * 60) 
    print("El tiempo de trabajo finaliza en 1 min...")
    playsound('bosque.mp3')

    # Tiempo de descanso
    print("\nDescansa...")
    print("El tiempo de descanso finaliza en 10 s...")
    time.sleep((rest * 60) - 10)     
    playsound('alarma.mp3')
    iteración += 1

    # Nueva iteración
    print("\n¡Trabaja!\nIteración # {}".format(iteración))

```




