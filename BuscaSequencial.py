#Este programa tem por finalidade demonstrar a lógica e o funcionamento de um algoritmo de busca sequencial que pode ser escrito em qualquer linguagem,
# assim sendo não utiliza funções e/ou bibliotecas exclusivas da linguagem Python.

#O programa funciona com base no fornecimento de 3 informações, um limite mínimo, um limite máximo e um valor X que será utilizado como critério,
# após o fornecimento das informações, o programa irá criar uma lista para os valores válidos e se manterá em looping solicitando um novo valor para teste até que o valor 0 seja digitado,
# esse novo valor será verificado e se caso estiver dentro do intervo mínimo e máximo, for divisível por X e não estiver na lista, ele será inserido.
# Ao final o programa exibe a lista de valores válidos, bem como a soma e a média dos itens constantes na lista.


Lmin = int(input("Digite um valor para o Limite Mínimo: "))
while Lmin < 0:
    print("O Limite Mínimo não pode ser negativo")
    Lmin = int(input("Digite um valor para o Limite Mínimo: "))
Lmax = int(input("Digite um valor para o Limite Máximo: "))
if Lmax < Lmin:
    print("Caro usuário, os valores de Lmin e Lmax foram digitados invertidos, irei corrigir para você")
    A = Lmin
    Lmin = Lmax
    Lmax = A
X = int(input("Digite X: "))
while X == 0:
    X = int(input("Digite X: "))
lista_valores = []
soma = 0
valor = 1
#implementação do algoritmo de busca sequencial
while valor != 0:
    Achou = False
    i = 0
    valor = int(input("Digite um valor: "))
    if valor >= Lmin and valor <= Lmax and valor % X == 0:
        while i < len(lista_valores) and Achou == False:
            if valor == lista_valores[i]:
                Achou = True
            else:
                i += 1
        if Achou == False and valor != 0:
            lista_valores.append(valor)
            soma += valor
print(lista_valores)
print("A lista possui {} valores".format(len(lista_valores)))
print("A soma dos valores da lista é {}".format(soma))
print("A média dos valores da lista é {}".format(soma/len(lista_valores)))