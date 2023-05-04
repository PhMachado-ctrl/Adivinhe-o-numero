'''Advinhe o número'''
#Módulos
import random #Importa a Biblioteca que gera valores aleatórios

#Coletar um número
print("Seja Bem vindo ao Guess Number!")
number = input("Digite o número teto do desafio: ")

#Verifica se é um número
if number.isdigit():
   number = int(number) #converte para inteiro
else:
   print("Erro: valor inormado não é numérico. Favor execure novamente e informe um número")
   quit()

#Pega um valor da operação randomica
random_number = random.randint(0, number)



#Pega a resposta do usuário
while True:
    answer = input("Adivinhe o número: ")

    if answer.isdigit():
        answer = int(answer)
    else:
        print("Erro: valor inormado não é numérico. Favor execure novamente e informe um número")
        continue #Repete o Loop do começa
    
    #Verifica se é igual ao numero
    if answer == number:
      print("Acertou!")
      break
    elif answer > number:
       print("Chutou alto, o número é menor que isso...")
    else:
       print("Chutou baixo, o número é maior que isso...")
       

   
  