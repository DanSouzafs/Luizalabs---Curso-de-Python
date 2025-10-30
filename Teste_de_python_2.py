def identificar_categoria_gadget(codigo):
    """
    Recebe uma string 'codigo' e retorna a categoria associada:
    - 'T': tablet
    - 'P': phone
    - 'N': notebook
    Se não corresponder, retorna 'unknown'.
    """
    # Verifica se o código não está vazio
    if not codigo:
        return "unknown"
    
    # Obtém a primeira letra do código
    primeira_letra = codigo[0]
    
    # Identifica a categoria baseada na primeira letra
    if primeira_letra == 'T':
        return "tablet"
    elif primeira_letra == 'P':
        return "phone"
    elif primeira_letra == 'N':
        return "notebook"
    else:
        return "unknown"

# Leitura da entrada (espera-se uma string representando o código do gadget)
codigo_gadget = input().strip()

# Chamada da função e saída do resultado
categoria = identificar_categoria_gadget(codigo_gadget)

print(categoria)  # Deve imprimir uma das categorias ou 'unknown'