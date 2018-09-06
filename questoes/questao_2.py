## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius)
# para °F (graus fahrenheit).
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    temperatura_c = float(input('Digite a temperatura em celsius (°C) que você deseja converter para fahrenheit (°F): '))
    resultado = (temperatura_c*1.8)+32
    print (temperatura_c, '°C é igual a',resultado,'°F')
if __name__ == '__main__':
    main()
