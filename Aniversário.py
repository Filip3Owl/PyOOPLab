class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # 👤 Armazena o nome da pessoa
        self.idade = idade  # 🎂 Armazena a idade da pessoa

    def aniversario(self):
        self.idade += 1  # 🎉 Incrementa a idade em 1 ano (sem retorno)
        # 💡 Alternativa com retorno: return self.idade

    def apresentar(self):
        return f'Meu nome é {self.nome} e eu tenho {self.idade} anos.'  # 🗣️ Retorna string de apresentação

# 🍰 Criando uma pessoa chamada Filipe com 29 anos
dados = Pessoa('Filipe', 29)

# 🎊 Fazendo Filipe fazer aniversário (idade 29 → 30)
dados.aniversario()  # ⚠️ Não usamos print() pois o método não retorna nada

# 📢 Mostrando a apresentação atualizada
print(dados.apresentar())  # Saída: "Meu nome é Filipe e eu tenho 30 anos."