entrada = (input("Digite o valor inteiro para saber a soma + 10: "))
try:
    E = int(entrada)
    print(f"Boa, o valor digitado foi: {E}, a soma é igual a:\n{E+10}.")
except ValueError:
    (print("Opa, você nao digitou um numero inteiro,\ntente novamente."))