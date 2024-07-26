# pedra-papel-tesoura-python
# Jogo de Pedra, Papel e Tesoura

Este é um simples jogo de "Pedra, Papel e Tesoura" implementado em Python. O jogo permite que um jogador humano jogue contra o computador. O projeto é ideal para aprender conceitos básicos de programação em Python e prática de lógica de jogo.

## 🚀 Começando

Essas instruções ajudarão você a obter uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implantação)** para saber como implantar o projeto.

### 📋 Pré-requisitos

Você precisará ter o Python 3.x instalado na sua máquina para executar o jogo. Para verificar se o Python está instalado e qual versão, você pode usar o seguinte comando no terminal:

```
python --version
```

Se o Python não estiver instalado, você pode baixá-lo do [site oficial do Python](https://www.python.org/downloads/).

### 🔧 Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento e executar o jogo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/MayconWork/pedra-papel-tesoura-python.git
   cd pedra-papel-tesoura-python

2. **(Opcional) Crie um ambiente virtual:**
    É uma boa prática criar um ambiente virtual para gerenciar as dependências do projeto.
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. **Execute o Jogo:**
    python jogo.py

## ⚙️ Regras do Jogo
O jogo "Pedra, Papel e Tesoura" é jogado entre um jogador humano e o computador. As regras são simples:

    * Pedra vence Tesoura.
    * Tesoura vence Papel.
    * Papel vence Pedra.

Se ambos os jogadores escolherem a mesma opção, o resultado é um Empate.

### 📊 Tabela Verdade

Aqui está a tabela verdade para o jogo, mostrando todas as combinações possíveis de escolhas e seus resultados:

| Jogador 1 | Jogador 2 | Resultado        |
|-----------|-----------|------------------|
| Pedra     | Pedra     | Empate           |
| Pedra     | Papel     | Computador venceu|
| Pedra     | Tesoura   | Você venceu      |
| Papel     | Pedra     | Você venceu      |
| Papel     | Papel     | Empate           |
| Papel     | Tesoura   | Computador venceu|
| Tesoura   | Pedra     | Computador venceu|
| Tesoura   | Papel     | Você venceu      |
| Tesoura   | Tesoura   | Empate           |

## ⚙️ Executando os testes
    "On Working"

## 🔩 Analise os testes de ponta a ponta
Para garantir que o jogo funcione conforme o esperado, você pode adicionar testes que verifiquem as regras do jogo, como:

Verificar se as escolhas do jogador e do computador são validadas corretamente.
Testar os cenários de vitória, derrota e empate.

## 📦 Implantação
Este é um projeto simples que pode ser executado em qualquer sistema com Python instalado. Para implantar em um sistema ativo, simplesmente siga os passos de instalação em qualquer máquina com Python.

## 🧩 Como Funciona o Código

Abaixo está uma descrição detalhada sobre como o código do jogo "Pedra, Papel e Tesoura" foi implementado.

### 📂 Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- **`jogo.py`**: O arquivo principal que contém a lógica do jogo.
- **`README.md`**: Este arquivo, que fornece informações sobre o projeto.
- **`requirements.txt`**: (Opcional) Arquivo que lista as dependências do projeto, se houver.

### 📝 Detalhes do Código

#### 1. **Importações e Configuração**

No início do arquivo `jogo.py`, são importadas as bibliotecas necessárias. No caso deste jogo, apenas a biblioteca padrão é utilizada:

    ```
    python
    import random
    ```

A biblioteca random é usada para permitir que o computador faça uma escolha aleatória entre Pedra, Papel e Tesoura.

#### 2. ** Função obter_escolha_computador**

Esta função retorna uma escolha aleatória do computador:

    ```
    def obter_escolha_computador():
    opcoes = ['pedra', 'papel', 'tesoura']
    return random.choice(opcoes)
    ```

    * Explicação: A função random.choice(opcoes) seleciona aleatoriamente uma opção da lista opcoes.

#### 3. **Função obter_resultado**

Esta função compara as escolhas do jogador e do computador e determina o resultado do jogo:

    ```
    def obter_resultado(escolha_jogador, escolha_computador):
        if escolha_jogador == escolha_computador:
            return "Empate"
        elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
            (escolha_jogador == 'papel' and escolha_computador == 'pedra') or \
            (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
            return "Você venceu"
        else:
            return "Computador venceu"
    ```

    *Explicação: A função compara as escolhas do jogador e do computador. Dependendo das escolhas, ela retorna "Você venceu", "Computador venceu" ou "Empate".

#### 4. **Função jogar**

A função principal que controla o fluxo do jogo:

    ```
    def jogar():
        escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
        escolha_computador = obter_escolha_computador()
        resultado = obter_resultado(escolha_jogador, escolha_computador)
        
        print(f"Você escolheu: {escolha_jogador}")
        print(f"O computador escolheu: {escolha_computador}")
        print(f"Resultado: {resultado}")
    ```

    *Explicação:
        ** Entrada do Usuário: O jogador insere sua escolha.
        ** Obtenção da Escolha do Computador: A função obter_escolha_computador é chamada para gerar a escolha do computador.
        ** Determinação do Resultado: A função obter_resultado é chamada para calcular o resultado do jogo com base nas escolhas.
        ** Saída: O jogo exibe a escolha do jogador, a escolha do computador e o resultado.

### ⚙️ Execução do Jogo
Quando o código é executado, o usuário é solicitado a inserir uma escolha (Pedra, Papel ou Tesoura). O computador faz uma escolha aleatória, e o resultado do jogo é exibido na tela. O jogo pode ser executado várias vezes para verificar diferentes cenários e resultados.
