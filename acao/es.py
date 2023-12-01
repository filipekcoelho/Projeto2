from proc import Acao

def leitora_emissor():
    """Lê emissor informado pelo usuário"""
    emissor = input("Qual o nome da empresa? ")
    return emissor

def leitora_codigo():
    """Lê código informado"""
    codigo = input("Qual o código na B3? ")
    return codigo

def leitora():
    emissor = leitora_emissor()
    codigo = leitora_codigo()
    return [emissor, codigo]

def impressora(acao: Acao):
    """Imprime o resultado"""
    print(acao)