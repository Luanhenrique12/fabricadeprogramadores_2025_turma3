class marinhos():
    def __init__(self, especie, tamanho_m, venenoso, profundidade):
        self.especie = especie
        self.tamanho_m = tamanho_m
        self.venenoso = venenoso
        self.profundidade = profundidade
        self.visitas = 0

    def mostrar_especie(self):
        print(f"Espécie: {self.especie}")

    def mostrar_tamanho(self):
        print(f"Tamanho: {self.tamanho_m} m")

    def mostrar_venenoso(self):
        print(f"É venenoso?: {self.venenoso}")

    def mostrar_profundidade(self):
        print(f"Profundidade: {self.profundidade} m")
    
    animal = marinhos(10.0, ["azul","branco", "cinza"], "baleias (Principalmente carcaças)", "carcharias" "carcharondon")
    animal.especie()