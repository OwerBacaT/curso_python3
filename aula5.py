
# variaveis e tipos de dados para exercicios 

# input de variaveis

nome = str(input("Informe seu nome: "))
sobrenome = str(input("Informe seu Sobrenome: "))
idade = int(input("Informe sua idade: "))
ano_nascimento = int(input("Informe sua data de nascimento: "))
altura_metros = float(input("Informe sua altura: "))

# '''Condicional'''
if idade >= 18:
    print(f'Nome: {nome} \nSobrenome: {sobrenome} \nIdade: {idade} \nAltura em metros: {altura_metros} \nÉ maior de idade')

else:
    print(f'Nome: {nome} \nSobrenome: {sobrenome} \nIdade: {idade} \nAltura em metros: {altura_metros} \nÉ menor de idade')




# Refatorando codigo acima para melhores praticas de desenvolvimento
'''
main()
├─ coletar_dados_usuario()
│  ├─ solicitar_input() [função reutilizável]
│  └─ retorna dicionário
├─ validar_dados()
│  ├─ validar_idade()
│  ├─ validar_altura()
│  └─ retorna True/False
├─ processar_dados()
│  ├─ calcular_idade_a_partir_do_ano()
│  ├─ determinar_maioridade()
│  └─ retorna dados processados
└─ exibir_resultados()
   └─ formata e imprime
'''
'''
╔════════════════════════════════════════════════════════════╗
║              PROGRAMA: CADASTRO DE USUÁRIO                ║
╚════════════════════════════════════════════════════════════╝

INÍCIO DO PROGRAMA

    ┌─────────────────────────────────────────┐
    │ PASSO 1: COLETAR DADOS DO USUÁRIO       │
    └─────────────────────────────────────────┘
    
    usuario = {}
    
    nome = SOLICITAR_INPUT("Qual seu nome?", TIPO_TEXTO)
    usuario.nome = nome
    
    sobrenome = SOLICITAR_INPUT("Qual seu sobrenome?", TIPO_TEXTO)
    usuario.sobrenome = sobrenome
    
    idade = SOLICITAR_INPUT("Qual sua idade?", TIPO_NÚMERO)
    usuario.idade = idade
    
    altura = SOLICITAR_INPUT("Qual sua altura em metros?", TIPO_DECIMAL)
    usuario.altura = altura
    
    
    ┌─────────────────────────────────────────┐
    │ PASSO 2: VALIDAR OS DADOS COLETADOS     │
    └─────────────────────────────────────────┘
    
    SE nome está vazio ENTÃO
        MOSTRAR erro: "Nome não pode ser vazio"
        VOLTAR ao PASSO 1
    FIM SE
    
    SE idade < 0 OU idade > 150 ENTÃO
        MOSTRAR erro: "Idade inválida"
        VOLTAR ao PASSO 1
    FIM SE
    
    SE altura <= 0 OU altura > 2.5 ENTÃO
        MOSTRAR erro: "Altura inválida"
        VOLTAR ao PASSO 1
    FIM SE
    
    
    ┌─────────────────────────────────────────┐
    │ PASSO 3: PROCESSAR OS DADOS             │
    └─────────────────────────────────────────┘
    
    SE idade >= 18 ENTÃO
        usuario.maiorDeIdade = VERDADEIRO
    SENÃO
        usuario.maiorDeIdade = FALSO
    FIM SE
    
    usuario.iniciaisNome = PEGAR_PRIMEIRA_LETRA(nome) + 
                           PEGAR_PRIMEIRA_LETRA(sobrenome)
    
    
    ┌─────────────────────────────────────────┐
    │ PASSO 4: EXIBIR RESULTADOS              │
    └─────────────────────────────────────────┘
    
    EXIBIR "╔════════════════════════════════╗"
    EXIBIR "║   DADOS DO USUÁRIO CADASTRADO  ║"
    EXIBIR "╚════════════════════════════════╝"
    EXIBIR ""
    EXIBIR "Nome completo: " + usuario.nome + " " + usuario.sobrenome
    EXIBIR "Idade: " + usuario.idade + " anos"
    EXIBIR "Altura: " + usuario.altura + " metros"
    EXIBIR "Maior de idade? " + usuario.maiorDeIdade
    EXIBIR "Iniciais: " + usuario.iniciaisNome
    
FIM DO PROGRAMA

'''
'''
╔═══════════════════════════════════════════════════════════╗
║  ESTRUTURA COM SEPARAÇÃO DE RESPONSABILIDADES             ║
╚═══════════════════════════════════════════════════════════╝


FUNÇÃO solicitar_input(mensagem, tipo_esperado)
    ┌─────────────────────────────────┐
    │ RESPONSABILIDADE: Pedir dados   │
    │ ENTRADA: mensagem e tipo        │
    │ SAÍDA: valor convertido         │
    └─────────────────────────────────┘
    
    TENTÁTIVAR
        valor = MOSTRAR_INPUT(mensagem)
        
        SE tipo_esperado == NÚMERO ENTÃO
            valor = CONVERTER_PARA_NÚMERO(valor)
        FIM SE
        
        RETORNAR valor
        
    CAPTURAR erro
        MOSTRAR "Entrada inválida, tente novamente"
        CHAMAR solicitar_input(mensagem, tipo_esperado) NOVAMENTE
    FIM TENTAR
    
FIM FUNÇÃO


FUNÇÃO validar_idade(idade)
    ┌──────────────────────────────────┐
    │ RESPONSABILIDADE: Validar idade  │
    │ ENTRADA: valor da idade          │
    │ SAÍDA: verdadeiro ou falso       │
    └──────────────────────────────────┘
    
    SE idade < 0 ENTÃO
        RETORNAR FALSO
    FIM SE
    
    SE idade > 150 ENTÃO
        RETORNAR FALSO
    FIM SE
    
    RETORNAR VERDADEIRO
    
FIM FUNÇÃO


FUNÇÃO validar_altura(altura)
    ┌──────────────────────────────────┐
    │ RESPONSABILIDADE: Validar altura │
    │ ENTRADA: valor da altura         │
    │ SAÍDA: verdadeiro ou falso       │
    └──────────────────────────────────┘
    
    SE altura <= 0 ENTÃO
        RETORNAR FALSO
    FIM SE
    
    SE altura > 2.5 ENTÃO
        RETORNAR FALSO
    FIM SE
    
    RETORNAR VERDADEIRO
    
FIM FUNÇÃO


FUNÇÃO validar_nome(nome)
    ┌──────────────────────────────────┐
    │ RESPONSABILIDADE: Validar nome   │
    │ ENTRADA: valor do nome           │
    │ SAÍDA: verdadeiro ou falso       │
    └──────────────────────────────────┘
    
    SE nome está vazio ENTÃO
        RETORNAR FALSO
    FIM SE
    
    SE COMPRIMENTO(nome) < 2 ENTÃO
        RETORNAR FALSO
    FIM SE
    
    RETORNAR VERDADEIRO
    
FIM FUNÇÃO


FUNÇÃO coletar_dados()
    ┌──────────────────────────────────────┐
    │ RESPONSABILIDADE: Coletar e validar  │
    │ ENTRADA: nenhuma                     │
    │ SAÍDA: dicionário com dados válidos  │
    └──────────────────────────────────────┘
    
    usuario = {}
    
    REPETIR
        nome = solicitar_input("Qual seu nome?", TEXTO)
        SE validar_nome(nome) == FALSO ENTÃO
            MOSTRAR "Nome deve ter pelo menos 2 caracteres"
            CONTINUAR
        FIM SE
        usuario.nome = nome
        SAIR DA REPETIÇÃO
    FIM REPETIR
    
    REPETIR
        sobrenome = solicitar_input("Qual seu sobrenome?", TEXTO)
        SE validar_nome(sobrenome) == FALSO ENTÃO
            MOSTRAR "Sobrenome deve ter pelo menos 2 caracteres"
            CONTINUAR
        FIM SE
        usuario.sobrenome = sobrenome
        SAIR DA REPETIÇÃO
    FIM REPETIR
    
    REPETIR
        idade = solicitar_input("Qual sua idade?", NÚMERO)
        SE validar_idade(idade) == FALSO ENTÃO
            MOSTRAR "Idade deve estar entre 0 e 150"
            CONTINUAR
        FIM SE
        usuario.idade = idade
        SAIR DA REPETIÇÃO
    FIM REPETIR
    
    REPETIR
        altura = solicitar_input("Qual sua altura em metros?", DECIMAL)
        SE validar_altura(altura) == FALSO ENTÃO
            MOSTRAR "Altura deve estar entre 0 e 2.5"
            CONTINUAR
        FIM SE
        usuario.altura = altura
        SAIR DA REPETIÇÃO
    FIM REPETIR
    
    RETORNAR usuario
    
FIM FUNÇÃO


FUNÇÃO processar_dados(usuario)
    ┌──────────────────────────────────────┐
    │ RESPONSABILIDADE: Processar dados    │
    │ ENTRADA: dicionário do usuário       │
    │ SAÍDA: dados processados             │
    └──────────────────────────────────────┘
    
    SE usuario.idade >= 18 ENTÃO
        usuario.maiorDeIdade = VERDADEIRO
    SENÃO
        usuario.maiorDeIdade = FALSO
    FIM SE
    
    primeira_letra_nome = usuario.nome[0]
    primeira_letra_sobrenome = usuario.sobrenome[0]
    usuario.iniciais = primeira_letra_nome + primeira_letra_sobrenome
    
    RETORNAR usuario
    
FIM FUNÇÃO


FUNÇÃO exibir_resultados(usuario)
    ┌──────────────────────────────────────┐
    │ RESPONSABILIDADE: Exibir resultados  │
    │ ENTRADA: dicionário do usuário       │
    │ SAÍDA: nenhuma (apenas imprime)      │
    └──────────────────────────────────────┘
    
    MOSTRAR "╔════════════════════════════════╗"
    MOSTRAR "║  DADOS DO USUÁRIO CADASTRADO   ║"
    MOSTRAR "╚════════════════════════════════╝"
    MOSTRAR ""
    MOSTRAR "Nome: " + usuario.nome + " " + usuario.sobrenome
    MOSTRAR "Idade: " + usuario.idade + " anos"
    MOSTRAR "Altura: " + usuario.altura + " metros"
    MOSTRAR "Maior de idade? " + usuario.maiorDeIdade
    MOSTRAR "Iniciais: " + usuario.iniciais
    
FIM FUNÇÃO


╔═══════════════════════════════════════════════════════════╗
║              FLUXO PRINCIPAL (MAIN)                        ║
╚═══════════════════════════════════════════════════════════╝

PROGRAMA principal()
    
    usuario = coletar_dados()
    usuario = processar_dados(usuario)
    exibir_resultados(usuario)
    
FIM PROGRAMA
'''
