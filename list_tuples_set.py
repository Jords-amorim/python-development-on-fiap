# tuple
# É uma coleção de objetos imutável, ou seja, não pode ser alterada após a criação
# Utilizamos tuplas quando queremos armazenar conjuntos de dados que não devem ser alterados
# Podem ser utilizados como chaves em dicionários.


tupla = (1, 2, 3, 4, 5)
print(tupla)  # imprime a tupla
print(type(tupla))  # imprime o tipo da tupla
print(len(tupla))  # imprime o tamanho da tupla
print(tupla[0])  # imprime o primeiro elemento da tupla
print(tupla[1:3])  # imprime os elementos da tupla do índice 1 ao 2 (não inclui o índice 3)
print(tupla[-1])  # imprime o último elemento da tupla

#desempacotar
user = ("John", 30, "New York")
name, age, city = user
print(f"Name: {name} \nAge: {age} \nCity: {city}")


categorias_jedi = ("Youngling", "Padawan", "Cavaleiro", "Mestre")
for categoria in categorias_jedi:
    print(categoria)

# tuplas e listas
inimigos = [(10,15), (20,25), (30,35), (40,45)]
for x, y in inimigos:
    print(f"Inimigo na posição {x} e {y}")  

# remove inimigos
inimigos = [(10, 15), (30, 30), (15, 25), (7, 10)]
for x, y in inimigos:
    print(f"O inimigo está na posição X={x} e Y={y}")
a = int(input("Digite a posição X do inimigo que deseja acertar "))
b = int(input("Digite a posição Y do inimigo que deseja acertar "))
if (a, b) in inimigos:
    print("ACERTOU!!")
    inimigos.remove((a, b))
else:
    print("Não foi encontrado nenhum inimigo na posição indicada ")
print(f"Os inimigos ainda existentes são: {inimigos}")   

# set

# Estrutura de dados set
# É uma coleção de objetos mutável, ou seja, pode ser alterada após a criação
# Não permite elementos duplicados
# Não possui ordem, ou seja, não podemos acessar os elementos por índice
# Utilizamos sets quando queremos armazenar conjuntos de dados que não devem ser alterados
# Podem ser utilizados como chaves em dicionários.

tupla = (1, 2, 3, 4, 5)

# três formas de criar um set

# 1. set() - cria um set vazio
conjunto = set()
# 2. Cria um set com o conteúdo de uma estrutura iterável
conjunto = set(tupla)
# 3. Cria um set com os itens indicados
conjunto = {6, 7, 8}

# print(conjunto)  # imprime o set

conjunto = set() #cria um set vazio
conjunto.add("Cebolinha")   
conjunto.add("Cascão")
conjunto.add("Mônica")
conjunto.add("Cebolinha")
print(f"O conteúdo do set que foi recebendo elementos com o método add() é \n{conjunto}") #Note que não existe repetição de elementos
lista = ["Cebolinha", "Cascão", "Mônica", "Magali", "Cebolinha"]
novo_conjunto = set(lista)
print(f"\nPodemos criar um set a partir de uma lista de um outro set ou de qualquer estrutura iterável. A lista é \n{lista}")
print(f"O conteúdo do set construído a partir da lista é \n{novo_conjunto}") #Note que não existe repetição de elementos


conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
conjunto1.difference_update(conjunto2)
print(f"O primeiro set foi atualizado com o método .difference_update() e agora contém: \n{conjunto1}")
print("\nRECONSTRUINDO OS SETS")
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
conjunto1.intersection_update(conjunto2)
print(f"O primeiro set foi atualizado com o método .intersection_update() e agora contém: \n{conjunto1}")
print("\nRECONSTRUINDO OS SETS")
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
conjunto1.symmetric_difference_update(conjunto2)
print(f"O primeiro set foi atualizado com o método .symmetric_difference_update() e agora contém: \n{conjunto1}")

# É possível ao invés de alterar os sets retornar novos sets de acordo com as comparações

conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
novo_conjunto = set.difference(conjunto1, conjunto2)
print(f"O novo set foi gerado a partir do método .difference() usando os sets 1 e 2 e contém: \n{novo_conjunto}")
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
novo_conjunto = set.symmetric_difference(conjunto1, conjunto2)
print(f"O novo set foi gerado a partir do método .symmetric_difference() usando os sets 1 e 2 e contém: \n{novo_conjunto}")
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
novo_conjunto = set.union(conjunto1, conjunto2)
print(f"O novo set foi gerado a partir do método .union() usando os sets 1 e 2 e contém: \n{novo_conjunto}")
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
novo_conjunto = set.intersection(conjunto1, conjunto2)
print(f"O novo set foi gerado a partir do método .intersection() usando os sets 1 e 2 e contém: \n{novo_conjunto}")

# Quando precisar:
# - Estrutura dinâmica que suporte repetições, utilize listas.
# - Estrutura imutável, utilize tuplas.
# - Estrutura dinâmica que não suporte repetições, utilize sets.

# Mas e quando precisamos associar os nossos dados a determinados valores?
# - Estrutura que não suporte repetições e que tenha ordem, utilize dicionários.


