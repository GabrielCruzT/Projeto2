class Pessoa:
    def __init__(self,nome,idade,altura,peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def eh_maior(self):
        if self.idade>=18:
            return True
        else:
            return False

    def imc(self):
        self.imc = self.peso / (self.altura ** 2)
        return  self.imc
    
    def imc_longo(self):
        self.imc = self.peso / (self.altura ** 2)
        if self.imc <= 18.5:
            self.imc_longo = "Abaixo do normal"
        elif self.imc >= 18.6 and self.imc <= 24.9:
            self.imc_longo = "Normal"
        elif self.imc >= 25 and self.imc <= 29.9:
            self.imc_longo = "Sobrepeso"
        elif self.imc >= 30 and self.imc <= 34.9:
            self.imc_longo = "Obesidade grau I"
        elif self.imc >= 35 and self.imc <= 39.9:
            self.imc_longo = "Obesidade grau II"
        else:
            self.imc_longo = "Obesidade grau III"
        return  self.imc_longo
            

pessoa1 = Pessoa("Zezinho", 19, 1.53, 68.2)
print(pessoa1.imc_longo()) 
print(pessoa1.eh_maior())
