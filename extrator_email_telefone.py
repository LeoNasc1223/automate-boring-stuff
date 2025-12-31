import pyperclip, re

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # nome do usuário
    @                      # símbolo arroba
    [a-zA-Z0-9.-]+         # nome do domínio
    (\.[a-zA-Z]{2,4})      # .com, .org, .edu, .com.br
    )''', re.VERBOSE)

joker_phone_regex = re.compile(r'''(
    \+                  # Começa obrigatoriamente com o sinal de +
    \d{1,3}             # Código do país (1 a 3 dígitos)
    [\s.-]?             # Separador opcional (espaço, ponto ou traço)
    \d{1,4}             # Código de área ou cidade (1 a 4 dígitos)
    [\s.-]?             # Outro separador opcional
    [\d\s.-]{5,12}      # O restante do número (5 a 12 caracteres entre dígitos e símbolos)
)''', re.VERBOSE)

mensagem = pyperclip.paste()

lista_de_dados = {"Email": [], "Telefone": []}

texto_para_copiar = []

moE = email_regex.findall(mensagem)

moP = joker_phone_regex.findall(mensagem)

for email in moE:
    lista_de_dados["Email"].append(email[0])

for numero in moP:
    lista_de_dados["Telefone"].append(numero)

for email in lista_de_dados["Email"]:
    texto_para_copiar.append(f"Email:{email}")

for numero in lista_de_dados["Telefone"]:
    texto_para_copiar.append(f"Telefone:{numero}")

texto_formatado = "\n".join(texto_para_copiar)

pyperclip.copy(texto_formatado)

print("Dados copiados para a area de tranferencia!")