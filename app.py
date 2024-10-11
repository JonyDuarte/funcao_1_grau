
def calcular_x(a, b):
     x = -b / a
     return x

# valores de a e b do usuário

a = float(input("Digite o valor de a : "))
b = float(input("Digite o valor de b : "))
        
# Calcula o valor de x1
x = calcular_x(a, b)

# Resultado
print(f"O valor de 'x' é: {x}")