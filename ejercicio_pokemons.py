class Pokemon:
    def __init__(self, nombre, numero, tipo):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo

# Lista de Pokemones Desordenados
pokemons = [
    Pokemon("Tyrantrum", 697, ["Roca", "Dragón"]),
    Pokemon("Lotad", 270, ["Agua", "Planta"]),
    Pokemon("Flareon", 136, ["Fuego", ]),
    Pokemon("Lycanroc", 745, ["Roca", ]),
    Pokemon("Raichu", 26, ["Eléctrico", ]),
    Pokemon("Zekrom", 644, ["Dragón", "Eléctrico"]),
    Pokemon("Jolteon", 135, ["Eléctrico", ]),
    Pokemon("Duraludon", 884, ["Acero", "Dragón"]),
]

pokemon_por_nombre = {}
pokemon_por_numero = {}
pokemon_por_tipo = {}

for pokemon in pokemons:
    pokemon_por_nombre[pokemon.nombre] = pokemon

    pokemon_por_numero[pokemon.numero] = pokemon

    for tipo in pokemon.tipo:
        if tipo not in pokemon_por_tipo:
            pokemon_por_tipo[tipo] = []
        pokemon_por_tipo[tipo].append(pokemon)

# Función para buscar Pokémon por número
def buscar_pokemon_por_numero(numero):
    return pokemon_por_numero.get(numero)

# Función para buscar Pokémon por nombre (búsqueda por proximidad)
def buscar_pokemon_por_nombre(nombre):
    resultados = []
    for pokemon in pokemons:
        if nombre.lower() in pokemon.nombre.lower():
            resultados.append(pokemon)
    return resultados

# Función para buscar Pokémon por tipo
def buscar_pokemon_por_tipo(tipo):
    if tipo in pokemon_por_tipo:
        return pokemon_por_tipo[tipo]
    else:
        return []

# Función para mostrar los nombres de Pokémon de un tipo específico
def mostrar_nombres_por_tipo(tipo):
    pokemons_de_tipo = buscar_pokemon_por_tipo(tipo)
    if not pokemons_de_tipo:
        print(f"No se encontraron Pokémon de tipo {tipo}.")
    else:
        print(f"Nombres de Pokémon de tipo {tipo}:")
        for pokemon in pokemons_de_tipo:
            print(pokemon.nombre)

# Función para mostrar todos los Pokémon en orden ascendente por número
def listar_pokemon_por_numero():
    pokemons_ordenados = sorted(pokemons, key=lambda pokemon: pokemon.numero)
    for pokemon in pokemons_ordenados:
        print(f"Número: {pokemon.numero}, Nombre: {pokemon.nombre}, Tipo: {pokemon.tipo}")

# Función para mostrar todos los Pokémon en orden ascendente por nombre
def listar_pokemon_por_nombre():
    pokemons_ordenados = sorted(pokemons, key=lambda pokemon: pokemon.nombre)
    for pokemon in pokemons_ordenados:
        print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipo: {pokemon.tipo}")

# Función para mostrar todos los Pokémon en orden ascendente por nivel de tipo
def listar_pokemon_por_tipo():
    tipos = sorted(list(pokemon_por_tipo.keys()))
    for tipo in tipos:
        print(f"Tipo: {tipo}")
        pokemons_de_tipo = sorted(pokemon_por_tipo[tipo], key=lambda pokemon: pokemon.nombre)
        for pokemon in pokemons_de_tipo:
            print(f"  Nombre: {pokemon.nombre}, Número: {pokemon.numero}")

# Función para mostrar todos los datos de Pokémon por nombre
def mostrar_datos_pokemon_por_nombre(nombre_pokemon):
    pokemon = pokemon_por_nombre.get(nombre_pokemon)
    if pokemon:
        print("Datos del Pokémon:")
        print(f"Nombre: {pokemon.nombre}")
        print(f"Número: {pokemon.numero}")
        print(f"Tipo: {', '.join(pokemon.tipo)}")
    else:
        print(f"No se encontró un Pokémon con el nombre {nombre_pokemon}.")

# Pokémon a buscar
pokemon_a_buscar = ["Jolteon", "Lycanroc", "Tyrantrum"]

for nombre_pokemon in pokemon_a_buscar:
    mostrar_datos_pokemon_por_nombre(nombre_pokemon)

# Función para contar la cantidad de Pokémon de un tipo específico
def contar_pokemon_por_tipo(tipo):
    if tipo in pokemon_por_tipo:
        return len(pokemon_por_tipo[tipo])
    else:
        return 0

# Contar la cantidad de Pokémon de tipo eléctrico y acero
tipo_electrico = "Eléctrico"
tipo_acero = "Acero"

cantidad_electrico = contar_pokemon_por_tipo(tipo_electrico)
cantidad_acero = contar_pokemon_por_tipo(tipo_acero)

print(f"Cantidad de Pokémon de tipo {tipo_electrico}: {cantidad_electrico}")
print(f"Cantidad de Pokémon de tipo {tipo_acero}: {cantidad_acero}")


# Ejemplos de búsqueda por número y nombre
numero_busqueda = 26
nombre_busqueda = "ly"

pokemon_por_numero = buscar_pokemon_por_numero(numero_busqueda)
pokemon_por_nombre = buscar_pokemon_por_nombre(nombre_busqueda)

if pokemon_por_numero:
        print(f"Pokémon encontrado por número: {pokemon_por_numero.nombre}")

if pokemon_por_nombre:
    print("Pokémon encontrado(s) por nombre:")
    for pokemon in pokemon_por_nombre:
        print(f"Nombre: {pokemon.nombre}, Número: {pokemon.numero}, Tipo: {pokemon.tipo}")
else:
    print("No se encontraron Pokémon con ese nombre.")

# Ejemplos de búsqueda por tipo
tipo_busqueda = "Agua"
mostrar_nombres_por_tipo(tipo_busqueda)

tipo_busqueda = "Fuego"
mostrar_nombres_por_tipo(tipo_busqueda)

tipo_busqueda = "Planta"
mostrar_nombres_por_tipo(tipo_busqueda)

tipo_busqueda = "Eléctrico"
mostrar_nombres_por_tipo(tipo_busqueda)

# Ejemplos de listados
print("Listado de Pokémon en orden ascendente por número:")
listar_pokemon_por_numero()

print("\nListado de Pokémon en orden ascendente por nombre:")
listar_pokemon_por_nombre()

print("\nListado de Pokémon en orden ascendente por tipo y nombre:")
listar_pokemon_por_tipo()
