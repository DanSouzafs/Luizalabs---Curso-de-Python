def formatar_mensagem(texto):
    # Remove espaços extras do início e do fim da string
    texto = texto.strip()
    
    # Se a string ficou vazia após o strip, retorne a string vazia
    if not texto:
        return texto
    
    # Converte o texto para minúsculas
    texto = texto.lower()
    
    # Separa o texto em palavras (split sem argumentos remove todos os espaços extras)
    # e depois junta as palavras com um único espaço
    palavras = texto.split()
    mensagem_formatada = ' '.join(palavras)
    
    # Retorne o texto já formatado conforme as regras
    return mensagem_formatada

# Lê a mensagem enviada ao robô via input padrão
entrada = input()  # Tipo de dado esperado: str

# Chama a função formatar_mensagem (você irá implementar a lógica)
saida = formatar_mensagem(entrada)

# Exibe a mensagem padronizada
print(saida)