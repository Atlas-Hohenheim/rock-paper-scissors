#Pedra, papel ou tesoura

from pedra_papel_tesoura.funcoes.funcoes import *
jogo = ["PEDRA", "PAPEL", "TESOURA"]
resp = "S"
placar_jogador = 0
placar_maquina = 0
while resp == "S":
    import random
    import sys
    maquina = random.choice(jogo) 
    if placar_jogador - placar_maquina < 3:
        jogador = str(input("Bem-vindo ao jogo (você perdeu, aliás) \nDigite Pedra, papel ou tesoura: ").upper())
        resultado = jogar(jogador, maquina, placar_jogador, placar_maquina)
        if jogador == "PEDRA" and maquina == "PAPEL":
            placar_maquina += 1
        elif jogador == "PEDRA" and maquina == "TESOURA":
            placar_jogador += 1
        elif jogador == "PAPEL" and maquina == "PEDRA":
            placar_jogador += 1
        elif jogador == "PAPEL" and maquina == "TESOURA":
            placar_maquina += 1
        elif jogador == "TESOURA" and maquina == "PEDRA":
            placar_maquina += 1
        elif jogador == "TESOURA" and maquina == "PAPEL":
            placar_jogador += 1
        print(f"\nVocê escolheu: {jogador}\nContra: {maquina}")
        print(f"Você fez {placar_jogador} pontos.\nContra meus {placar_maquina} pontos.")
        resp = str(input("\nVocê deseja jogar novamente? Humano...\nDigite <S> para sim e <N> para não: ")).upper()
    else:
        print("\n>>>Chega, humano! Você já me ultrapassou em 3 pontos!")
        sys.exit()
print("\n>>>Humanos sempre desistem...")