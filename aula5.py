
# variaveis e tipos de dados para exercicios 

# input de variaveis

'''

def solicitaca_infos():
    nome = (input("Informe seu nome: "))
    sobrenome = (input("Informe seu Sobrenome: "))
    idade = int(input("Informe sua idade: "))
    ano_nascimento = int(input("Informe sua data de nascimento: "))
    altura_metros = float(input("Informe sua altura: "))
'''
from datetime import datetime

def coleta_dados[T: (int | float | str)](coleta: str , tipo: type[T]) -> T :
    while True:
        try:
            entrada_dados = tipo(input(coleta))
            return entrada_dados
        except ValueError:
            print('Dado Invalido!')

def valida_dados(ano: int, mes: int, dia: int) -> None:
    if mes < 1 or mes > 12:
        raise ValueError('Digite um mes valido')
    elif dia < 1 or dia > 31:
        raise ValueError('Digite um dia valido')
    elif ano < 1920 or ano > hoje.year:
        raise ValueError('Digite um ano valido')
    

name = coleta_dados(coleta = 'Digite seu nome: ', tipo = str)
lastname = coleta_dados(coleta = 'Digite seu sobrenome: ', tipo = str)
altura = coleta_dados(coleta = 'Digite sua altura: ', tipo = float)

ano_nascimento = 0
mes_de_nascimento = 0
dia_de_nascimento = 0

while True:
    # Entrada de dados para idade
    ano_nascimento = coleta_dados(coleta = 'Digite sua data de nascimento: ', tipo = int)
    mes_de_nascimento = coleta_dados(coleta = 'Digite seu mes de nascimento: ', tipo = int)
    dia_de_nascimento = coleta_dados(coleta = 'Digite seu dia de nascimento:', tipo = int )

    try:
        valida_dados(ano_nascimento, mes_de_nascimento, dia_de_nascimento)
        break # cierra el loop
    except ValueError as e:
        print(e)


# Calculo de idade

hoje = datetime.now()
aniversario_passou =(hoje.month, hoje.day) >= (mes_de_nascimento, dia_de_nascimento)
age = hoje.year - ano_nascimento - (0 if aniversario_passou else 1)


print(f'Nome:{name} \nSobrenome:{lastname} \nIdade:{age} \nAno de Nascimento:{ano_nascimento} \nAltura:{altura}')

