# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: aneska.silva@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    divisores = 0
    candidato = 1
    while candidato <= n:
        if n % candidato == 0:
            divisores += 1
        candidato += 1
    if divisores == 2:
        return True
    else:
        return False


def lista_primos(n):
    primos_encontrados = []
    for item in range(2, n):
        if eh_primo(item):
            primos_encontrados.append(item)
    return primos_encontrados


def conta_primos(s):
    contagem_primos = {}
    for item in s:
        if eh_primo(item):
            if item in contagem_primos:
                contagem_primos[item] += 1
            else:
                contagem_primos[item] = 1
    return contagem_primos


def eh_armstrong(n):
    potencia = len(str(n))
    soma = 0
    num = n
    while num > 0:
        digito = num % 10
        soma += digito ** potencia
        num //= 10
    if n == soma:
        return True
    return False


def eh_quase_armstrong(n):
    while n >= 0:
        if eh_armstrong(n):
            return False
        return True


def lista_armstrong(n):
    armstrong_encontrados = []
    for item in range(n):
        if eh_armstrong(item):
            armstrong_encontrados.append(item)
    return armstrong_encontrados


def eh_perfeito(n):
    divisores = []
    soma = 0
    for numero in range(1, n):
        if n % numero == 0:
            divisores.append(numero)
            soma += numero
    if soma == n:
        return True
    return False


def lista_perfeitos(n):
    perfeitos_encontrados = []
    for item in range(1, n):
        if eh_perfeito(item):
            perfeitos_encontrados.append(item)
    return perfeitos_encontrados

