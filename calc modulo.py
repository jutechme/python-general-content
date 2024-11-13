#FINCAO OTIMIAZADA
#parametros
#def soma(n1,n2):
 #    print (n1+n2)
#soma()

def funcoes():
    n1 = float(input('<<'))
    n2 = float(input('<'))
    soma = n1 + n2
    print(soma)


def funcoes2():
    n1 = float(input('<<'))
    n2 = float(input('<'))
    sub = n1 - n2
    print(sub)

def funcoes3():
    n1 = float(input('<<'))
    n2 = float(input('<'))
    mult = n1 * n2
    print(mult)    

def funcoes3():
    n1 = float(input('<<'))
    n2 = float(input('<'))
    div = n1 / n2
    print(div)  

    
    from funcoes import *
def calculadora():
    opr =input('operacao>>')
    if opr == '+':
        soma()
    elif opr == "-":
        sub()
    elif opr == '*':
        mut()
    elif opr == '/':
        div()
    else:
        print('digite algo valido ')       