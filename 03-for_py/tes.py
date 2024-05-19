candidatos = ['walex', 'Rubia', 'Diocel']
votos = [16, 90, 90]

# Dicionário para armazenar candidatos e seus respectivos votos
votos_dict = {}

# Armazenando os votos no dicionário
for i, voto in enumerate(votos):
    print(f'O candidato {candidatos[i]} teve -> {voto}')
    votos_dict[candidatos[i]] = voto

# Encontrando o maior número de votos
maior = max(votos)

# Encontrando todos os candidatos com o maior número de votos
vencedores = [candidato for candidato, voto in votos_dict.items() if voto == maior]

# Verificando se há empate
if len(vencedores) > 1:
    print(f"Empate! Os candidatos vencedores são: {', '.join(vencedores)} com {maior} votos cada.")
else:
    print(f"O candidato vencedor é: {vencedores[0]} com {maior} votos.")
