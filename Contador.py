# Crie uma classe Contador que inicializa com um valor e possui métodos para:
# - incrementar() - aumenta o contador em 1
# - decrementar() - diminui o contador em 1
# - valor() - retorna o valor atual

class Contador:
    def __init__(self, valor_inicial=0):
        """Inicializa o contador com o valor fornecido (0 por padrão)"""
        self.valor_atual = valor_inicial
    
    def incrementar(self):
        """Aumenta o contador em 1 unidade"""
        self.valor_atual += 1
    
    def decrementar(self):
        """Diminui o contador em 1 unidade"""
        self.valor_atual -= 1
    
    def valor(self):
        """Retorna o valor atual do contador"""
        return self.valor_atual

# Exemplo de uso
contador = Contador(5)  # Inicia com valor 5
contador.incrementar()  # Valor passa a ser 6
contador.incrementar()  # Valor passa a ser 7
contador.decrementar()  # Valor volta a ser 6
print(contador.valor())  # Imprime 6