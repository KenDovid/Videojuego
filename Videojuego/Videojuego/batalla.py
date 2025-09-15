import random

def batalla(jugador, boss):
    print("\n⚔️ ¡Comienza la batalla contra el Boss!")
    print(f"Te enfrentas a: {boss['Nombre']}\n")

    vida_jugador = jugador["Vida"]
    vida_boss = boss["Vida"]

    defendiendo_jugador = False
    defendiendo_boss = False

    while vida_jugador > 0 and vida_boss > 0:
        print("\n--- ESTADO ---")
        print(f"{jugador['Nombre']} (Vida: {vida_jugador}) vs {boss['Nombre']} (Vida: {vida_boss})")

        # Turno jugador
        print("\nAcciones disponibles:")
        print("1. Atacar")
        print("2. Defenderse")
        print("3. Esperar")

        accion_jugador = int(input("Elige tu acción: "))

        if accion_jugador == 1:
            dano = jugador["Daño"]
            if defendiendo_boss:
                dano //= 2
            vida_boss -= dano
            print(f"\n💥 {jugador['Nombre']} ataca y hace {dano} de daño!")
            defendiendo_jugador = False

        elif accion_jugador == 2:
            defendiendo_jugador = True
            print(f"\n🛡️ {jugador['Nombre']} se defiende, reducirá el daño recibido!")

        else:
            print(f"\n⏳ {jugador['Nombre']} espera su momento...")
            defendiendo_jugador = False

        # Turno boss
        accion_boss = random.choice(boss["Acciones"])
        print(f"\n👉 El Boss decide: {accion_boss}")

        if accion_boss == "Atacar":
            dano = boss["Daño"]
            if defendiendo_jugador:
                dano //= 2
            vida_jugador -= dano
            print(f"🔥 {boss['Nombre']} ataca e inflige {dano} de daño!")
            defendiendo_boss = False

        elif accion_boss == "Defenderse":
            defendiendo_boss = True
            print(f"🛡️ {boss['Nombre']} se defiende!")

        else:
            print(f"😈 {boss['Nombre']} espera...")
            defendiendo_boss = False

    # Resultado final
    print("\n=== RESULTADO DE LA BATALLA ===")
    if vida_jugador <= 0 and vida_boss <= 0:
        print("😵 Ambos han caído... ¡Empate épico!")
    elif vida_boss <= 0:
        print(f"🏆 ¡{jugador['Nombre']} ha derrotado al {boss['Nombre']}!")
    else:
        print(f"💀 {jugador['Nombre']} ha sido derrotado por el {boss['Nombre']}...")
