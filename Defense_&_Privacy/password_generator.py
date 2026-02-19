import random
import string

def gerar_senha(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

print("---------Gerador de Senhas Fortes----------")
comprimento = int(input("Digite o comprimento desejado para a senha: "))
senha_gerada = gerar_senha(comprimento)
print(f"Sua senha gerada é: {senha_gerada}")
