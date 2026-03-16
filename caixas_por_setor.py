#Exercicio 2 - Separar caixas por setor

#No armazém:

#Pedidos pares - Setor A
#Pedidos ímpares - Setor B

#Peça 10 números de pedidos e no final mostre:

#Setor A: [ 1002, 1004, 1008 ]
#Setor B: [ 1001, 1003, 1005 ]

#Você vai usar:

#- % 2
#- duas listas
#- append()

setor_par = []
setor_impar = []

while True:
    pedidos = int(input('Qual o número do pedido? '))

    if pedidos % 2 == 0:
        setor_par.append(pedidos)
    else:
        setor_impar.append(pedidos)
    
    pergunta = input('Deseja cadastrar mais um pedido? [S/N]').upper()
    while pergunta not in 'SN': 
        pergunta = input('Digite uma resposta valida [S/N]').upper()
    if pergunta == 'N':
        break

setor_impar.sort
setor_par.sort

print(f'Pedidos do setor par são: {setor_par}')
print(f'Pedidos do setor impar são: {setor_impar}')
    
        
