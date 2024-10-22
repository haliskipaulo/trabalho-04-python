import pandas as pd
import matplotlib.pyplot as plt

arq = pd.read_txt("") 

def resumo():
    print()

def historico():
    print()
    
def grafico_historico():
    print()

def grafico_pizza():
    print()

def grafico_linhas():
    print()




while True:

    print()
    print()
    print("===== MENU  ===== ")
    print('1. Resumo das Conversas')
    print('2. Historico Remetentes')
    print('3. Grafico historico do remetente')
    print('4. Grafico Pizza')
    print('5. Grafico Linhas')
    print('6. Sair')
        
        
    opcao = input('Escolha uma opção: ')
        
    if opcao == '1':
        resumo()    
           
    elif opcao == '2':
        historico()
          
    elif opcao == '3':
        grafico_historico()
            
    elif opcao == '4':        
        grafico_pizza()
            
    elif opcao == '5':        
        grafico_linhas()            

    elif opcao == '6':           
        print('==== Saindo... ====')       
        print()
        break

    else:
        print('Opção inválida.')