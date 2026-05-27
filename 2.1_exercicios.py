# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX1
# Crie uma variável chamada texto1 com o valor "Logica"
# usando aspas duplas e exiba o conteúdo.

str = "Lógica"
print(str)

# EX2
# Crie uma variável chamada texto2 com o valor
# 'Eu sou top em python' usando aspas simples e exiba.

str2 = "'Eu sou top em python'"
print(str2)

# EX3
# Crie uma string usando aspas simples que contenha
# aspas duplas dentro do texto: copa "padrão fifa".

str3 = 'copa "padrão fifa".'
print(str3)

# EX4
# Crie uma string usando aspas duplas que contenha
# aspas simples dentro do texto: copa 'padrão fifa'.

str4 = "copa 'padrão fifa'."
print(str4)

# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX5
# Crie uma string multilinha representando um menu
# com as opções:
# -A  Exibe ajuda
# -E  Execute agora, quero jogar!

menu = """\
Uso: programa [OPÇÕES]
-A Ajuda
-E Executar agora, quero jogar!
"""
print(menu)


# EX6
# Crie uma string multilinha contendo um poema
# com três versos.

poema = """Saudade é solidão acompanhada,
é quando o amor ainda não foi embora,
mas o amado já.
"""
print(poema)


# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX7
# Use concatenação automática de literais para unir
# as palavras "Volei" e "top!".

str7 = ("Volei" " Top")
print(str7)

# EX8
# Concatene automaticamente as strings
# "Python", " é ", "demais" em uma única string.

str8 = ("Python" "é" "demais")
print(str8)


# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX9
# Atribua "software" a uma variável chamada st
# e mostre a primeira letra da string.

st = "software"
print("Primeira letra:", st[0])

# EX10
# Usando a mesma string "software",
# mostre a última letra.

print("Ultima letra:", st[-1])

# EX11
# Mostre os caracteres do índice 1 até o índice 4
# (sem incluir o 4) da string "software ".

print("índice 1 até o índice 4:", st[1:4])

# EX12
# Mostre os caracteres do início até o índice 3
# da string "software".

print("inicio até o índice 3:", st[0:3])

# EX13
# Mostre os caracteres do índice 2 até o final
# da string "software".

print("índice 2 até o final:", st[2:])

# EX14
# Mostre o tamanho da string "software"
# usando a função len().

print ("Tamanho", len(st))

# EX15
# Acesse o último caractere de "software"
# usando índice positivo (sem usar -1).

# EX16
# Mostre os caracteres que estão nos índices pares
# da string "software".

# EX17
# Inverta a string "software".