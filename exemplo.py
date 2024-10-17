import random

def gerar_inicio():
    inicio = ["Eu sou da Inglaterra e vim visitar o Brasil","Eu sou da Finlândia e vim visitar o Brasil", "Eu sou de Portugal e vim visitar o Brasil"]
    return random.choice(inicio)

def gerar_meio():
    meio = ["amo este lugar", " amo a comida brasileira", " amo o calor daqui"]
    return random.choice(meio)

def gerar_final():
    final = ["vou ir para a Inglaterra ano que vem", " vou ir para a Finlândia amanhã","vou para Holanda mês que vem"]
    return random.choice(final)

def gerar_frases():
    inicio = gerar_inicio()
    meio = gerar_meio()
    final = gerar_final()

    relato = f"{inicio}, {meio} e {final}"
    return relato
print(gerar_frases())