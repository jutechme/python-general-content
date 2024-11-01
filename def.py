def deposito(saldo,valor):
    return saldo - valor
def saque(saldo,valor):
     return saldo+valor
def extrato(saldo,valor):
     return saldo





def banco():
    saldo = 30000
    opcoes = ['saque','extrato', 'depósito']
    print (opcoes)
    my_nome = 1234
    my_senha = 389
    for i in range(3):
         nome = int(input('digite seu login '))
         senha = int(input('digite seu login '))
         if my_nome == nome and my_senha == senha:
            print("acesso permitido")
            op = input('1saque, 2 deposito, 3 extrato')
         if op == '1':
             valor = float(input('digite o valor '))
             saque = saque(saldo,valor)
             print (saque)
         elif op == '2':
             valor = float(input('digite o valor')
                           deposito = deposito(saldo,valor)
                           print (deposito)
         elif op == '3':
                           valor = float(input('digite o valor '))
                           extrato = extrato(saldo,valor)
                           print (extrato)
                 
            
            
            
            break
    else:
        print('dados errados tente nomanete')
        saldo = 30000
        valor = float(input('digite o valor '))
        calc = saldo - valor
        print (calc)
        
saque()        

    
