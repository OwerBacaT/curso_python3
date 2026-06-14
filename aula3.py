# Conversión de Tipos
# type convertion, typecasting, coercion
# es el acto de convertir un tipo en otro
# Tipos inmutables y primitivos
# str, int, float, bool

print(type(int('100')) , type('100'))

# entrada de dado
number_1 = input('Digite o valor: ')
print(type(number_1))

number_1 = int(number_1) #Coercion de valor str para int

if number_1 > 5:
    print("Gain")
else:
    print("loss")

#convertendo para str
num = 58
num = str(num)
print(type(num))