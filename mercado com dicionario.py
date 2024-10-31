#sistema de mercado 
print('ola bem vindo(a) ao mercado ')
produtos = {'maracuja':19,
            'uva':5,
            'limão': 8,
            'morango': 38,
            'laranja' :17            }
lista =[]
lista1 =[]
for chave,valor in produtos.items():
    lista.append(chave)
    lista1.append(valor)
print (lista,lista1)
carrinho=[]
escolha = str(input('escolha o produto para compra '))
carrinho.append (produtos[escolha])
print('produto',carrinho,00)
valores =[]
pagamento =['pix','credito','debito']
escolha1 = int(input('digite a forma de pagamento '))
valores.append(pagamento[escolha1])
print (valores)
print('obrigada pela sua compra ')