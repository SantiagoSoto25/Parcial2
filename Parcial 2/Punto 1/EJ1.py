from arbolbinario import BinaryTree

pokemon_data = [
    {"name": "Tyrantrum", "number": 697, "types": ["Roca", "Dragón"]},
    {"name": "Lotad", "number": 270, "types": ["Agua", "Planta"]},
    {"name": "Flareon", "number": 136, "types": ["Fuego"]},
    {"name": "Bulbasaur", "number": 1, "types": ["Pasto", "Veneno"]},
    {"name": "Zekrom", "number": 644, "types": ["Dragón", "Eléctrico"]},
    {"name": "Jolteon", "number": 135, "types": ["Eléctrico"]},
    {"name": "Lycanroc", "number": 745, "types": ["Roca"]},
    {"name": "Tyrantrum", "number": 697, "types": ["Roca", "Dragón"]},
    {"name": "Raichu", "number": 26, "types": ["Eléctrico"]},
    {"name": "Duraludon", "number": 884, "types": ["Acero", "Dragón"]},
]

pokemon_tree = BinaryTree()

for pokemon in pokemon_data:
    name = pokemon["name"]
    number = pokemon["number"]
    types = pokemon["types"]
    pokemon_tree.insert_node(name, (number, types))

cadena = input("Ingrese una cadena para buscar Pokémon por proximidad en el nombre: ")
print("Resultados de búsqueda:")
pokemon_tree.inorden_start_with(cadena)

tipos_a_buscar = ["Agua","Fuego", "Planta","Electrico"]
print("Nombres de Pokémon de tipo Agua:")
pokemon_tree.listar_nombres_por_tipo(pokemon_tree.root, tipos_a_buscar)

print("Listado en orden ascendente por número de Pokémon:")
pokemon_tree.inorden()

print("\nListado por nivel por nombre de Pokémon:")
pokemon_tree.by_level()

pokemon_name_to_search = input("Ingrese la parte del nombre del Pokémon que desea buscar: ")
print("Resultados de búsqueda por coincidencia en el nombre:")
pokemon_tree.search_by_coincidence(pokemon_name_to_search)

tipo_electrico = "Eléctrico"
tipo_acero = "Acero"

print(f"Cantidad de Pokémon de tipo Eléctrico: {pokemon_tree.contar(tipo_electrico)}")
print(f"Cantidad de Pokémon de tipo acero: {pokemon_tree.contar(tipo_acero)}")