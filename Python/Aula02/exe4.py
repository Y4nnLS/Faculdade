# Crie uma lista com elementos duplicados. Crie uma nova lista sem elementos duplicados, mantendo a ordem original.
lista_com_duplicados = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

nova_lista = []
conjunto_visto = set()

for item in lista_com_duplicados:
    if item not in conjunto_visto:
        nova_lista.append(item)
        conjunto_visto.add(item)

print(nova_lista)
