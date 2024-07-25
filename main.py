import random

class Jogador():
    def __init__ (self, nome):
        self.nome = nome
        self.escolha = None

    def fazer_escolha(self):
        pass

class jogadorHumano(Jogador):
    def fazer_escolha(self):
        escolhas_possiveis = ["Pedra", "Papel", "Tesoura"]
        escolha = input(f"{self.nome}, escolha Pedra, Papel ou Tesoura: ").capitalize()
        while escolha not in escolhas_possiveis:
            escolha = input("Escolha inválida! Escolha Pedra, Papel ou Tesoura: ").capitalize()
        self.escolha = escolha

class JogadorMaquina(Jogador):
    def fazer_escolha(self):
        escolhas = ["Pedra", "Papel", "Tesoura"]
        self.escolha = random.choice(escolhas)
        print(f"{self.nome} escolheu: {self.escolha}")

class Jogo:
    def __init__(self):
        self.jogador1 = jogadorHumano("Jogador1")
        self.jogador2 = JogadorMaquina("Maquina")

    def determinarVencedor(self):
        if self.jogador1.escolha == self.jogador2.escolha:
            print("Empate!")
        elif (self.jogador1.escolha == "Pedra" and self.jogador2.escolha == "Tesoura") or \
             (self.jogador1.escolha == "Papel" and self.jogador2.escolha == "Pedra") or \
             (self.jogador1.escolha == "Tesoura" and self.jogador2.escolha == "Papel"):
            return f"{self.jogador1.nome} venceu!"
        else:
            return f"{self.jogador2.nome} venceu!"
        
    def jogar(self):
        self.jogador1.fazer_escolha()
        self.jogador2.fazer_escolha()
        resultado = self.determinarVencedor()
        print(resultado)

if __name__ == "__main__":
    Jogo = Jogo()
    Jogo.jogar()