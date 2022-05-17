#!/usr/bin/env python
# coding: utf-8

# In[1]:


cadastro_alunos = []


def cadastrar(indice_existente = None):
    #matriculando alunos
        aluno =  {
        "Matrícula do aluno": "",
        "Nome do aluno: ": "",
        "Data de nascimento": "",
        "CPF: ": "",
        "Telefone: ": "",
        "Idioma: ": "",
        "Turno: ": ""
        }
        
        print("Digite os campos abaixo para cadastrar um aluno:")
        for indice in aluno:
            aluno[indice] = input(indice + ": ")
            
        if indice_existente is None:
            cadastro_alunos.append(aluno)
            print("Aluno cadastrado com sucesso.")
        else:
            cadastro_alunos[indice_existente] = aluno
            print("Aluno atualizado com sucesso.")
   
        return

def pesquisar():
    #pesquisando aluno matriculado
     if len(cadastro_alunos) > 0:
        aluno =  {
        "Matrícula do aluno": "",
        "Nome do aluno: ": "",
        "Data de nascimento": "",
        "CPF: ": "",
        "Telefone: ": "",
        "Idioma: ": "",
        "Turno: ": ""
        }
        
        alunos_encontrados = []
        
        termo_pesquisa = input("Digite a matrícula do aluno: ")
        for indice in aluno:
            alunos_encontrados.extend([aluno for aluno in cadastro_alunos if termo_pesquisa.lower() in str(aluno[indice]).lower()])
        
        if len(alunos_encontrados) > 0:
            print('Aluno')
            print("Matrícula do aluno".center(14))
            print("Nome do aluno".center(30))
            print("Data de nascimento".center(12))
            print("CPF".center(15))
            print("Telefone".center(15))
            print("Idioma".center(12))
            print("Turno".center(20))
            
        
            for posicao_e_aluno in list(enumerate(alunos_encontrados, start=1)):
                
                posicao_encontrada = posicao_e_aluno[0]
                aluno_encontrado = posicao_e_aluno[1]
                
                print(str(posicao_encontrada).center(3))
                print(str(aluno_encontrado['Matrícula do aluno']).center(14))
                print(str(aluno_encontrado['Nome do aluno']).center(30))
                print(str(aluno_encontrado['Data de nascimento']).center(12))
                print(str(aluno_encontrado['CPF']).center(15))
                print(str(aluno_encontrado['Telefone']).center(15))
                print(str(aluno_encontrado['Idioma']).center(12))                       
                print(str(aluno_encontrado['Turno']).center(20))
        else:
            print(f"Nenhum aluno encontrado para o termo: {termo_pesquisa}")
     else:
        print("Não há alunos matriculados.")
        
     return

def imprimir():
    #imprimindo lista de alunos matriculados
    if len(cadastro_alunos) > 0:
            print('Alunos matriculados')
            print("Nr".center(3))
            print("Matrícula do aluno".center(14))
            print("Nome do aluno".center(30))
            print("Data de nascimento".center(12))
            print("CPF".center(15))
            print("Telefone".center(15))
            print("Idioma".center(12))
            print("Turno".center(20))
        

    for posicao_e_aluno in list(enumerate(cadastro_alunos, start=1)):
            
            posicao = posicao_e_aluno[0]
            aluno = posicao_e_aluno[1]
            
            print(str(posicao).center(3))
            print(str(aluno['Matrícula do aluno']).center(14))
            print(str(aluno['Nome do aluno']).center(30))
            print(str(aluno['Data de nascimento']).center(12))
            print(str(aluno['CPF']).center(15))
            print(str(aluno['Telefone']).center(15))
            print(str(aluno['Idioma']).center(12))                           
            print(str(aluno['Turno']).center(20))
    else:
        print("Não há alunos matriculados")
    
    return

def remover():
    #removendo alunos do sistema
    if len(cadastro_alunos) > 0:
        
        matricula_informada = input("Digite o número de matrícula para remover o aluno do sistema: ")
        alunos_encontrados_por_matricula = [aluno for aluno in cadastro_alunos if matricula_informada == str(aluno['Matrícula do aluno'])]
        
        if len(alunos_encontrados_por_matricula) > 0:
            for aluno_encontrado in alunos_encontrados_por_matricula:
                cadastro_alunos.remove(aluno_encontrado)
            
            print(f"Foram removidos {len(alunos_encontrados_por_matricula)} alunos com a matrícula {matricula_informada}")
        else:
            print(f"Não foram encontrados alunos com a matrícula {matricula_informada}")
                            
    else:
        print("Não é possível remover nenhum aluno porque não há alunos matriculados.")
        
    return

def atualizar():
    #atualizar alunos no sitema
    quantidade_alunos_sistema = len(cadastro_alunos)
    
    if quantidade_alunos_sistema > 0:
        
        imprimir()
        
        indice_informado = int(input("Digite o número da matrícula do aluno para atualizar o cadastro: "))
        
        if indice_informado > quantidade_alunos_sistema or indice_informado < 1:
            print("O número da matrícula precisa ser maior que zero e existir no sistema.")
        else:
            cadastrar(indice_informado-1)                            
    else:
        print("Não é possível atualizar nenhum cadastro porquenão há alunos matriculados.") 
                                
    return

def tela_menu():
    print("\n\t\t\t  [1] >> Matricular Aluno");
    print("\n\t\t\t  [2] >> Pesquisar Aluno Matriculado");
    print("\n\t\t\t  [3] >> Listar Alunos Matriculados");
    print("\n\t\t\t  [4] >> Apagar Registro de Aluno");
    print("\n\t\t\t  [5] >> Atualizar Registro de Aluno");
    print("\n\t\t\t  ===================================\n");
    print("\n\t\t\t  [0] >> Sair");
    
tela_menu()
opcao = int(input())

while 0 <= opcao <= 6:
    
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        pesquisar()
    elif opcao == 3:
        imprimir()    
    elif opcao == 4:
        remover()
    elif opcao == 5:
        atualizar()
    elif opcao == 0:
        print('Programa encerrado')
        exit()
    
    tela_menu()
    opcao = int(input())
    
else:
        print('Opção inválida, programa encerrado')


# In[ ]:




