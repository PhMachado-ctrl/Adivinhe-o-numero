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