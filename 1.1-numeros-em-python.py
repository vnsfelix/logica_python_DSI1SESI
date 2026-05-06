# AULA COMPLETA: NUMEROS EM PYHTON

"""
Vamos aprender:
1 - Tipos numérios
2- Conversões de tipos
3 - Hierarquia numérica
4 - Operações matemáticas
5 - Coerção de tipos
6 - Verificação de tipos
7 - Entrada de dados
"""
#=============================
## PASSO 01 - TIPOS NUMERÍCOS
#=============================
# INT -> numeros inteiros
# float -> numeros com casas decimais
# complex -> numeros complexos (matematica/engenharia)

print("===== TIPOS NUMERICOS =====")

# EXEMPLO 1 - NUMERO INTEIRO

# criamos uma variavel chamada numero_inteiro
numero_inteiro = 10

# mostramos o valor
print("Valor:", numero_inteiro)
# Type() mostra qual é o tipo da variavel
print("Tipo:", type(numero_inteiro))

print("-----------------------------")
# EXEMPLO 2 - NUMERO COM CASA DECIMAL

# criamos uma variavel chamada numero_decimal
numero_decimal = 3.14
# mostramos o valor
print("Valor:", numero_decimal)
# mostramos o tipo
print("Tipo:", type(numero_decimal))

print("-----------------------------")

# EXEMPLO 3 - NUMERO COMPLEXO
# criamos uma variavel chamada numero_complexo
# Parte real (2) + parte imaginaria (3j)

#estrutura geral:
# numero = a + bj

# a = parte real
# b = parte imaginaria
# c = unidade imaginaria
numero_complexo = 2 + 3j

# mostramos o valor
print("Valor:", numero_complexo)
# mostramos o tipo
print("Tipo:", type(numero_complexo))

print("-----------------------------")