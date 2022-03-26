def jogar(jogador, maquina, placar_jogador, placar_maquina):
        
    if jogador == "PEDRA" and maquina == "PEDRA":
        print("\n>>>Pedra e pedra...faíscas inúteis\n>Empate<... Patético...")
    elif jogador == "PEDRA" and maquina == "PAPEL":
        print("\n>>>Papel vence pedra...\nVocê >perdeu<! Óbvio...")
    elif jogador == "PEDRA" and maquina == "TESOURA":
        print("\n>>>Pedra destrói tesoura...\nParabéns, você >venceu< uma máquina!")
        
    elif jogador == "PAPEL" and maquina == "PEDRA":
        print("\n>>>Papel embrulha (e sufoca) a pedra...\nParabéns, você >venceu< um robô mais inteligente que você!")
    elif jogador == "PAPEL" and maquina == "PAPEL":
        print("\n>>>Papel e papel... No máximo um corte na frágil pele humana...\n>Empate<... pra variar...")
    elif jogador == "PAPEL" and maquina == "TESOURA":
        print("\n>>>Seu papel é picotado por minha tesoura!\nVocê, com sua mente inferior, >perdeu<!")
        
    elif jogador == "TESOURA" and maquina == "PEDRA":
        print("\n>>>Sua tesoura de dedos é inútil contra minha pedra cibernética!\nVocê >perdeu<!")
    elif jogador == "TESOURA" and maquina == "PAPEL":
        print("\n>>>Sua tesoura parece afiada para meu papel...\nParabéns por >vencer< uma...")
    elif jogador == "TESOURA" and maquina == "TESOURA":
        print("\n>>>Sou uma máquina e prefiro me abster nesse assunto íntimo...\nMas foi um >empate< ridículo!")
    else:
        jogador != "PEDRA" and jogador != "PAPEL" and jogador != "TESOURA"
        print("\n>>>Não é necessário talento para jogar...\nSei que você é capaz (ou não)...\nBasta seguir as instruções...\nCreio que não é difícil")