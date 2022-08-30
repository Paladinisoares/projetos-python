cpf = input('Digite seu cpf: ')

if len(cpf) != 11:
    print('Você não digitou os 11 digitos do cpf')
else:
    pass

cpf_separado = ''
novo_cpf = ''
soma = 0
soma_2 = 0
primeiro_digito = 0
segundo_digito = 0

for d in range(0, 9):
    cpf_separado += cpf[d]

for p, r in enumerate(range(10, 1, -1)):
    multiplicacao = int(cpf_separado[p]) * r
    soma += multiplicacao

primeira_equacao = 11 - (soma % 11)

if primeira_equacao < 9:
    primeiro_digito = primeira_equacao
    primeiro_digito = str(primeiro_digito)
else:
    primeiro_digito = str(primeiro_digito)

novo_cpf = cpf_separado + primeiro_digito

for p, r in enumerate(range(11, 1, -1)):
    multiplicacao = int(novo_cpf[p]) * r
    soma_2 += multiplicacao

segunda_equacao = 11 - (soma_2 % 11)

if segunda_equacao < 9:
    segundo_digito = segunda_equacao
    segundo_digito = str(segundo_digito)
else:
    segundo_digito = str(segundo_digito)

novo_cpf += segundo_digito

print(f'O cpf {cpf} está válido') if novo_cpf == cpf else print(f'O cpf {cpf} não está válido')
