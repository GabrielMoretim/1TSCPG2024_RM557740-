'''Complete os exercícios com os código como for solicitado'''

'''______________________________________________________________________________________________________________________'''

#Exercício 1 (2 PONTOS)

'''
Dado um número pelo usuário, verificar se ele é "par" ou "impar",
exibindo as seguintes mensagens: 
    1. "O número é par!"
    2. "O número é ímpar!" 

Resolver usando 'IF' quantas vezes forem necessárias!

'''

input_numero = eval(input('Digite o número a ser avaliado: '))

if (input_numero % 2 == 0):
    print("O número informado é par!")
else:
    print("O número informado é impar!")



'''______________________________________________________________________________________________________________________'''

#Exercício 2 (2 PONTOS)

'''
Solicitar a digitação de duas notas entre 0 e 10: 
    1. Caso uma (ou as duas) nota seja inválida (fora do intervalo) exibir: 
        “Nota do CPX inválida!” e terminar o algoritmo;

    2. Senão, calcular e exibir a média e e uma mensagem que pode ser:
        2.1 - "Você foi aprovado!"  (caso média >= 6) ou
        2.2 - "Você não foi aprovado! (caso contrário)"

* Vejam que temos dois testes de nota, e portanto, seria ideal que a resposta seja  por teste, onde PX pode ser entre 1 e 2!

Resolver usando 'IF' quantas vezes forem necessárias!
'''

input_nota1 = eval(input('Digite a nota do CP1: '))
input_nota2 = eval(input('Digite a nota da CP2: '))
media = (input_nota1 + input_nota2) / 2;

if (input_nota1 >= 0 and input_nota1 <= 10 and input_nota2 >= 0 and input_nota2 <= 10):
    if (media >= 6):
        print("Você foi aprovado!");
    else:
        print("Você foi reprovado!");
else:
    print("Nota do CPX inválida!");




'''______________________________________________________________________________________________________________________'''

#Exercício 3 (2 PONTOS)

'''
Dado um número, exibir os seus 10 primeiros múltiplos:

Exemplo: 2 
    Saída: 2 4 6 8 10 12 14 16 18 20

Resolver usando o laço WHILE:

* Dica: Incremente o contador

'''
numero_para_calcular = eval(input('Digite um número para multiplicar: '))
contador = numero_para_calcular
seletor = numero_para_calcular * 10;

while (contador <= seletor):
    print(contador)
    contador += numero_para_calcular;






'''______________________________________________________________________________________________________________________'''

#Exercício 4 (2 PONTOS)

'''
Em uma votação, existem 3 candidatos: 
    1. Huguinho;
    2. Zezinho;
    3. Luizinho. 
    
Pedir e acumular votos até que no campo "votos" seja digitado o numero 0
(zero). 

Ao final, exibir a quantidade de votos de cada usuário.

Resolver usando o laço WHILE e IF aninhados:

* Dicas: inicie as notas e uma variável de controle do laço (True or False)
chamar o voto com: 

    input_voto = eval(input('Digite 1 para votar no Huguinho, 2 no Zezinho e 3 no Luizinho! Digite 0 (Zero) para Terminar: '))

    colocar um ELSE: no fim dos testes de voto para rejeitar valores fora dos especificados

        else:
            print("Voto descartado!")
    
    use break ou altere a variável de controle para False para parar

'''

votos_Huginho = 0
votos_Zezinho = 0
votos_Luizinho = 0

controle = True

while (controle):
    input_voto = eval(input('Digite 1 para votar no Huguinho, 2 no Zezinho e 3 no Luizinho! Digite 0 (Zero) para Terminar: '))

    if (input_voto == 1):
        votos_Huginho += 1;
    elif (input_voto == 2):
        votos_Zezinho += 1;
    elif (input_voto == 3):
        votos_Luizinho += 1;
    elif (input_voto == 0):
        break
    else:
        print("Voto Descartado!")


#Seu código termina aqui <---
print(f"O Huguinho teve {votos_Huginho} votos!")
print(f"O Zezinho teve {votos_Zezinho} votos!")
print(f"O Luizinho teve {votos_Luizinho} votos!")



'''______________________________________________________________________________________________________________________'''

#Exercício 5 (2 PONTOS)

'''
faça a entrada do nome de uma pessoa e reduza tudo para caixa baixa com .lower()
Usando o laço FOR faça a varredura do nome de entrada e imprima letra a letra do nome:

Exemplo: FULANO

    F
    U
    L
    A
    N
    O

'''

nome = input('Entre com seu nome: ').lower();

for nome in nome:
    print(nome)

# aqq fnrjefbghogtaejh-\shjt
