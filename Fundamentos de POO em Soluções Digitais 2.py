class Robo:
    def __init__(self, modelo1, modelo2):
        # Inicializa os atributos do robô com os dois modelos
        self.modelo1 = modelo1
        self.modelo2 = modelo2
    
    def obter_nome_completo(self):
        # Retorna o nome completo do robô no formato modelo1-modelo2
        return f"{self.modelo1}-{self.modelo2}"


# Lê a entrada e separa os dois modelos
entrada = input().split()
modelo1 = entrada[0]
modelo2 = entrada[1]

# Cria o objeto Robô com os modelos recebidos
robo = Robo(modelo1, modelo2)

# Imprime o nome completo do robô
print(robo.obter_nome_completo())