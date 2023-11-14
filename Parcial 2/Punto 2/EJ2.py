from grafo import Grafo

grafo = Grafo()

personajes = [ "Luke Skywalker", "Darth Vader", "Kylo Ren", "Leia","Boba Fett", "C-3PO", "Rey", "Chewbacca","Han Solo", "R2-D2", "BB-8", "Yoda"]

for personaje in personajes:
    grafo.insert_vertice(personaje)

grafo.insert_arist("Luke Skywalker", "Darth Vader", 5)
grafo.insert_arist("Luke Skywalker", "Kylo Ren", 2)
grafo.insert_arist("Luke Skywalker", "Leia", 3)

grafo.insert_arist("Darth Vader", "Kylo Ren", 4)
grafo.insert_arist("Darth Vader", "Leia", 2)

grafo.insert_arist("Kylo Ren", "Leia", 1)

grafo.insert_arist("Leia", "Boba Fett", 3)
grafo.insert_arist("Leia", "C-3PO", 4)
grafo.insert_arist("Leia", "Rey", 5)

grafo.insert_arist("Boba Fett", "C-3PO", 2)
grafo.insert_arist("Boba Fett", "Rey", 1)

grafo.insert_arist("C-3PO", "Rey", 3)
grafo.insert_arist("Chewbacca", "Han Solo", 4)
grafo.insert_arist("R2-D2", "BB-8", 2)
grafo.insert_arist("Yoda", "Chewbacca", 1)

arbol_expansion_minimo = grafo.kruskal()

print("Árbol de Expansión Mínimo:")
for arista in arbol_expansion_minimo:
    print(arista)

contiene_yoda = False
for arista in arbol_expansion_minimo:
    if "Yoda" in arista:
        contiene_yoda = True
        break

if contiene_yoda:
    print("El árbol de expansión mínimo contiene a Yoda.")
else:
    print("El árbol de expansión mínimo no contiene a Yoda.")

max_peso, personajes_max_episodios = grafo.max_episodios_compartidos()

if max_peso > 0:
    print(f"El número máximo de episodios compartidos es {max_peso}, y los personajes son:")
    for i in range(0, len(personajes_max_episodios), 2):
        personaje1 = personajes_max_episodios[i]
        personaje2 = personajes_max_episodios[i + 1]
        print(f"{personaje1} y {personaje2}")
else:
    print("No se encontraron personajes que compartan episodios.")

#EJ extra del recuperatorio
com = "Yoda"
fin= "Rey"
comienzo = grafo.search_vertice(com)
final = grafo.search_vertice(fin)
camino_mas_corto = None
if(comienzo is not None and final is not None):
    if(grafo.has_path(com, fin)):
        camino_mas_corto = grafo.dijkstra(com, fin)
        fin = fin
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value [2]