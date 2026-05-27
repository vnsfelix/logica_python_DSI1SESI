# ----------- ESCRITA DE CÓDIGOS EM PYTHON - AULA 3 -----------

"""
Vamos aprender:
- Estruturas de decisão
- Estruturas de repetição
- Funções
"""

# - Criação de strings
# - Strings multilinhas
# - Índices e fatiamento
# - Operações com strings
# - Imutabilidade
# - Métodos uteis
# - Formatação de strings
# - Unicode e bytes

# =============================
# PASSO 01 - Criação de strings
# =============================

# Strings são textos em python.
# Podemos criar strings usando aspas simples ou duplas.

string1 = "Olá, mundo!"
string2 = 'Curso de Python'
string3 = "Copa 'padrão fifa'"
string4 = 'Copa "padrão fifa"'
print(string1, string2, string3, string4)

# Pyhton permite misturar aspas simples e duplas. dentro das strings sem precisar escapar caracteres

# ============================
# 2) STRINGS MULTILINHA
# ============================
# Usando 3 aspas (""" ou ''') para criar textos que ocupam varias linhas

menu = """\
Uso: programa [OPÇÕES]
-h exibe ajuda
-U Url do dataset
"""
print(menu)

# Esse formato é muito usado para:
# - Menus
# - documentos
# - textos longos

# =====================================
# 3) CONCATENAÇÃO AUTOMÁTICA
# =====================================
# Quando duas strings aparecem lado a lado, o Pyhton junta automaticamente

texto = ("Copa" " 2026 " "Neymar é show mesmo?")
print(texto)

# =====================================
# 4) STRINGS COMO SEQUENCIAS  
# =====================================
# Uma string funciona como uma sequência de caracteres, cada caractere possui um índice

st = "Maracana"
print("Primeira letra:", st[0])
# só exibir a letra: M

print("Ultima letra:", st[-1])

print("Trecho 1:4:", st[1:4])

print("Do inicio até 3", st[:3])

print("Do 2 até o fim:", st[2:])

print ("Tamanho", len(st))

# ==============================
# 5) OPERAÇÕES COM STRINGS
# ==============================
# Python permite várias operações com strings

print("M" in st)
# significa que a letra "m" existe dentro da string

print("x" not in st)

print("m" * 20)

print("m" + "aracana")

# ==========================
# 6) STRINGS SÃO IMUTAVEIS
# ========================== 
# Strings não podem ser alteradas diretamente !!!
# Isso significa que o conteudo não muda
# O quie acontece é a criação de uma nova string

string5 = "python 3"

string5 = string5.replace("3","2")

print(string5)

# ==============================
# 7) METODOS IMPORTANTES
# ==============================
# Strings possuem vários metodos uteis

cidade = "maracana"
print(cidade.capitalize())

# contar quantas vezes a letra "a" aparece
print(cidade.count("a"))

# Verificar se comeca com "M"
print(cidade.startswith("m"))

# Verifica se termina com "z"
print(cidade.endswith("z"))

frase = "copa de 2002"

print(frase.split(" "))

# ============================
# 8) FORMATAÇÃO DE STRINGS 
# ============================