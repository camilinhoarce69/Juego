import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    intentos = 6

    while numero_aleatorio != numero_elegido:

        if numero_elegido < numero_aleatorio:
            numero_elegido = int(input('busca un numero mas grande: '))
            intentos -= 1

        if numero_elegido > numero_aleatorio:
            numero_elegido = int(input('busca un numero mas pequeño: '))
            intentos -= 1

        if intentos == 0:
            print('Game Over')
            print('el numero aleatorio era: ' + str(numero_aleatorio))
            break

        if numero_aleatorio == numero_elegido:
            print('¡Ganaste!')
            break



if __name__ == '__main__':
    run()