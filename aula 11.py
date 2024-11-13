#try:
 #   teste= 10/10
  #  print(teste)
#except:zerodivisionbyerror as erro:
 #   print(erro)
#else:
 #   print('erro')    
    

#Exercício 1:
#Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
try:
    num= int(input('digite m num  '))
except ValueError:
  print('isso nao é um numero ')

#Exercício 2:
#Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
try:
    n =int(input('digite um nrm'))
    n2 =int(input('digite um nrm'))
    div= n/n2
except ZerodivisionError:
    print('a divisao nao pode ser feita co o zero')

#Exercício 3:
#Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
lista = [1,2,3]
def verificar (lista):
    try:
        n1= (imput('..'))
        i= lista[n1]
        print('i')
    except:
         print('indice nao existe')
#Exercício 4:
#Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.
def manipule():
    try:
         n3= int (input('='))
         n4= int (input('='))
         div= n3/n4
           except:zerodivionerror:
        print('a divisao nao pode ser feita por zero')
                       