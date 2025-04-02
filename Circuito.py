import math

class Circuito:
    def __init__(self, raio):
        """Inicializa um circuito/círculo com o raio especificado"""
        self.raio = raio  # 📏 Armazena o raio do circuito (em unidades)
    
    def calcular_area(self):
        """Calcula a área do circuito circular (π * raio²)"""
        return math.pi * (self.raio ** 2)  # 📊 Fórmula: A = πr²
    
    def calcular_circunferencia(self):
        """Calcula o comprimento da circunferência (2 * π * raio)"""
        return 2 * math.pi * self.raio  # 🔄 Fórmula correta: C = 2πr

if __name__ == "__main__":
    # 🟢 Criando uma instância de Circuito com raio 5 unidades
    meu_circulo = Circuito(5)

    # 📊 Exibindo cálculos (com 2 casas decimais)
    print(f"⚙️ Raio: {meu_circulo.raio} unidades")  # 📏 Valor do raio
    print(f"📦 Área: {meu_circulo.calcular_area():.2f} unidades quadradas")  # 🟣 Resultado ~78.54
    print(f"⏺️ Circunferência: {meu_circulo.calcular_circunferencia():.2f} unidades")  # 🔵 Resultado ~31.42