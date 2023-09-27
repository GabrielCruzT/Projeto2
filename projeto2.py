
from datetime import datetime
class Pessoa:
    def __init__(self,nome,idade,altura,peso,nascimento):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.nascimento = nascimento

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

while True:
    nome_pessoa = input('Digite seu nome: ')
    idade_pessoa = input('Digite sua idade: ')
    altura_pessoa = input('Digite sua altura: ')
    peso_pessoa = input('Digite seu peso: ')
    nascimento_pessoa = input('Digite sua data de nascimento (formato dd/mm/aaaa): ')
    data_formato = "%d/%m/%Y"
    res = True
    try:
        res = bool(datetime.strptime(nascimento_pessoa, data_formato))
        altura_pessoa = float(altura_pessoa)
        peso_pessoa = float(peso_pessoa)
        idade_pessoa = int (idade_pessoa)
    except ValueError:
        res = False

    if all(c.isalpha() or c.isspace() for c in nome_pessoa) and idade_pessoa>0 and altura_pessoa>0 and peso_pessoa>0 and res==True:
        print("ok")
        break
    else:
        print("Dados errados")         

pessoa1 = Pessoa(nome_pessoa, idade_pessoa, altura_pessoa, peso_pessoa, nascimento_pessoa)

print(pessoa1.nome)
print(pessoa1.imc_longo()) 
print(pessoa1.eh_maior())
