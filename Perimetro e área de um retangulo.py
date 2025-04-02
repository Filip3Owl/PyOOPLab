class Retangulo:
    
    def __init__(self, altura, largura):
        self.altura = altura  # 📏 Altura do retângulo
        self.largura = largura  # 📏 Largura do retângulo
    
    def calcular_area(self):
        return self.largura * self.altura  # 📊 Área = largura × altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)  # 🔄 Perímetro = 2 × (largura + altura)

# 🏗️ Criando um retângulo com altura=5 e largura=3
retangulo = Retangulo(5, 3)

# 🖨️ Exibindo os cálculos
print(f'Área: {retangulo.calcular_area()}')  # 📌 Saída: 15 (5 × 3)
print(f'Perimetro: {retangulo.calcular_perimetro()}')  # 📌 Saída: 16 (2 × (5 + 3))