#Diccionarios donde se guardarán los datos, raza, arma, armadura, estadisticas_totales
personajes = {
    "Vikingo": {"Vida": 250, "Armadura Base": 120, "Daño Base": 12, "Alcance": 4},
    "Caballero": {"Vida": 220, "Armadura Base": 150, "Daño Base": 10, "Alcance": 3},
    "Cazador": {"Vida": 160, "Armadura Base": 80, "Daño Base": 15, "Alcance": 8},
    "Druida": {"Vida": 180, "Armadura Base": 90, "Daño Base": 9, "Alcance": 7},
    "Elfo": {"Vida": 150, "Armadura Base": 70, "Daño Base": 13, "Alcance": 9}
}

armas = {
    "Espada Larga": {"Daño Extra": 6, "Alcance Extra": 1},
    "Hacha de Batalla": {"Daño Extra": 9, "Alcance Extra": 0},
    "Arco Largo": {"Daño Extra": 7, "Alcance Extra": 4},
    "Bastón Mágico": {"Daño Extra": 5, "Alcance Extra": 3},
    "Dagas Gemelas": {"Daño Extra": 4, "Alcance Extra": 1}
}

armaduras = {
    "Armadura Pesada": {"Armadura Extra": 15, "Vida Extra": 20},
    "Cota de Malla": {"Armadura Extra": 10, "Vida Extra": 10},
    "Túnica Mágica": {"Armadura Extra": 5, "Vida Extra": 5},
    "Armadura de Cuero": {"Armadura Extra": 7, "Vida Extra": 8},
    "Armadura Élfica": {"Armadura Extra": 12, "Vida Extra": 12}
}


boss = {
    "Nombre": "Señor de las Sombras",
    "Vida": 300,
    "Armadura": 80,
    "Daño": 15,
    "Acciones": ["Atacar", "Defenderse", "Esperar"]
}


