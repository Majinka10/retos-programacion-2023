""" * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia."""

import time


def comprobar_respuesta(longitud):
    # Recogemos la respuesta a través de un input, y comprobamos si está dentro del rango permitido.
    respuesta = input()
    opciones = ["1", "2", "3", "4"]
    opciones_longitud = []
    for i in range(longitud):
        opciones_longitud.append(opciones[i])

    while respuesta not in opciones_longitud:
        print("No has introducido un valor correcto. Las opciones son del 1 al {}.".format(opciones[longitud - 1]))
        respuesta = input()
    return respuesta


def annadir_puntuaciones(respuesta, puntuaciones):
    #  Cada pregunta, sumamos la puntuación a la respectiva casa.
    if respuesta == "1":
        puntuaciones["gryffindor"] += 1
    elif respuesta == "2":
        puntuaciones["slytherin"] += 1
    elif respuesta == "3":
        puntuaciones["hufflepuff"] += 1
    elif respuesta == "4":
        puntuaciones["ravenclaw"] += 1

    return puntuaciones


def bienvenida():
    #  Mensaje que sirve a modo de introducción.
    print("-" * 150)
    print("\n\n\nBienvenido a Hogwarts, joven mago. Antes de entrar al castillo el sombrero seleccionador"
          "te asignará una casa entre: Gryffindor, Slytherin, Hufflepuff y Ravenclaw.")

    print("¿Estás preparado?\n"
          "1- Si.\n")
    comprobar_respuesta(1)

    print("¡Adelante!\n\n")


def devolver_preguntas():
    #  Funcion que retorna las preguntas, a modo de lista de listas.
    preguntas = [
        ["Llega el final del año, está a punto de entregarse la copa de la casa. Sabes que tu casa es la ganadora."
         " ¿Cómo reaccionas?",

         "1- Espero tranquilamente a que Dumbledore haga ganar a mi casa gracias a Harry Potter.\n"
         "2- Les restriego a todos que somos los mejores, y que se jodan.\n"
         "3- ¿Ah, qué hay una copa de la casa?\n"
         "4- No te importa, tu sigues leyendo y estudiando.\n"],


        ["Ves que unos compañeros se están metiendo con un alumno de otra casa. ¿Qué haces?",

         "1- Le ayudas heroicamente.\n"
         "2- Pasas de él. Seguro que es un asqueroso sangre sucia.\n"
         "3- Nada, tu eres el alumno con el que se están metiendo.\n"
         "4- Les pides amablemente que bajen la voz, estás intentando aprender un conjuro"],


        ["Estás pasenado de noche por la escuela, y de repente encuentras la sala de los menesteres."
         "¿Para qué la utilizas?",

         "1- Ayudas a tus compañeros a aprender defensa contra las artes oscuras.\n"
         "2- Montas una mazmorra para torturar a los gryffindor.\n"
         "3- Pasas de largo, y al rato se te olvida que la has visto.\n"
         "4- Montas una sala de estudio. Por fin puedes estar tranquilo, alejado del ruidoso colegio."],


        ["Un profesor entra corriendo en el gran comedor y grita ¡Hay un troll en las mazmorras!. ¿Qué haces?",

         "1- Vas corriendo con tus amigos, e intentas neutralizar al troll.\n"
         "2- Te haces loco, y guardas la carta que mandaste a Alquiler De Trolls S.L.\n"
         "3- Intentas pasar desapercibido. No quieres que sepas que podria ser un familiar tuyo.\n"
         "4- Recordar todo lo que leiste en \"Trolls y otras criaturas pestilentes\"\n"],


        ["En clase de pociones, alguien ha hecho las cosas muy mal y su explosión va a explotar inminentemente."
         "¿Qué haces?",

         "1- Corres a avisar a todos de que se pongan a cubierto.\n"
         "2- Te escondes detrás de un compañero. Si alguien tiene que morir, que sea él.\n"
         "3- Te preguntas que le has echado a la poción para que reaccione así.\n"
         "4- Te precipitas y añades una pluma de hipogrifo, que estabiliza la poción.\n"]
    ]
    return preguntas


def hacer_pregunta(pregunta, puntuaciones):
    #  Imprimimos las preguntas, esperamos dos segundos, y a continuación imprimimos las posibles respuestas.
    print(pregunta[0])

    time.sleep(2)

    print("\n\n")
    print(pregunta[1])

    respuesta = comprobar_respuesta(4)
    return annadir_puntuaciones(respuesta, puntuaciones)


def hacer_test():
    #  Hacemos todas las preguntas, y sumamos las puntuaciones en un diccionario.
    puntuaciones = {"gryffindor": 0, "slytherin": 0, "hufflepuff": 0, "ravenclaw": 0}
    preguntas = devolver_preguntas()

    for pregunta in preguntas:
        puntuaciones = hacer_pregunta(pregunta, puntuaciones)

    return puntuaciones


def decidir_casa(puntuaciones: dict):
    """Buscamos la maxima puntuación dentro del diccionario, y, si encontramos que hay dos o más casas
    con la maxima puntuación, las mandamos al desempate."""

    maxima_puntuacion = max(puntuaciones.values())

    puntuaciones_maximas = []

    for clave, valor in puntuaciones.items():
        if valor == maxima_puntuacion:
            puntuaciones_maximas.append(clave)

    if len(puntuaciones_maximas) == 1:
        comunicar_casa(puntuaciones_maximas)
    else:
        desempate(puntuaciones_maximas)


def desempate(puntuaciones):
    #  Si hay un desempate, permitimos al usuario elegir el desempate, tal y como hace el sombrero seleccionador.

    print("El sombrero está indeciso, ayudalo a elegir que casa prefieres:\n\n")
    for numero, casa in enumerate(puntuaciones, 1):
        print("-{} {}.".format(numero, casa))

    eleccion = int(comprobar_respuesta(len(puntuaciones)))

    comunicar_casa([puntuaciones[eleccion - 1]])


def comunicar_casa(puntuaciones_maximas):
    #  Comunicamos la casa a la que pertenece el usuario.
    print("¡Enhorabuena! Perteneces a {}.".format(puntuaciones_maximas[0]))
    time.sleep(10)


def main():
    #  Funcion main, donde comienza el script.
    bienvenida()
    puntuacion = hacer_test()
    decidir_casa(puntuacion)


if __name__ == '__main__':
    main()
