from art import *
import os
import pyautogui

pyautogui.hotkey('win', 'up')

tprint('Bem   Vindo   ao:\n')
tprint('SUPER   MARCOS   BROS')
tprint('\n\n\n')
tprint(' Obs:   Essa   e   apenas \n uma   versao   em   desolvimento')
print('\n\n')
tprint('Atualizações   em   breve!!!')
input('press enter to continue')
os.system('cls')

tprint(' Para   registrar   que   voce \n fez   parte   desse   desolvimento')
print('\n\n')
tprint('Por   favor   digite   seu   nome   e   seu   e-mail')

name = input('Insira seu nome: ')
input('press enter to continue')

email = input('Insira seu e-mail: ')
input('press enter to continue')

log = '*** ' 'Nome: ' + name + ' *** ' + 'E-mail: ' + email + ''' ***
'''
try:
    file = open('amigosDoProjeto.txt','r')
    leitura = file.readline()
    leitura = leitura + log

    file = open('amigosDoProjeto.txt','w')
    file.writelines(leitura)
    file.close()
except:
    file = open('amigosDoProjeto.txt','w')

    file = open('amigosDoProjeto.txt','r')
    leitura = file.readline()
    leitura = leitura + log

    file = open('amigosDoProjeto.txt','w')
    file.writelines(leitura)
    file.close()

tprint('Esta   pronto   para   comecar ?')
print('\n\n')
input('Press   enter   to   continue')
os.system('cls')


from superMarcosBros import startGame

while True:
    startGame()
