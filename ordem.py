'''
Coloque esses números dentro de um arquivo nessa ordem:
6
10
9
7
1
4
3
8
2
5

Faça um programa que lê o arquivo, ordena os números e mostra eles na tela em ordem crescente. É importante que os números sejam lidos a partir de um arquivo. Não vale colocá-los no código.
'''

with open('numeros.txt', 'w') as arquivo:
    numeros = [6, 10, 9, 7, 1, 4, 3, 8, 2, 5]
    for numero in numeros:
        arquivo.write(str(numero) + '\n')

with open('numeros.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    numeros = [int(linha.strip()) for linha in linhas]
    numeros.sort()

arquivo.close()

print("Números em ordem crescente:")
for numero in numeros:
    print(numero)