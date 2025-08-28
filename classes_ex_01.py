class AnimaisMarinhos:
    def __init__(self, nome, especie, local, tamanho, idade):
        self.nome = nome
        self.especie = especie
        self.local = local
        self.tamanho = tamanho
        self.idade = idade

    def nadar(self):
        return f"{self.nome} está nadando!"

    def comer(self):
        return f"{self.nome} está se alimentando."

    def dormir(self):
        return f"{self.nome} está dormindo."

    def som(self):
        return f"{self.nome} está emitindo um som característico."

    def info(self):
        return f"Nome: {self.nome}, Espécie: {self.especie}, Habitat: {self.local}"





animais = [
    AnimaisMarinhos("Nemo", "Peixe-palhaço", "Recife", "Pequeno", 2),
    AnimaisMarinhos("Baleia Azul", "Cetáceo", "Oceano", "Gigante", 80),
    AnimaisMarinhos("Polvo", "Molusco", "Fundo do mar", "Médio", 5),
    AnimaisMarinhos("Tubarão", "Cartilaginoso", "Oceano", "Grande", 25),
    AnimaisMarinhos("Golfinho", "Cetáceo", "Oceano", "Médio", 15)
]
