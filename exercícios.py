
#Função fstring():
#Exercício 1:

vdia = 1500.00
cdia = 830.00
rdia = vdia - cdia
print(rdia)

#Exercício 2:

salario = 2350.02
aumento = 0.05
novo_salario = salario * (1 + aumento)
print(f'O salário antigo era R$ {salario:_.2f}'.replace('.',',').replace('_','.'))
print(f'O salário atual é R$ {novo_salario:_.2f}'.replace('.',',').replace('_','.'))
valor_do_aumento = novo_salario - salario
print(f'O aumento salarial foi de R$ {valor_do_aumento:_.2f}'.replace('.','.').replace('_','.'))

#Função input():
#Exercício 1:
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print(f'Seu nome é {nome} e sua idade é {idade} anos')

#Exercício 2:
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = nota1 + nota2 / 2
print(f'A média das duas notas é: {media:.1f}'.replace('.','.'))

#Operadores lógicos:
not(True) #O not, além de negação, também é conhecido como a inversão, ou seja, ele inverte o valor booleano. Podemos ler então esse código da seguinte forma: "O que não é True", "O contrário de True" e versa.
True and False #O operador and só resulta em verdadeiro se seus dois operandos lógicos forem verdadeiros. Resultará sempre em False.
True or False #O operador or só resulta em falso quando todos os operandos lógicos forem falsos. Caso contrário será sempre True.

#Exercício 1:
nota_1= 10.0
nota_2= 5.0
nota_3= 4.3
nota_4= 6.0
soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma / 4
print(f'A soma das notas dos alunos da minha turma é {soma:.1f} e a média aritmética é {media:.1f}'.replace('.',','))