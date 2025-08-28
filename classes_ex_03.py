class pessoa:
    def __init__(self, nome, idade, cpf, email, telefone, endereco, altura, peso, genero, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.__email = email
        self._telefone = telefone
        self.endereco = endereco
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.nacionalidade = nacionalidade


    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_email(self):
        return self.__email

    def set_email(self, novo_email):
        self.__email = novo_email

    def falar(self):
        return f"{self.nome} está falando."

    def andar(self):
        return f"{self.nome} está andando."


    def _ligar(self):
        return f"{self.nome} está ligando para {self._telefone}."

    def _dormir(self):
        return f"{self.nome} está dormindo."
    



