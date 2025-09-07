from base_datos import personajes, armas, armaduras


def seleccionar_opcion(diccionario, mensaje):
    opciones = list(diccionario.keys())
    opcion_elegida = None

    while opcion_elegida is None:
        print(f"\n{mensaje}")
        for indice, valor in enumerate(opciones, start=1):
            print(f"{indice}. {valor}")

        opcion = int(input("Selecciona una opción: "))

        if 1 <= opcion <= len(opciones):
            opcion_elegida = opciones[opcion - 1]
            for clave, valor in diccionario[opcion_elegida].items():
                print(f"{clave}: {valor}")
        else:
            print("Opción no válida, intente nuevamente.")

    return opcion_elegida


def iniciar_juego():
    name = input("Ingresa el nombre para tu personaje: ")

    clase_elegida = seleccionar_opcion(personajes, "Selecciona tu clase de guerrero")
    arma_elegida = seleccionar_opcion(armas, "Selecciona tu arma")
    armadura_elegida = seleccionar_opcion(armaduras, "Selecciona tu armadura")

    print("\n" + "="*40)
    print(f"   🧝‍♂️ Personaje creado: {name}")
    print("="*40)

    print(f"\nClase: {clase_elegida}")
    for clave, valor in personajes[clase_elegida].items():
        print(f"   • {clave}: {valor}")

    print(f"\nArma: {arma_elegida}")
    for clave, valor in armas[arma_elegida].items():
        print(f"   • {clave}: {valor}")

    print(f"\nArmadura: {armadura_elegida}")
    for clave, valor in armaduras[armadura_elegida].items():
        print(f"   • {clave}: {valor}")

    print("\n" + "="*40)
    print("   ¡Tu héroe está listo para la aventura!")
    print("="*40)
