# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  essencial = 10
  prata = 20
  premium = 20
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
  if consumo <= essencial:
    return "Plano Essencial Fibra - 50Mbps"
  elif essencial < consumo <= prata:
    return "Plano Prata Fibra - 100Mbps"
  elif consumo > prata:
    return "Plano Premium Fibra - 300Mbps"
  else:
    return "Informe um número novamente."

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
