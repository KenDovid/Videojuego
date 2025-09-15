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

def crear_personaje():
    name = input("Ingresa el nombre para tu personaje: ")

    clase_elegida = seleccionar_opcion(personajes, "Selecciona tu clase de guerrero")
    arma_elegida = seleccionar_opcion(armas, "Selecciona tu arma")
    armadura_elegida = seleccionar_opcion(armaduras, "Selecciona tu armadura")

    # Crear stats totales
    stats = personajes[clase_elegida].copy()
    stats["Vida"] += armaduras[armadura_elegida]["Vida Extra"]
    stats["Armadura Base"] += armaduras[armadura_elegida]["Armadura Extra"]
    stats["Daño Base"] += armas[arma_elegida]["Daño Extra"]
    stats["Alcance"] += armas[arma_elegida]["Alcance Extra"]

    personaje = {
        "Nombre": name,
        "Clase": clase_elegida,
        "Arma": arma_elegida,
        "Armadura": armadura_elegida,
        "Vida": stats["Vida"],
        "Armadura": stats["Armadura Base"],
        "Daño": stats["Daño Base"],
        "Alcance": stats["Alcance"]
    }

    print("\n" + "="*40)
    print(f"   🧝‍♂️ Personaje creado: {name}")
    print("="*40)
    print(f"Clase: {clase_elegida}")
    print(f"Arma: {arma_elegida}")
    print(f"Armadura: {armadura_elegida}")
    print("=== Estadísticas Totales ===")
    for clave, valor in personaje.items():
        if clave not in ["Nombre", "Clase", "Arma", "Armadura"]:
            print(f"   • {clave}: {valor}")

    return personaje
