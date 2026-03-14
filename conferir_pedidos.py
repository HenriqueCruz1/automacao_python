#Exercicio 1.

#Conferir pedidos duplicados.

#Imagine que ao registrar caixas, as vezes o mesmo pedido é escaneado duas vezes.

#Peça para o usuário digitar 5 números de pedidos e informe se algum foi digitado mais de uma vez.

#Exemplo de saida:

#Pedido 1020 já foi registrado!

#Dica de lógica:

#- Usar uma lista
#- Verificar if pedido in lista

print('-'*30 , 'CONFERENCIA DE PEDIDOS DUPLICADOS' , '-' * 30)

pedidos = []

while True:

    pedido = input('Digite o número do pedido. ')
    
    if pedido not in pedidos:
        pedidos.append (pedido)
    else:
        print('Pedido já registrado anteriormente ...')

    pergunta = input('Deseja continuar ? [S/N]').upper()

    while pergunta not in 'SN': #filtro de resposta se corresponde ao solicitado.
        pergunta = input('Resposta invalida. Digite S ou N ').upper()

    if pergunta == 'N': #condição para aplicar o break do loop.
        break
    
pedidos.sort()
print (pedidos)