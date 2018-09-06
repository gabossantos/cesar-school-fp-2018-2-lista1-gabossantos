## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem
# agradável de volta para o usuário com a resposta.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    raio = int(input('Digite o raio: '))
    area = 3.14 * (raio * raio)
    diametro = raio * 2
    comp_circunferencia = 2 * 3.14 * raio
    print ('A área do círculo é ',area,'o diâmetro é',diametro,'e o comprimento da circunferência é',round(comp_circunferencia, 2))
if __name__ == '__main__':
    main()
