# dict
# Estrutura de dados dicionário
# É uma coleção de objetos mutável, ou seja, pode ser alterada após a criação
# Não permite elementos duplicados
# Possui ordem, ou seja, podemos acessar os elementos por índice
# Utilizamos dicionários quando queremos armazenar conjuntos de dados que não devem ser alterados
# Podem ser utilizados como chaves em dicionários.
# É uma coleção de pares chave-valor, onde cada chave é única e está associada a um valor
# Podem ser criados com chaves e valores indicados ou a partir de uma estrutura iterável    

# sintaxe
# dicionario = {
#     chave1:valor1,
#     chave2:valor2,
#     chave3:valor3
# }

dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "lançamento": 1977,
    "bilheteria": 775000000.00
}
print(f"O dicionário completo é {dicionario}")
print(f"O valor da chave nome é {dicionario['nome']}")
dicionario["gênero"] = "Space opera"
print(f"O dicionário completo é {dicionario}")

print(f"O método .keys() retorna \n{dicionario.keys()}")
print("Se percorrermos a lista retornada com um loop for teremos: ")
for chave in dicionario.keys():
    print(chave)
print(f"\nO método .values() retorna \n{dicionario.values()}")
print("Se percorrermos a lista retornada com um loop for teremos: ")
for valor in dicionario.values():
    print(valor)
print(f"\nO método .items() retorna \n{dicionario.items()}")
print("Como foi retornada uma lista de tuplas e as tuplas podem ser desempacotadas, teremos: ")
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")
