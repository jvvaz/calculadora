# Complete as funcoes a seguir

def  soma ( a , b ):
	  print(a+b)

def  subtrai ( a , b ):
    print (a-b)

def  multiplica ( a , b ):
	print (a*b)

def  divide ( a , b ):
  #usando 'if' e 'else' para mostrar mensagem de erro, caso a variável b seja igual a "0".
  if b == 0:
    print('Nenhum número pode dividido por 0. Digite outro número maior que zero.')
  else:
    print (a/b)


# Programa principal

print ( " Calculadora simples " )

num1 =  float ( input ( " Insira o primeiro número: " ))
num2 =  float ( input ( " Insira o segundo número: " ))

soma (num1, num2)
subtrai (num1, num2)
multiplica (num1, num2)
divide (num1, num2)

