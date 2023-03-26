import csv
import interfaz
import random



def leer_palabra_secreta(csvfilename):
    with open(csvfilename)as text_csv:
        list_secret=list(csv.DictReader(text_csv))
        palabra_secreta=random.choice(list_secret)
        return palabra_secreta['palabras']
    
def pedir_letra(letras_usadas): 
    while True: 
        # ingreso de nueva letra tranformando todo a minusculo. 
        entrada_user = str(input("para jugar ingrese una letra..")).lower()
        # el metodo isalpha() se verifica que sea una letra.
        if  (entrada_user.isalpha()) == False:
            print("Error, debe ingrresar una letra intenta nuevamente..\n")
        # el operador in verifico si la letra ya fue ingresada 
        elif entrada_user in  letras_usadas:
            print("Esta letra ya fue usada, intenta con una diferente...\n")
        # la funcion len verificamos la cantidad de letras ingressados       
        elif len(entrada_user) > 1 :
             print("solo se permite el ingreso de una letra ingrersela nuevamnete..\n")   
        else:
        # se agregan las letras a la lista utilizando append()
            letras_usadas.append(entrada_user)
            return entrada_user
        

def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        return True
    else:
        return False
    

def validar_palabra(letras_usadas, palabra_secreta):
    for i in palabra_secreta:
        if i in letras_usadas:
          return True
        else:
             return False
        

if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.

    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)
        
       
        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')