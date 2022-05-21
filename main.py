import os
import random
from colorama import Fore


def tela():
    global jogo
    os.system("cls")  # Limpa a tela
    print('Jogo da Velha')
    print('   ' + jogo[0][0] + "| " + jogo[0][1] + " | " + jogo[0][2], '      1 | 2 | 3')
    print('-' * 13)
    print('   ' + jogo[1][0] + "| " + jogo[1][1] + " | " + jogo[1][2], '      4 | 5 | 6')
    print('-' * 13)
    print('   ' + jogo[2][0] + "| " + jogo[2][1] + " | " + jogo[2][2], '      7 | 8 | 9')
    print('Jogadas: ' + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogadorJoga():
    global quemJoga, jogadas, jogador1
    if quemJoga == 2 and jogadas <= maxJogadas:
        while True:
            while True:
                try:
                    x = int(input('Sua vez: '))
                    if 0 <= x <= 9:
                        break
                except ValueError:
                    print('Você digitou um valor não numérico, tente novamente...')
            if x == 1 and jogo[0][0] == ' ':
                jogo[0][0] = jogador1
                break
            elif x == 2 and jogo[0][1] == ' ':
                jogo[0][1] = jogador1
                break
            elif x == 3 and jogo[0][2] == ' ':
                jogo[0][2] = jogador1
                break
            elif x == 4 and jogo[1][0] == ' ':
                jogo[1][0] = jogador1
                break
            elif x == 5 and jogo[1][1] == ' ':
                jogo[1][1] = jogador1
                break
            elif x == 6 and jogo[1][2] == ' ':
                jogo[1][2] = jogador1
                break
            elif x == 7 and jogo[2][0] == ' ':
                jogo[2][0] = jogador1
                break
            elif x == 8 and jogo[2][1] == ' ':
                jogo[2][1] = jogador1
                break
            elif x == 9 and jogo[2][2] == ' ':
                jogo[2][2] = jogador1
                break
            print('Campo ja preenchido,tente novamente')
        tela()
        quemJoga = 1
        jogadas += 1
    return


def cpuJoga():
    global quemJoga, jogadas, cpu
    if quemJoga == 1 and jogadas < maxJogadas:
        while True:
            x = random.randrange(0, 10)
            if x == 1 and jogo[0][0] == ' ':
                jogo[0][0] = cpu
                break
            elif x == 2 and jogo[0][1] == ' ':
                jogo[0][1] = cpu
                break
            elif x == 3 and jogo[0][2] == ' ':
                jogo[0][2] = cpu
                break
            elif x == 4 and jogo[1][0] == ' ':
                jogo[1][0] = cpu
                break
            elif x == 5 and jogo[1][1] == ' ':
                jogo[1][1] = cpu
                break
            elif x == 6 and jogo[1][2] == ' ':
                jogo[1][2] = cpu
                break
            elif x == 7 and jogo[2][0] == ' ':
                jogo[2][0] = cpu
                break
            elif x == 8 and jogo[2][1] == ' ':
                jogo[2][1] = cpu
                break
            elif x == 9 and jogo[2][2] == ' ':
                jogo[2][2] = cpu
                break
    tela()
    quemJoga = 2
    jogadas += 1
    return


def verificaWin():
    global winCpu, winJogador
    if ((jogo[0][0] == jogador1 and jogo[0][1] == jogador1 and jogo[0][2] == jogador1) or
            (jogo[1][0] == jogador1 and jogo[1][1] == jogador1 and jogo[1][2] == jogador1) or
            (jogo[2][0] == jogador1 and jogo[2][1] == jogador1 and jogo[2][2] == jogador1) or
            (jogo[0][0] == jogador1 and jogo[1][0] == jogador1 and jogo[2][0] == jogador1) or
            (jogo[0][1] == jogador1 and jogo[1][1] == jogador1 and jogo[2][1] == jogador1) or
            (jogo[0][2] == jogador1 and jogo[1][2] == jogador1 and jogo[2][2] == jogador1) or
            (jogo[0][0] == jogador1 and jogo[1][1] == jogador1 and jogo[2][2] == jogador1) or
            (jogo[0][2] == jogador1 and jogo[1][1] == jogador1 and jogo[2][0] == jogador1)):
        print('jogador ganhou')
        winJogador += 1
        return True
    else:
        if ((jogo[0][0] == cpu and jogo[0][1] == cpu and jogo[0][2] == cpu) or
                (jogo[1][0] == cpu and jogo[1][1] == cpu and jogo[1][2] == cpu) or
                (jogo[2][0] == cpu and jogo[2][1] == cpu and jogo[2][2] == cpu) or
                (jogo[0][0] == cpu and jogo[1][0] == cpu and jogo[2][0] == cpu) or
                (jogo[0][1] == cpu and jogo[1][1] == cpu and jogo[2][1] == cpu) or
                (jogo[0][2] == cpu and jogo[1][2] == cpu and jogo[2][2] == cpu) or
                (jogo[0][0] == cpu and jogo[1][1] == cpu and jogo[2][2] == cpu) or
                (jogo[0][2] == cpu and jogo[1][1] == cpu and jogo[2][0] == cpu)):
            print('CPU ganhou')
            winCpu += 1
            return True
    return False


# *************** PROGRAMA PRINCIPAL ***************

jogadas = 0
quemJoga = 2
maxJogadas = 9
jogo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
jogador1 = 'X'
winJogador = 0
cpu = 'O'
winCpu = 0
vit = False
tela()
while True:
    jogadorJoga()
    cpuJoga()
    vit = verificaWin()
    if vit:
        print('Placar : {} Jogador - {} Cpu'.format(winJogador, winCpu))
        while True:
            try:
                question = input('GAME OVER, deseja jogar novamente?\n >> S or N :')
                if question.upper() == 'S' or question.upper() == 'N':
                    break
            except:
                continue
        if question.upper() != 'S':
            exit()
        else:
            jogo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            jogadas = 0
            tela()
