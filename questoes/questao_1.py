## QUESTÃO 1 ##
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do
# novo salário.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    salario_antigo = float(input('Digite o valor do salário: '))
    percentual_aumento = float(input('Digite o percentual de aumento salarial: '))
    aumento = (salario_antigo * (percentual_aumento / 100))
    resultado = salario_antigo + aumento
    print ('O reajuste salarial foi de R$',aumento,'e o valor do novo salário é R$',resultado)
if __name__ == '__main__':
    main()
