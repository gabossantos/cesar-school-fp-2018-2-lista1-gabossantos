## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e
# R$ 0,15 por km rodado.

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    kms_rodados = int(input('Digite quantos quilômetros você percorreu: '))
    dias = int(input('Digite quantos dias você ficou com o carro: '))
    valor_km = kms_rodados * 0.15
    valor_dias = dias * 60
    resultado = valor_km + valor_dias
    print ('O valor a pagar é R$',resultado)
if __name__ == '__main__':
    main()
